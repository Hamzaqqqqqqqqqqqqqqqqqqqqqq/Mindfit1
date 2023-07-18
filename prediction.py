import pickle
import pandas as pd
import json

import pickle

# save the iris classification model as a pickle file
model_pkl_file = "finalized_model_accuracy.sav"


def predict_exercise(config):
    # load model from pickle file
    with open(model_pkl_file, 'rb') as file:
        model = pickle.load(file)

    config = {
        'type': [1],  # 1- Male, 2- Female
        'values': [1, 2, 3],
    }

    print(type(config['values']))
    print(type([1, 2, 3]))

    values = config['values']
    # print(model.predict([[1,2,3]]))

    predicted_value = model.predict([values])
    print(predicted_value)
    return predicted_value[0]

def predict_mpg(config):
    ##loading the model from the saved file
    pkl_filename = "model.pkl"
    with open(pkl_filename, 'rb') as f_in:
        model = pickle.load(f_in)

    if type(config) == dict:
        df = pd.DataFrame(config)
    else:
        df = config

    y_pred = model.predict(df)

    if y_pred == 0:
        return 'Extremely Weak'
    elif y_pred == 1:
        return 'Weak'
    elif y_pred == 2:
        return 'Normal'
    elif y_pred == 3:
        return 'Overweight'
    elif y_pred == 4:
        return 'Obesity'
    elif y_pred == 5:
        return 'Extreme Obesity'