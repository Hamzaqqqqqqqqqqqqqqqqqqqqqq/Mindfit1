from flask import Flask, request, redirect
from flask_restful import Resource, Api
from flask_cors import CORS
import os

import pickle

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class Test(Resource):
    def get(self):
        return 'Welcome to, Test App API!'

    def post(self):
        try:
            value = request.get_json()
            if(value):
                return {'Post Values': value}, 201

            return {"error":"Invalid format."}

        except Exception as error:
            return {'error': error}

class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            data = request.get_json()
            print(os.getcwd())
            print("#############################")
            print(data)
            predict = prediction1.predict_exercise(data)
            predictOutput = predict
            return {'predict':predictOutput}

        except Exception as error:
            return {'error': error}

class prediction1():
    # save the iris classification model as a pickle file

    def predict_exercise(config):
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(config)
        model_pkl_file = "https://trainedmodels.nyc3.cdn.digitaloceanspaces.com/finalized_model_accuracy.sav"
        
        # load model from pickle file
        with open(model_pkl_file, 'rb') as file:
            model = pickle.load(file)

        # config = {
        #     'type': [1],  # 1- Male, 2- Female
        #     'values': [1, 2, 3],
        # }

        print(type(config['values']))
        print(type([1, 2, 3]))

        values = config['values']
        # print(model.predict([[1,2,3]]))

        predicted_value = model.predict([values])
        print(predicted_value)
        return predicted_value[0]

api.add_resource(Test,'/')
api.add_resource(GetPredictionOutput,'/getPredictionOutput')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)
