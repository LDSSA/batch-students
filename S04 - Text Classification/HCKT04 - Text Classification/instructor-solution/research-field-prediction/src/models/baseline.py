import logging
import argparse
import numpy as np
import spacy
import re
import string

# NLTK imports
from nltk.tokenize import WordPunctTokenizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

from pathlib import Path
from src.data.read_dataset import get_data
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin, BaseEstimator
#from src.data.text_preprocessing import convert_labels
nlp = spacy.load("en_core_web_lg")

project_dir = Path(__file__).resolve().parents[2]


# Custom transformer to implement sentence cleaning
class TextCleanerTransformer(TransformerMixin):
    def __init__(self, tokenizer, stemmer, regex_list,
                 lower=True, remove_punct=True):
        self.tokenizer = tokenizer
        self.stemmer = stemmer
        self.regex_list = regex_list
        self.lower = lower
        self.remove_punct = remove_punct

    def transform(self, X, *_):
        X = list(map(self._clean_sentence, X))
        return X

    def _clean_sentence(self, sentence):

        # Replace given regexes
        for regex in self.regex_list:
            sentence = re.sub(regex[0], regex[1], sentence)

        # Lowercase
        if self.lower:
            sentence = sentence.lower()

        # Split sentence into list of words
        words = self.tokenizer.tokenize(sentence)

        # Remove punctuation
        if self.remove_punct:
            words = list(filter(lambda x: x not in string.punctuation, words))

        # Stem words
        if self.stemmer:
            words = map(self.stemmer.stem, words)

        # Join list elements into string
        sentence = " ".join(words)

        return sentence

    def fit(self, *_):
        return self


class VectorTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, nlp):
        self.nlp = nlp
        self.dim = 300

    def fit(self, X, y):
        return self

    def transform(self, X):
        return np.array([self.nlp(text).vector for text in X])


class BaselinePredict:
    """
    Provides a classic baseline for comparison
    Usage:
    python -m src.models.baseline <sentence>
    """

    def __init__(self, model_name):
        self._model = self.train(model_name)

    def predict(self, sentence: str):
        """Predict the class of an abstract using a Logistic Regression
        Args:
            sentence (str): sentence
        Returns:
            multi classes (str): Computer Vision and Pattern Recognition | Machine Learning | Computation and Language | Human-Computer Interaction | Information Retrieval
        """
        # predict
        test_pred = self._model.predict([sentence])
        return test_pred

    def train(self, model) -> str:
        """Train a logistic regression method"""
        try:
            # Initialize a tokenizer and a stemmer
            tokenizer = WordPunctTokenizer()
            stemmer = SnowballStemmer("english", ignore_stopwords=True)
            regex_list = [("<[^>]*>", "")]

            # pipeline
            pipeline = Pipeline([
                #('text_embeddings', VectorTransformer(nlp)),
                ('prep', TextCleanerTransformer(tokenizer, stemmer, regex_list)),
                ('vect', CountVectorizer(stop_words='english', ngram_range=(1,2))),
                ('tfidf', TfidfTransformer()),
                ('lr', LogisticRegression(multi_class='auto', max_iter=10000))
            ])

            # data
            df_train, _, _ = get_data()

            # text
            train_texts = df_train['Abstract']

            # fit
            pipeline.fit(train_texts, df_train['label'])

            return pipeline

        except Exception:
            logging.error(f'directory or model is invalid or does not exist: {self._model}')
