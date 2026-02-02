# LDSSA Hackathon #4 - Predicting Judicial Recommendations for Clemency

## Schedule

| Hour  | Activity                          |
|-------|-----------------------------------|
| 08:15 | Arrival, Student setup            |
| 08:30 | Hackathon Prompt, Team Assignment |
| 09:00 | **Start Hacking!**                    |
| 12:30 | Lunch (keep hacking if you like)  |
| 14:00 | Goal - First Submission           |
| 15:00 | Goal - Improved Submission        |
| 16:00 | Start Working on Presentation     |
| 17:00 | **Stop Hacking!**                     |
| 17:30 | Team Presentations                |
| 18:20 | Instructor’s Presentation         |
| 18:30 | Winners Announced                 |
| 18:45 | Closing Remarks                   |

## Overview

Welcome to the **LDSSA Hackathon #4 - Predicting Judicial Recommendations for Clemency**! 🚀

This hackathon aims to build NLP models for predicting judicial recommendations for clemency from historical judges’ reports at the Old Bailey (1784–1827).

The task is to predict the judicial recommendation for clemency associated with a historical criminal case. The problem is formulated as a supervised multi-class classification task, where each case is assigned one of three labels: FAVOURABLE, UNFAVOURABLE, or NO_CLEAR_RECOMMENDATION.

Classification is performed at the level of individual cases, without assuming links between multiple records referring to the same individual.

## Data

The dataset used in this notebook is Judges’ Reports on Criminals convicted at the Old Bailey, 1784–1827. It consists of structured summaries derived from judges’ reports and related documents concerning individuals convicted at the Old Bailey between 1784 and 1827.

The dataset was created as part of the Digital Panopticon project and is based on item-level descriptions from the Home Office series HO 47 held at The National Archives (UK). The descriptions are archival summaries rather than full transcripts of the original documents.

Each row represents an individual case. An individual may appear more than once, and no attempt is made to link multiple records referring to the same person.

For the purposes of the hackathon, the original dataset has been simplified to retain only a small number of descriptive textual fields and the target label, in order to focus the task on textual reasoning and avoid information leakage.

**Dataset columns**:
- `crime`: Description of the offence.
- `initial_sentence`: Sentence passed at trial, as described.
- `grounds_clemency`: Stated grounds cited in favour of clemency.
- `additional_info`: Additional contextual information.
- `doc_description`: Archivist description of the document.
- `label`: Target variable used in this notebook.


## Recommendations
❗Begin with a straightforward baseline model to benchmark and guide the development of more advanced iterations.   
❗Improve your models by extracting relevant features from the data and/or tuning hyperparameters.   
❗Remember to understand your data before feature engineering.   
❗Distribute tasks wisely: one member can handle data exploration and cleaning, another can focus on model development and testing, and a third crafts visualizations to highlight insights from the dataset.   
❗Explore different language models.   
❗If processing time is a limit, try out online platforms like Kaggle or Google Colab.

## Hints for Success
❗Own the data: Understand your dataset thoroughly to uncover valuable insights.   
❗Preprocess correctly: Remove the unnecessary characters, …   
❗Feature engineering: Try out different ways of feature extraction.   
❗Reduce the dimensionality: Select the most important features.   
❗Iterate Quickly: Start simple and iteratively refine your models for consistent improvement.   
❗ Enjoy the hackathon and learn as much as you can! 🎉

## Evaluation Criteria

Model performance is evaluated using the **macro-averaged F1 score** as the primary metric. Additional metrics, including per-class precision and recall, are reported for diagnostic purposes.

## Hackathon Rules

- The selection of the teams is random. 
- Instructors will be available to help at any time. The instructors will not help your team solve the challenge, but they will help your team to be on track and answer technical questions that your team might have.
- No more submissions and questions to the instructors shall be done after the end of the challenge.
- Your team will have to prepare a presentation to share your findings with everyone. See the presentation guidelines below. This presentation will be considered in the overall evaluation of your team, so don’t consider it less important than the ML model!
- You can submit your predictions up to five times to evaluate your MAE score. The best will be chosen for the team’s best score.
- The final rank is calculated as:

   FinalRank = 0.5 * F1_rank + 0.5 * Presentation_rank

   Where:
   - MAE_rank is the rank of your team in the leaderboard, considering the score of your best submission
   - Presentation_rank is the rank of your team in the presentation evaluation

- The teams will be sorted by FinalRank ascending, and the first team wins!

## Presentation Guidelines

- The presentation can take a maximum of 4 minutes. This is a hard limit! We’ll literally silence you and move on to the next group after the 4 minutes have passed.
- The presentation should be clear, structured, and informative. Suggested format:
   - Problem description and formulation
   - Data science workflow
   - Data cleaning and exploration
   - Modelling: SARIMAX, ML models, both? Hyperparameter tuning can take a while, can you make some valid assumptions to make it faster? 
   - Interpreting results
   - Recommendations / Future work if you had more time to work on the problem
   - A funny pun at the end (not mandatory, but everyone loves it)!
- You can use this template if you want (make a copy of it and edit your copy): https://docs.google.com/presentation/d/1_qhG8xZYUuk25YEKKHD5-oF-wXsOeG_yZm0EcdnO440/edit?usp=sharing
- Charts/tables/great visuals are encouraged in your presentation. We actually have an evaluation criteria for the presentation which is “Used relevant visuals” (note the relevant!)
- The team can decide who is presenting. There are no rules here, you can go with one person presenting everything or having everyone presenting a part.

## After the hackathon

The leaderboard will be reopened after today so that you can keep trying to improve your score!

**Good luck, and may the best predictions win!** 🎯
