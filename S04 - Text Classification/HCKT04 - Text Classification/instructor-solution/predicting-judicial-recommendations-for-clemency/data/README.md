# Hackathon Dataset

This directory contains the train and test splits used in the NLP hackathon task on predicting judicial recommendations for clemency. The data is derived from *Judges’ Reports on Criminals convicted at the Old Bailey, 1784–1827* and has been reduced for hackathon use.

## Files

- `trials_train.csv`
- `trials_test.csv`

## Columns

The datasets contain the following columns only:

- `crime`
- `initial_sentence`
- `grounds_clemency`
- `additional_info`
- `doc_description`
- `label`

## Exclusions

The following fields are not included:

- identifiers and archival references
- recommendation or outcome fields
- categorical sentence metadata
- biographical and administrative metadata

## Notes

- Each row represents an individual case.
- Records are not linked across rows.