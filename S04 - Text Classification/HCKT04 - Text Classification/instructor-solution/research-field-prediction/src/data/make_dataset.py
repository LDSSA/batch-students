# -*- coding: utf-8 -*-
"""
Script used to read external files in order to generate training, development and test sets.
Usage:
python -m src.data.make_dataset <dataset_file> <testset_file>
"""
import argparse
import logging
import pandas as pd
from pathlib import Path
from src.data.text_preprocessing import remove_html
from src.data.read_dataset import balance_data, split_data

project_dir = Path(__file__).resolve().parents[2]


def create_train_test_sets(df: pd.DataFrame, train_frac: float, balanced: bool,) -> None:
    """
    Create training and test sets with the same class distribution, in order to train and evaluate trained models

    param dataset_file: Data to be split
    param train_frac: Ratio of train set to whole dataset
    param balanced: Downsample majority class equal to the number of samples in the minority class
    """
    path = project_dir / 'data' / 'processed'
    if path.exists():
        try:
            # Balance by class
            if balanced:
                df = balance_data(df)

            # Get labels
            labels = pd.concat([df['label']], axis=1)

            # Split data
            df_train, df_dev = split_data(df, labels, train_frac)

            # Resume
            logging.info('\ntrain-------------------------------------------------------------')
            logging.info(df_train.shape)
            logging.info('label     %')
            logging.info(f" {round(df_train.groupby('label')['Abstract'].count() * 100 / df_train.shape[0], 2)}")

            logging.info('\ndev-------------------------------------------------------------')
            logging.info(df_dev.shape)
            logging.info('label     %')
            logging.info(f" {round(df_dev.groupby('label')['Abstract'].count() * 100 / df_dev.shape[0], 2)}")

            # Save files
            df_train.to_csv(path / 'train.csv', index=False)
            df_dev.to_csv(path / 'dev.csv', index=False)
        except pd.errors.EmptyDataError:
            logging.error(f'directory or file is invalid or does not exist: {path}')


if __name__ == '__main__':
    # Parser descriptors
    parser = argparse.ArgumentParser(
        description='''Script used to read external files in order to generate training, development and test sets.''')

    parser.add_argument('dataset_file',
                        help='Choose the dataset to be split into train, dev and test. The file must be inside the ./data/raw/ directory and the extension must be .csv: {dataset.csv}.')

    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    args = parser.parse_args()

    dataset_path = project_dir / 'data' / 'raw' / args.dataset_file
