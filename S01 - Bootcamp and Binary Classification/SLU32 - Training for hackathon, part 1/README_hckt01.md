# LDSSA Hackathon #1 - Binary classification

## Schedule

| Hour  | Activity                          |
|-------|-----------------------------------|
| 08:15 | Arrival, Student setup            |
| 08:30 | Hackathon Prompt, Team Assignment |
| 09:00 | Start Hacking!                    |
| 12:30 | Lunch (keep hacking if you like)  |
| 14:00 | Goal - First Submission           |
| 15:00 | Goal - Improved Submission        |
| 16:00 | Start Working on Presentation     |
| 17:00 | Stop Hacking!                     |
| 17:30 | Team Presentations                |
| 18:20 | Instructor’s Presentation         |
| 18:30 | Winners Announced                 |
| 18:45 | Closing Remarks                   |

---

## Overview

In this hackathon, we will delve into the critical and ever-evolving field of heart disease prediction.

Heart disease remains one of the leading causes of death globally. With the rise of wearable technology, electronic health records (EHR), and patient monitoring systems, a wealth of data is now available to predict and prevent heart-related conditions. Early diagnosis is essential, as timely interventions can dramatically reduce the risk of severe health outcomes and improve the quality of life for millions.

Machine learning has emerged as a powerful ally in healthcare, enabling us to analyse vast amounts of patient data and uncover hidden patterns that may not be apparent through traditional diagnostic methods. By leveraging advanced algorithms, we can predict the likelihood of heart disease in patients based on factors such as age, blood pressure, cholesterol levels, lifestyle choices, and medical history. These models hold the potential to transform the way we approach preventive care and ensure that high-risk individuals receive the attention they need.

Today, your challenge will be to build a machine learning model capable of predicting whether a patient is likely to develop heart disease. You will be working with a dataset of anonymized patient records, containing various features such as **demographic data, lifestyle choices, and clinical measurements. The dataset comprises ~222,000 patient records, with approximately 19,000 confirmed heart disease cases. Your task is to** predict whether a patient will develop heart disease based on their profile.

To offer some insight, heart disease prediction often relies on recognizing patterns and risk factors that are not always immediately obvious. For instance, sudden spikes in cholesterol levels, changes in blood pressure, or specific age groups may correlate with a higher likelihood of heart disease.

In order to save you time, you can use the requirements.txt in the Bootcamp directory which identifies some basic packages that you should install right away when setting up your virtual environment for the hackathon. Please bear in mind that they are not mandatory to use, and if you are more comfortable using other packages feel free to do so.

**Disclaimer**: This hackathon is intended for educational purposes only. Predicting heart disease is a complex task that requires access to a wider set of clinical data, specialised models, and expert medical knowledge. The results may not reflect real-world medical accuracy, so please treat this as a learning exercise in the field of healthcare data science.
Good luck, and we look forward to seeing the innovative solutions you come up with!

--- 

## Objective

**The main goal is to predict whether a patient will develop a heart disease or not.**
For each event in the test dataset, you’ll have to predict the probability of it being an actual fraud.

Your submission file should be a CSV with two columns:
- **id**: the id of the patient
- **result**: the probability of the patient developing a heart disease

When you submit your predictions, some validations will be run that will check the following:
Your file has the two columns with the right name
Your file has the right number of events
Your file has the same event ids as the test dataset. The submission is sorted by id, so the order doesn’t matter
Your predictions are probabilities and not just 0s and 1s

---

## Dataset

You can find all these files in data/ under the hackathon directory.
- train.csv - Training set (222k events)
- test.csv - Test set (95k events)
- sample_submission.csv - Submission file example

### Data dictionary

**id** - patient id
**BMI** - Body Mass Index (BMI)
**Smoking** - if patient smokes
**AlcoholDrinking** - if patient drinks alcohol
**Stroke** - had a stroke in the past
**PhysicalHealth** - how many days during the past 30 days was physical health not good
**MentalHealth** - how many days during the past 30 days was mental health not good
**DiffWalking** - serious difficulty walking or climbing stairs
**Sex** - patient’s gender
**Age** - patient’s age
**Race** - patient’s race
**Diabetic** - if patient is diabetic
**Weekly PhysicalActivity (H)** - hours of physical activity on a weekly basis
**GenHealth** - would you say your general health is?
**SleepTime** - average hours of sleep in a 24-hour period
**Asthma** - if patient has asthma
**KidneyDisease** - history of kidney disease
**SkinCancer** - if patient has asthma
**External Heart Test Score** - heart test score provided by an external entity
**HeartDisease** - developed a heart disease

---

## Recommendations
-❗Remember: “weeks of planning can save hours of programming”, so work with your team to plan and distribute work before diving in! 
-❗Focus on feature engineering and data understanding/exploration, which type of features you can build to better detect heart disease patterns..
-❗Make sure that you get to and submit a baseline ASAP! Then work on improving it.

---

## Evaluation criteria for your model

Evaluation Metric - Area Under Receiver Operating Characteristic Curve (AUROC).

You learned about this metric in SLU10 - Metrics for classification.

---

## Hackathon Rules

- The selection of the teams is **random**. 
- Instructors will be available to help at any time. The instructors will **not** help your team solve the challenge but they will help your team to be on track and answer technical questions that your team might have.
- **No more submissions and questions** to the instructors shall be done after the end of the challenge. 
- Your team will have to prepare a presentation to share your findings with everyone. See the presentation guidelines below. This presentation will be considered in the overall evaluation of your team, so don’t consider it less important than the ML model!
- You can submit your predictions up to five times to evaluate your AUROC score. The best will be chosen for the team’s best score.
- The final rank is calculated as:

   FinalRank = 0.5 * AUROC_rank + 0.5 * Presentation_rank

   Where:
 - AUROC_rank is the rank of your team in the leaderboard, considering the score of your best submission
 - Presentation_rank is the rank of your team in the presentation evaluation

   The teams will be sorted by FinalRank ascending, and the first team wins! 

---

## **Presentation Guidelines**

Your presentation should be clear, structured, and informative. Suggested format:

1. **Problem description**
2. **Data cleaning and exploration**
3. **Feature engineering and modeling approach**
4. **Evaluation and results**
5. **Future work & improvements**
6. **A funny pun at the end (VERY IMPORTANT!)**

---

**Good luck!** 🎯
