# LDSSA Hackathon #6 - Patient days in hospitals

## Schedule

| Hour  | Activity                          |
|-------|-----------------------------------|
| 08:15 | Arrival, Student setup            |
| 08:30 | Hackathon Prompt, Team Assignment |
| 09:00 | **Start Hacking!**                |
| 12:15 | Trial round - test your servers   |
| 12:30 | Lunch (keep hacking if you like)  |
| 13:45 | First evaluation                  |
| 16:00 | Start Working on Presentation     |
| 16:15 | Final evaluation                  |
| 17:00 | **Stop Hacking!**                 |
| 17:30 | Team Presentations                |
| 18:20 | Instructor’s Presentation         |
| 18:30 | Winners Announced                 |
| 18:45 | Closing Remarks                   |

## Overview

Welcome to the **LDSSA Hackathon #6 - Predicting hospital inpatient stay length**! 🚀

You've been hired by the Department of Health to help plan the hospital bed occupancy in the state of NY. They provided anonymized patient data admitted to the hospital in the past year. The data contains demographic and medical descriptors for each patient and hospital.

Your goal is to build and deploy a model that predicts the length of the hospital stay for each newly admitted patient.

## Dataset

All the data is in the file train.zip.

### Columns in the dataset:

- data about the hospital: Health Service Area, Hospital County, Operating Certificate Number, Facility Id, Facility Name,
- patient demographic data: Age Group, Zip Code - 3 digits, Gender, Race, Ethnicity,
- days of stay of patient in the hospital: Length of Stay
- patient medical data: Type of Admission, Patient Disposition, Discharge Year, CCS Diagnosis Code, CCS Diagnosis Description, CCS Procedure Code, CCS Procedure Description, APR DRG Code, APR DRG Description, APR MDC Code, APR MDC Description, APR Severity of Illness Code, APR Severity of Illness Description, APR Risk of Mortality, APR Medical Surgical Description
- patient insurance data: Payment Typology 1, Payment Typology 2, Payment Typology 3, Attending Provider License Number, Operating Provider License Number, Other Provider License Number,
- other: Birth Weight, Abortion Edit Indicator, Emergency Department Indicator, Total Charges, Total Costs

## Objective

Your task is to build an API that can be used by hospital managers to obtain a prediction of the length of the hospital stay for newly admitted patients.

The service should have two endpoints:
- Predict: where they will send requests for predictions
- Update: where they will send actual outcomes when the patient is discharged from the hospital.

|Endpoint | Expected payload (input) | Expected response (output)|
|---|---|---|
|POST /predict | {"observation_id": "fd3f9217-9f93-47f5-9375-dd2386e92e5f", <br> "Health Service Area": "Western NY", <br> "Hospital County": "Erie",<br> "Operating Certificate Number": "1401014.0", <br> "Facility Id": "207.0", <br>"Facility Name": "Buffalo General Hospital",<br>"Age Group": "30 to 49",<br>"Zip Code - 3 digits": "147",<br>"Gender": "F",<br>"Race": "White",<br>"Ethnicity": "Not Span/Hispanic",<br>"Type of Admission": "Emergency",<br>"CCS Diagnosis Code": "157",<br>"CCS Diagnosis Description": "Acute and unspecified renal failure",<br>"CCS Procedure Code": "0",<br>"CCS Procedure Description": "NO PROC",<br>"APR DRG Code": "460",<br>"APR DRG Description": "RENAL FAILURE",<br>"APR MDC Code": "11",<br>"APR MDC Description": "Diseases and Disorders of the Kidney and Urinary Tract",<br>"APR Severity of Illness Code": "3",<br>"APR Severity of Illness Description": "Major",<br>"APR Risk of Mortality": "Major",<br>"APR Medical Surgical Description": "Medical",<br>"Payment Typology 1": "Medicaid",<br>"Payment Typology 2": "Self-Pay",<br>"Payment Typology 3": "nan",<br>"Attending Provider License Number": "237483.0",<br>"Operating Provider License Number": "nan",<br>"Other Provider License Number": "nan",<br>"Birth Weight": "0",<br>"Abortion Edit Indicator": "N",<br>"Emergency Department Indicator": "Y"}|{"observation_id": "fd3f9217-9f93-47f5-9375-dd2386e92e5f",<br>   "prediction": "5"}|
|POST /update | {"observation_id": ""fd3f9217-9f93-47f5-9375-dd2386e92e5f",<br>"true_value": "4"<br>}|{"observation_id": "fd3f9217-9f93-47f5-9375-dd2386e92e5f",<br>"true_value": "4"}|

If your application receives a request that doesn't conform to the specified formats, it should either return an appropriate error message or disregard the request. Importantly, your system must be robust and fault-tolerant, meaning it shouldn’t crash due to an anomalous request!

A preliminary evaluation phase will take place, during which several test cases will be sent to verify if your endpoints function correctly. By this stage, you should have already provided your endpoint details so they can be accessed for queries. Soon after, the first round of evaluations will begin, where your server will be queried for predictions. The outcomes will be calculated based on the initial metric and displayed on a leaderboard, allowing you to gauge your performance against other competing teams.

Following the predictions, a round of updates will be communicated back to your update endpoint, which you should capture and use as feedback to refine your model in preparation for the ultimate round of predictions. If you happen to fail in storing the update data, it will be forwarded to you in a CSV format, but be aware that there will be penalties for not maintaining your server adequately. After retraining and reassessing your model, you will enter the final evaluation stage. During this period, your server will face a series of prediction requests, culminating in a final score.

## Evaluation Criteria

You will be assessed based on several metrics: 

- MSE calculated on all predictions.

- Fairness Penalty calculated from how well the predictions perform for patients of different races. The client would like the model to perform similarly well for patients of all races. The maximum acceptable difference between the best and worse MSE calculated per race can be 15%. If the largest discrepancy between the MSEs by race is larger, you will be penalized by the difference, e.g. if your largest discrepancy is 20%, you will be penalized by 0.05 (0.20-0.15). If you meet the requirement, fairness penalty is 0. The fairness penalty will increase your overall MSE.

- Server Reliability: Your predictions will only be processed if your server is stable and responds to all requests. While there is no explicit metric for reliability, your overall performance could be affected by it.

## Hackathon Rules

- Team Formation: Teams will be randomly assigned.
- Instructor Support: Instructors will be available to help with technical questions, but will not provide solutions.
- Final Presentation: Each team must present their work in a 4-minute presentation.

## Presentation Guidelines

Your presentation should be clear, structured, and informative. Suggested format:

1. Problem description
2. Data cleaning and exploration
3. Feature engineering and modeling approach
4. Deployment details
5. Evaluation and results
6. Future work & improvements
7. A funny pun at the end (VERY IMPORTANT!)

## Tips for Success, but you are free to do what works best for you

✅ Establish a simple baseline for the task and make sure you assess not only the leaderboard metric but also the client requirements.

✅ Set up your service and make sure it is functioning correctly (both endpoints!)

✅ Take advantage of the trial run to verify the correct functioning of the service. You should check your app logs to make sure there were no errors. You can use the dummy score on the leaderboard to make sure your scores were delivered correctly. Remember: these will be dummy examples, so the scores themselves do not necessarily reflect the quality of the model.

✅ In case you submitted some requests to tests your app and you see issues with the database (eg. errors saving new requests) reset the database by removing the service and de-linking it from your app (we still haven’t figured out a better way to do this in Railway). Do this only before the first official evaluation moment.

✅ Divide and conquer: one person sets up the server, another works on its robustness, another works on the model.

✅ Remember: More data doesn’t always mean better results.

✅ Remember: More complex models don’t always yield better results.

✅ The presentation can take a maximum of 4 minutes. This is a hard limit! We’ll literally silence you and move on to the next group after the 4 minutes have passed.

✅ The team can decide who is presenting. There are no rules here, you can go with one person presenting everything or having everyone presenting a part.

✅ Communicate well within your team to distribute tasks efficiently..

✅ Enjoy the hackathon and learn as much as you can! 🎉


**Good luck, and may the best servers and predictions win!** 🎯
