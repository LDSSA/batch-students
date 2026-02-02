# Predicting Judicial Recommendations for Clemency (NLP Hackathon)

This repository contains a notebook developed for an NLP hackathon focused on predicting judicial recommendations for clemency using historical legal records.

The task is framed as a multi-class text classification problem using the *Judges’ Reports on Criminals convicted at the Old Bailey, 1784–1827* dataset. The notebook explores baseline models, an instructors’ solution, and several alternative approaches, with an emphasis on interpretability and empirical comparison.

---

## Contents

- A single Jupyter notebook implementing:
  - Task definition and data exploration
  - A minimal baseline using a single textual field
  - An instructors’ solution using broader textual context
  - Comparative experiments with alternative representations and models
  - Error analysis and discussion of results

---

## Installation

Create and activate a virtual environment, then install dependencies:
```console
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```
