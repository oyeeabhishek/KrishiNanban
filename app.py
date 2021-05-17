# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import requests
import config
import pickle

# Loading crop recommendation model

crop_recommendation_model_path = 'D:\\New-Model\\RF_Model_pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))












app = Flask(__name__)

# render crop recommendation form page


@ app.route('/')
def crop_recommend():
    title = 'Harvestify - Crop Recommendation'
    return render_template('crop.html', title=title)

# render crop recommendation result page


@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Harvestify - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # state = request.form.get("stt")
        
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        return render_template('crop-result.html', prediction=final_prediction, title=title)

        
        
        # ===============================================================================================
if __name__ == '__main__':
    app.run(debug=True)
