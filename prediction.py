import spaces


# save the iris classification model as a pickle file
#model_pkl_file = "finalized_model_accuracy.sav"


def predict_exercise(config):
    # load model from pickle file
    model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_accuracy1.sav")

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
