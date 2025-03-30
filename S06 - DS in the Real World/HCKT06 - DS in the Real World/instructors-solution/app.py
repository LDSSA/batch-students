import os
import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request
from peewee import (
    Model, BooleanField, CharField,
    TextField
)
from playhouse.shortcuts import model_to_dict
from playhouse.db_url import connect
import logging


class CustomRailwayLogFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "time": self.formatTime(record),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log_record)
    

def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO) # this should be just "logger.setLevel(logging.INFO)" but markdown is interpreting it wrong here...
    handler = logging.StreamHandler()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    formatter = CustomRailwayLogFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = get_logger()

DB = connect(os.environ.get('DATABASE_URL') or 'sqlite:///predictions.db')

class Prediction(Model):
    observation_id = CharField(primary_key=True, max_length=50)
    observation = TextField()
    pred_class = BooleanField()
    true_class = BooleanField(null=True)

    class Meta:
        database = DB


DB.create_tables([Prediction], safe=True)

with open('columns.json') as fh:
    columns = json.load(fh)

pipeline = joblib.load('pipeline.pickle')

app = Flask(__name__)


def process_observation(observation):
    logger.info("Processing observation, %s", observation)
    # A lot of processing
    return observation


@app.route('/predict', methods=['POST'])
def predict():
    obs_dict = request.get_json()
    logger.info('Observation: %s', obs_dict)
    _id = obs_dict['observation_id']
    observation = obs_dict

    if not _id:
        logger.warning('Returning error: no id provided')
        return jsonify({'error': 'observation_id is required'}), 400
    if Prediction.select().where(Prediction.observation_id == _id).exists():
        prediction = Prediction.get(Prediction.observation_id == _id)

        # Update the prediction
        prediction.observation = str(observation)
        prediction.save()

        logger.warning('Returning error: already exists id %s', _id)
        return jsonify({'error': 'observation_id already exists'}), 400

    try:
        obs = pd.DataFrame([observation], columns=columns)
    except ValueError as e:
        logger.error('Returning error: %s', str(e), exc_info=True)
        default_response = {'observation_id': _id, 'label': False}
        return jsonify(default_response), 200
    
    label = bool(pipeline.predict(obs))
    response = {'observation_id': _id, 'label': label}
    p = Prediction(
        observation_id=_id,
        observation=request.data,
        pred_class=label,
    )
    p.save()
    logger.info('Saved: %s', model_to_dict(p))
    logger.info('Prediction: %s', response)

    return jsonify(response)


@app.route('/update', methods=['POST'])
def update():
    obs = request.get_json()
    logger.info('Observation:', obs)
    _id = obs['observation_id']
    label = obs['label']

    if not _id:
        logger.warning('Returning error: no id provided')
        return jsonify({'error': 'observation_id is required'}), 400
    if not Prediction.select().where(Prediction.observation_id == _id).exists():
        logger.warning(f'Returning error: id {_id} does not exist in the database')
        return jsonify({'error': 'observation_id does not exist'}), 400
    
    p = Prediction.get(Prediction.observation_id == _id)
    p.true_class = label
    p.save()
    logger.info('Updated: %s', model_to_dict(p))

    response = {'observation_id': _id, 'label': label}
    return jsonify(response)



@app.route('/list-db-contents')
def list_db_contents():
    return jsonify([
        model_to_dict(obs) for obs in Prediction.select()
    ])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
