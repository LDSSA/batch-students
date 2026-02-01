# -*- coding: utf-8 -*-
"""
Script used to evaluate transformer models.
Usage:
    python -m src.models.evaluate_model <model_name>
"""
import logging
import argparse
import torch
import numpy as np
from pathlib import Path
from datasets import Dataset
from src.data.text_preprocessing import TextPreprocessing, convert_labels
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import Trainer
from src.data.read_dataset import get_data

project_dir = Path(__file__).resolve().parents[2]
device = torch.device("cpu")

def compute_metrics(raw_predictions):
    """Compute metrics using the ground truth and predicted values"""
    #predictions, labels, metrics = raw_predictions
    predictions, labels = raw_predictions
    predictions = np.argmax(predictions, axis=1)

    accuracy = accuracy_score(y_true=labels, y_pred=predictions)
    recall = recall_score(y_true=labels, y_pred=predictions, average='weighted')
    precision = precision_score(y_true=labels, y_pred=predictions, average='weighted')
    f1 = f1_score(y_true=labels, y_pred=predictions, average='weighted')

    return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}


class TransformerEvaluation:
    """Provides an evaluation based on transformers and pre-trained models"""

    def __init__(self, model_name):
        self._model_name = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5).to(device)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)

    def evaluate(self) -> None:
        """Predict the classes of a testset and provide an evaluation through accuracy, precision, recall and f1 metrics."""
        try:
            # Load test data
            _, _, df_test = get_data()

            # Convert labels to int
            label2int = convert_labels(df_test["label"])
            df_test["label"] = df_test["label"].apply(lambda x: label2int[x])

            # Create torch dataset
            hf_test = Dataset.from_pandas(df_test)

            # Perform tokenization
            tokenized_test = hf_test.map(TextPreprocessing(self._tokenizer).tokenize_text, batched=True)

            # Define eval object
            test_trainer = Trainer(model=self._model_name)

            # Make prediction
            raw_predictions = test_trainer.predict(tokenized_test)

            # Compute metrics
            return compute_metrics(raw_predictions)

        except Exception:
            logging.error(f'directory or model is invalid or does not exist: {self._model_name}')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Parser descriptors
    parser = argparse.ArgumentParser(
        description='''Script used to evaluate trained models.''')

    parser.add_argument('model_name',
                        type=str,
                        default='checkpoint-32924',
                        help='Choose the fine-tuned transformer model to be used in the evaluation. The file must be inside the ./model/ directory and must be a torch model: {checkpoint-32924}.')

    args = parser.parse_args()

    model_path = project_dir / 'model' / args.model_name

    logging.info(TransformerEvaluation(model_path).evaluate())
