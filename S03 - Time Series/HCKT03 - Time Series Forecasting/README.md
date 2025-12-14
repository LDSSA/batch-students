# LDSSA Hackathon #3 - The wind and the electricity price

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

Welcome to the **LDSSA Hackathon #3 - Electricity price prediction**! 🚀

In this hackathon you’ll get to test your multistep time series forecasting skills with exogenous data! The objective is to forecast electricity prices for the next seven days.

The **data_v1** file contains three columns: time, price and exog. The price corresponds to the electricity price at each hour, which is what you want to predict. The exog corresponds to the wind power forecast, which is the exogenous data that may be useful to make your predictions. 

## Data

At first you only have the **data_v1** file which contains data for the last 5 weeks of 2017. This data should be enough to build a baseline or perhaps even a simple model. Note that the last 168 values of the price are missing in this dataset, because these correspond to the values you are expected to predict. So you have 4 weeks of electricity prices to come up with a methodology to predict the 5th week. We encourage you to submit at least once using this dataset, think of this as your baseline. Check the example submission file to see how you should submit your results - a file with only one column named 'price'.

Then at 11:30 we will release **data_v2** which updates the previous dataset all the way back to 2015. This means you now have years of data to predict that same last week of December. Can you use more complex models to leverage the extra data? 

Some clarifications:
- data_v2 contains the new data as well as the old data, so you only need to read the new dataset, you don’t need to merge with the old one. 
- Again, you are predicting the last week of December 2017, so the test dataset in the portal is the same. The only difference is that with data_v2 you have extra data to train your models.

## Context

A little domain knowledge a day, puts the unknown away. How the electricity pricing works, in an oversimplified manner: the different electricity sources (coal, gas, solar, wind) present different costs, mostly due to their different characteristics like investment and operational costs. The electricity price of a given day depends on how much each source contributes to the overall picture. So, maybe there is an intrinsic temporal pattern that we can explore. And, maybe, having a prediction of how much one of these sources (in our case, wind) is going to play out, can help the model perform better.

## Recommendations

❗Establish a simple baseline against which you can benchmark your models.
❗Improve your models by extracting relevant features from the data and/or tunning hyper-parameters.
❗Hyper-parameter tuning can take a long time, can you make some valid assumptions that limit the search space, making the tuning faster?
❗Remember to visualize your data. Whether to get a sense for the data or to understand why your predictions are not the best, data visualization is a fundamental tool when working with time series.
❗The provided utils.py is merely a tool to help you, feel free to expand it further.
❗Distribute work intelligently across team members: Maybe one is responsible for exploring the data and cleaning the data, the other for reviewing the functions and trying out the ML models and the other for having a go at SARIMAX?
❗You can use any sklearn like model with the time series formulation, you’re not limited to Linear Regression and Gradient Boosting Regressors
❗Remember: More complex models don’t always yield better results.
❗ Enjoy the hackathon and learn as much as you can! 🎉

## Evaluation Criteria

Evaluation Metric - Mean Absolute Error (MAE). 

## Hackathon Rules

- The selection of the teams is random. 
- Instructors will be available to help at any time. The instructors will not help your team solve the challenge, but they will help your team to be on track and answer technical questions that your team might have.
- No more submissions and questions to the instructors shall be done after the end of the challenge.
- Your team will have to prepare a presentation to share your findings with everyone. See the presentation guidelines below. This presentation will be considered in the overall evaluation of your team, so don’t consider it less important than the ML model!
- You can submit your predictions up to five times to evaluate your MAE score. The best will be chosen for the team’s best score.
- The final rank is calculated as:

   FinalRank = 0.5 * MAE_rank + 0.5 * Presentation_rank

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
