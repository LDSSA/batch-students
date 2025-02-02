# -*- coding: utf-8 -*-
"""
Script used to predict a class through transformers models.
"""
import logging
import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

project_dir = Path(__file__).resolve().parents[2]
device = torch.device("cpu")

class TransformerPredict:
    """Provides a prediction based on transformers and pre-trained models"""

    def __init__(self, model_name):
        self._model_name = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5, problem_type = "multi_label_classification").to(device)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)

    def predict(self, sentence: str) -> str:
        """Predict the binary class of a sentence using a Transformer model
        Args:
            Data (pd.DataFrame): DataFrame
        Returns:
            classes (str): Computer Vision and Pattern Recognition | Machine Learning | Computation and Language | Human-Computer Interaction | Information Retrieval
        """
        try:
            # Tokenizer parameters
            tokenizer_kwargs = {'padding': True, 'truncation': True, 'max_length': 512}

            # Define the pipeline
            pipeline = TextClassificationPipeline(model=self._model_name, tokenizer=self._tokenizer, return_all_scores=False, device=-1, **tokenizer_kwargs)

            return pipeline(sentence)

        except Exception:
            logging.error(f'directory or model is invalid or does not exist: {self._model_name}')
