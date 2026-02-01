# -*- coding: utf-8 -*-
"""
Script used to fine-tune pre-trained transformers models.
Usage:
    python -m src.models.train_model <model_name>
"""
import os
import logging
import argparse
import torch
from pathlib import Path
from datasets import Dataset
from src.data.read_dataset import get_data
from src.data.text_preprocessing import TextPreprocessing
from transformers import TrainingArguments, Trainer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from src.models.evaluate_model import compute_metrics

project_dir = Path(__file__).resolve().parents[2]
device = torch.device("cpu")

class TransformerFineTuning:
    """
    Provides a fine-tuned transformer model based on pre-trained models"""

    def __init__(self, model_name):
        self._model_name = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5).to(device)
        self._tokenizer = AutoTokenizer.from_pretrained(model_name)

    def train(self) -> None:
        """Train Transformer models"""
        try:
            # Load data
            df_train, df_dev, _ = get_data()

            # Create torch dataset
            hf_train = Dataset.from_pandas(df_train)
            hf_dev = Dataset.from_pandas(df_dev)

            # Perform tokenization
            tokenized_train = hf_train.map(TextPreprocessing(self._tokenizer).tokenize_text, batched=True)
            tokenized_dev = hf_dev.map(TextPreprocessing(self._tokenizer).tokenize_text, batched=True)

            # Define training arguments
            training_args = TrainingArguments(
                output_dir=project_dir / "model",
                evaluation_strategy="epoch",
                save_strategy="epoch",
                learning_rate=2e-5,
                per_device_train_batch_size=16,
                per_device_eval_batch_size=16,
                num_train_epochs=4,
                weight_decay=0.01,
                save_total_limit=1,
                load_best_model_at_end=True,
            )

            # Define trainer object
            trainer = Trainer(
                model=self._model_name,
                args=training_args,
                train_dataset=tokenized_train,
                eval_dataset=tokenized_dev,
                tokenizer=self._tokenizer,
                compute_metrics=compute_metrics,
            )

            # Make training
            trainer.train()

            # Save the best model explicitly to a clean directory
            trainer.save_model(os.path.join(training_args.output_dir, "best_model"))

        except Exception:
            logging.error(f'directory or model is invalid or does not exist: {self._model_name}')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Parser descriptors
    parser = argparse.ArgumentParser(
        description='''Script used to fine-tune a pre-trained transformer model.''')

    parser.add_argument('model_name',
                        type=str,
                        default='distilbert-base-uncased',
                        help='Pre-trained transformer model, e.g. distilbert-base-uncased')

    args = parser.parse_args()

    TransformerFineTuning(args.model_name).train()
