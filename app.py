import json
import os

from flask import Flask, request, jsonify

import pandas as pd
from fbprophet import Prophet

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'rasprophet v0.1'

@app.route('/', methods=['POST'])
def calc():
    try:
        data = json.loads(request.data)
    except Exception:
        return jsonify(dict(message="invalid data format")), 400
    # try:
    #     key = data['key']
    # except KeyError:
    #     return jsonify(dict(message='no key submitted')), 400
    # if key != os.environ['secret_key']:
    #     return jsonify(dict(message='invalid key')), 400
    try:
        ds = data['ds']
        y = data['y']
        p = data['p']
    except KeyError:
        return jsonify(dict(message='invalid input')), 400

    periods = data.get('periods', p)
    m = Prophet(
            yearly_seasonality=True, 
            # changepoints=['2020-06-12','2020-12-24', '2021-06-12']
        )
    df = pd.DataFrame(dict(ds=ds, y=y))
    m.fit(df)
    f = m.make_future_dataframe(periods=periods)
    forecast = m.predict(f)
    # only send back new dates
    f_df = forecast[forecast['ds'] > df['ds'].max()].to_dict()
    return jsonify(f_df)
