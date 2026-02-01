# -*- coding: utf-8 -*-
"""
Script used to preprocess datasets files.
"""
from bs4 import BeautifulSoup


def convert_labels(labels):
    """Convert labels into integer format."""
    pass


def remove_html(sentence) -> str:
    """Take a sentence and remove the html tags."""
    clean_sentence = ""
    if sentence is not None:
        soup = BeautifulSoup(sentence, 'html.parser')
        clean_sentence = soup.get_text()
        clean_sentence = clean_sentence.strip()
        clean_sentence = clean_sentence.replace('\n', " ")
        clean_sentence = clean_sentence.replace('\t', " ")
        clean_sentence = " ".join(clean_sentence.split())
    return clean_sentence


class TextPreprocessing(object):
    """
    Handles text pre-processing
    """

    def __init__(self, tokenizer):
        self._tokenizer = tokenizer

    def tokenize_text(self, text):
        """Perform tokenization in a text."""
        return self._tokenizer(text["Abstract"], truncation=True, padding=True, max_length=512)
