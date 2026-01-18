import re

def remove_punctuation(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text.lower()

def remove_stopwords(text, stopwords, tokenizer):
    """ Preprocess text column
        df: pd.Series, text to process
        df_processed: pd.Series, processed text
    """    
    tokens = tokenizer.tokenize(text)    
    tokens = [tok for tok in tokens if tok not in stopwords]
    text_processed = ' '.join(tokens)
    return text_processed

'''
import spacy
from spacy.tokens import DocBin

nlp = spacy.load('en_core_web_md')
nlp.add_pipe("merge_entities", after="ner")

doc_bin = DocBin()
for doc in nlp.pipe(df["text"], batch_size=20, n_process=cpu_count-1):
    doc_bin.add(doc)

print(doc_bin.__len__)
doc_bin.to_disk("data/processed_docs.spacy")
'''