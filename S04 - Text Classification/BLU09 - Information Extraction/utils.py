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
