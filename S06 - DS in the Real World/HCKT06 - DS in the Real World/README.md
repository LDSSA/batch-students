# LDSSA Hackathon #6 - Traffic across borders

## Schedule

| Hour  | Activity                          |
|-------|-----------------------------------|
| 08:15 | Arrival, Student setup            |
| 08:30 | Hackathon prompt, team assignment |
| 09:00 | **Start Hacking!**                |
| 12:15 | Trial round - test your servers   |
| 12:30 | Lunch (keep hacking if you like)  |
| 13:45 | First evaluation                  |
| 16:00 | Start working on the presentation     |
| 16:15 | Final evaluation                  |
| 17:00 | **Stop Hacking!**                 |
| 17:30 | Team presentations                |
| 18:20 | Instructor’s presentation         |
| 18:30 | Winners announced                 |
| 18:45 | Closing remarks                   |

## Overview

Welcome to the **LDSSA Hackathon #6 - Predicting traffic on US borders**! 🚀

You've been hired by the Customes Department to help plan the deployment of customs officers on the US border crossings. You've been provided with about 10 years of data from all the border crossings on the US-Mexico and US-Canadian borders.

Your goal is to build and deploy a model that predicts the volume of people, vehicle, and container traffic on all border crossings for the next six months.

## Dataset

All the data is in the file train.csv.

### Columns in the dataset:

- Place, State, Code, Border: the name, the state, the code, and the placement of the border crossing
- Trafic: the kind of traffic - which vehicle, container or traveller type crossed the border
- Value: how many vehicles/containers/people crossed in the given month
- Date: the month for which the data was collected

## Objective

Your task is to build an API that can be used by the customs department for planning the staff deployment to the border crossings with the regard to the expected traffic. The API should predict the volume of people, container, and vehicle traffic up to six months from the last datapoint (Sep 2025 - Feb 2026). 

The service should have two endpoints:
- Predict: where they will send requests for predictions. The endpoint takes two inputs - the code of the border crossing and the traffic type (people, vehicles, containers). The endpoint should return predictions for the next 6 months (Sep 2025 - Feb 2026).
- Update: where they will send actual traffic volumes at the end of each month.

|Endpoint | Expected payload (input) | Expected response (output)|
|---|---|---|
|POST /predict | {"port_code": 3004, <br> "traffic": "people" }|{"port_code": 3004, <br> "traffic": "people",  prediction: "5045 3023 7087 6530 3210 1200"}|
|POST /update | {"date": "Sep 2025", , <br> "port_code": 3004, <br> "traffic": "people", <br> "true_value": 6400}|{"date": "Sep 2025",  <br> "port_code": 3004, <br> "traffic": "people", <br> "true_value": 6400}|

If your application receives a request that doesn't conform to the specified formats, it should either return an appropriate error message or disregard the request. Importantly, your system must be robust and fault-tolerant, meaning it shouldn’t crash due to an anomalous request!

During the trial round, several test requests will be sent to verify if your endpoints function correctly. By this stage, you should have already provided your endpoint details so they can be accessed for queries.

In the first round of evaluation, your server will be queried for predictions from the test set. The score will be calculated with the given metric and displayed on the leaderboard, allowing you to gauge your performance against other competing teams. Next, a round of updates will be communicated back to your update endpoint, which you should capture and use as feedback to refine your model in preparation for the final evaluation. If you happen to fail to store the update data, it will be forwarded to you in a CSV format, but be aware that there will be penalties for not maintaining your server adequately. 

After retraining and reassessing your model, you will enter the final evaluation stage. During this period, your server will face a series of prediction requests, culminating in the final score.

## Evaluation Criteria

You will be assessed based on several metrics: 

- MAPE calculated on all predictions.

- Fairness Penalty calculated from how well the predictions perform for the same type of traffic at different crossing and for the different traffic types on the same crossing. The client would like the model to perform similarly well for all three traffic types (people, vehicles, containers) in the same crossing. They would also like to see the same performance for the people traffic on the two borders (Mexico and Canada) which means that the MAPEs should not differ significantly across each border. The maximum acceptable difference between the best and worse MAPE can be 15 percentage points. If the largest discrepancy between the MAPEs is larger, you will be penalized by the difference, e.g. if your largest discrepancy is 20 percentage points, you will be penalized by 0.05 (0.20-0.15). If you meet the requirement, fairness penalty is 0. The fairness penalty will increase your overall MAPE.

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

✅ Take advantage of the trial run to verify the correct functioning of the service. You should check your app logs to make sure there were no errors. You can use the dummy score on the leaderboard to make sure your predictions were delivered correctly. In this round, your app doesn't need to contain a great model, but it should return some predictions to make sure that your workflow is smooth.

✅ In case you submitted some requests to test your app and you see issues with the database (eg. errors saving new requests) reset the database by removing the service and de-linking it from your app (we still haven’t figured out a better way to do this in Railway). Do this only before the first official evaluation moment.

✅ Divide and conquer: one person sets up the server, another works on its robustness, another works on the model.

✅ Remember: More data doesn’t always mean better results.

✅ Remember: More complex models don’t always yield better results.

✅ The presentation can take a maximum of 4 minutes. This is a hard limit! We’ll literally silence you and move on to the next group after the 4 minutes have passed.

✅ The team can decide who is presenting. There are no rules here, you can go with one person presenting everything or having everyone presenting a part. Try to get someone to present who did not yet have a chance to present in the previous hackathons.

✅ Communicate well within your team to distribute tasks efficiently..

✅ Enjoy the hackathon and learn as much as you can! 🎉


**Good luck, and may the best servers and predictions win!** 🎯
