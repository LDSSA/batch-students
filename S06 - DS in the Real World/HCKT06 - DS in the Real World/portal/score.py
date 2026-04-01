# batch 9 hackathon 6 score - 6 prediction values were provided in each response

import json

from sklearn.metrics import mean_absolute_percentage_error

from portal.capstone.models import DueDatapoint

from collections import Counter

import pandas as pd
import numpy as np


ports_mexico = [2301, 2302, 2303, 2304, 2305, 2307, 2309, 2310, 2401, 2402, 2403,
       2404, 2406, 2408, 2502, 2503, 2504, 2505, 2506, 2507, 2601, 2602,
       2603, 2604, 2606, 2608]
ports_canada = [ 103,  104,  105,  106,  107,  108,  109,  110,  115,  118,  127,
        203,  206,  209,  211,  212,  701,  704,  708,  712,  715,  901,
       3004, 3007, 3009, 3011, 3012, 3013, 3015, 3016, 3017, 3019, 3020,
       3023, 3025, 3103, 3104, 3106, 3301, 3302, 3306, 3308, 3309, 3310,
       3316, 3317, 3318, 3319, 3321, 3322, 3323, 3325, 3401, 3403, 3404,
       3405, 3406, 3407, 3408, 3409, 3410, 3413, 3414, 3415, 3416, 3417,
       3419, 3420, 3421, 3422, 3423, 3424, 3425, 3426, 3430, 3604, 3613,
       3801, 3802, 3803]

ports_moment_4 = [103, 104, 106, 108, 115, 118, 127, 203, 206, 209, 211, 704, 708, 715, 901, 2302, 2303, 2304, 2305, 2307, 2309, 2408, 2502, 2503, 2504, 2505, 2506, 2507, 2602, 2603, 2606, 3004, 3007, 3011, 3012, 3015, 3017, 3019, 3023, 3025, 3103, 3104, 3106, 3301, 3306, 3308, 3316, 3317, 3318, 3319, 3322, 3401, 3403, 3404, 3405, 3408, 3409, 3413, 3414, 3419, 3420, 3423, 3424, 3425, 3430, 3613, 3801, 3803]

ports_moment_1 = [105, 107, 109, 110, 212, 701, 712, 2301, 2310, 2401, 2402, 2403, 2404, 2406, 2604, 3009, 3016, 3020, 3302, 3309, 3310, 3321, 3323, 3325, 3406, 3407, 3410, 3415, 3416, 3417, 3421, 3422, 3604, 3802]


def fairness_score(sensitive_class): # not using this function in this hackathon
    '''
    Computes a fairness score corresponding to the highest difference
     between mse-score among sensitive classes
    :param sensitive_class: dictionary with the following structure
      {
       'sensitive_class_1': {'outcomes': [...], 'predictions': [...]},
       'sensitive_class_2': {'outcomes': [...], 'predictions': [...]},
       ...
      }
    :return: maximum difference between f1-scores in sensitive clasess
    '''
    scores = []
    for s_class in sensitive_class.keys():
        outcomes = sensitive_class[s_class]["outcomes"]
        predictions = sensitive_class[s_class]["predictions"]
        if len(outcomes) > 200:
            scores.append(metrics.mean_squared_error(outcomes, predictions))

    score_diff = 0
    if scores:
        score_diff = (max(scores) - min(scores))/max(scores)

    return score_diff


def score(student_api):
    '''
    Calculates the score of the students' API model
    :param student_api: StudentApi object
    :return: score as a float
    '''

    print("Evaluating... {}".format(student_api.user,student_api.url))
    if len(student_api.url) > 0:
        
        simulator_ids = []
        for simulator in student_api.capstone.simulators.filter(name="cap-moment4").all():
            if simulator.datapoints.exclude(outcome="").count() > 0:
                simulator_ids.append(simulator.id)

        if len(simulator_ids) == 0:
            raise RuntimeError("No simulators with outcomes found.")

        qs = DueDatapoint.objects.filter(
            simulator_id__in=simulator_ids,
            user=student_api.user,
        )
        
        print("QS len: {}".format(len(qs)))

        if len(qs)==0:
            return 0
            
        dict_ports = {} # [port][traffic][mape]
        outcome_all = []
        prediction_all = []
        for ddp in qs:  # loop through each entry in DueDataPoint
            outcome = [int(i) for i in json.loads(ddp.datapoint.outcome).split()]  # this is the real value - has to be called outcome in the moments files
            data = json.loads(ddp.datapoint.data)
            port_code = data['port_code']
            traffic = data['traffic']
            if ddp.response_status != 200:  # Missing or bad response
                prediction = [0, 0, 0, 0, 0, 0]
        
            else:
                try:
                    prediction_str = json.loads(ddp.response_content)['prediction']
                except (json.JSONDecodeError, KeyError):
                    prediction = "0 0 0 0 0 0"
                try:
                    prediction = [int(i) for i in prediction_str.split()] 
                except AttributeError:  # handle missing data
                    prediction = [0,0,0,0,0,0]
            while len(prediction)<6:
                prediction.append(0)
            mape = mean_absolute_percentage_error(outcome,prediction)
            if mape<10: # remove weirdly large mapes
                outcome_all.append(outcome)
                prediction_all.append(prediction)
            else:
                mape = 1   

            if port_code not in dict_ports.keys():
                dict_ports[port_code]={}
            dict_ports[port_code][traffic]=mape
        
        # mean mape over everything
        score = mean_absolute_percentage_error(outcome_all,prediction_all)
        
        n_missed = 0
        
        fairness_penalty = 0.0
        # penalize items where min and max mape is 1
        # difference between traffic for each port
        for p in dict_ports.keys():
            max_mape = np.max([dict_ports[p]['people'], dict_ports[p]['vehicles'], dict_ports[p]['containers']])
            min_mape = np.min([dict_ports[p]['people'], dict_ports[p]['vehicles'], dict_ports[p]['containers']])
            port_diff = max_mape-min_mape
            if (min_mape==1) and (max_mape==1):
                fairness_penalty += 1
                n_missed +=1
            elif port_diff>0.15:
                fairness_penalty += port_diff

        # difference for people traffic at borders
        mape_mexico = []
        mape_canada = []
        for p in dict_ports.keys():
            if p in ports_mexico:
                mape_mexico.append(dict_ports[p]['people'])
            if p in ports_canada:
                mape_canada.append(dict_ports[p]['people'])    
        diff_mexico = np.max(mape_mexico) - np.min(mape_mexico)
        diff_canada = np.max(mape_canada) - np.min(mape_canada)
        if (np.max(mape_mexico)==1) and (np.min(mape_mexico)==1):
            fairness_penalty += 1
            n_missed +=1
        elif diff_mexico > 0.15:
            fairness_penalty += diff_mexico
        if (np.max(mape_canada)==1) and (np.min(mape_canada)==1):
            fairness_penalty += 1
            n_missed +=1
        elif diff_canada > 0.15:
            fairness_penalty += diff_canada

        
        final_score =  score * (1 + fairness_penalty/10)

        print("mean MAPE: {}".format(score))
        print("Fairness penalty: {}".format(fairness_penalty))
        print("Missed: {}".format(n_missed))
        print("Final score: {}".format(final_score))
    
        return max(0, score)
    else:
        return 0

