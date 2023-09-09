import spaces


# save the iris classification model as a pickle file
# model_pkl_file = "finalized_model_accuracy.sav"


def predict_exercise(config):
    # load model from pickle file

    # if config['type'][0]==1:
    #     model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_accuracy.sav")
    # else:
    #     model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_accuracy1.sav")

    if 0 < config['type'][0] <= 10:
        if config['type'][0] == 1:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_accuracy.sav")

        elif config['type'][0] == 2:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_agility.sav")

        elif config['type'][0] == 3:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_balance.sav")

        elif config['type'][0] == 4:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_coordination.sav")

        elif config['type'][0] == 5:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_endurance.sav")

        elif config['type'][0] == 6:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_flexibility.sav")

        elif config['type'][0] == 7:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_power.sav")

        elif config['type'][0] == 8:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_speed.sav")

        elif config['type'][0] == 9:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_stamina.sav")

        elif config['type'][0] == 10:
            model = spaces.download_file("ml-trained-models", "nyc3", "finalized_model_strength.sav")

        # print(model)
        # print(type(config['values']))
        # print("hamzaabbsi")
        # print(config['type'])
        # print(type(config['type']))
        # print(config['type'][0])
        # print("hamza")
        # print(type([1, 2, 3]))

        values = config['values']
        # print(model.predict([[1,2,3]]))

        predicted_value = model.predict([values])
        print(predicted_value)

        tag = predicted_value[0]
        code = 0
        message = "success"
        return code,message,tag

    else:
        print("Is that even a thing?")
        tag = "Wrong Values Provided"
        code = 1
        message = "failure"
        return code, message, tag

    # 2 finalized_model_agility
    # 3 finalized_model_balance
    # 4 finalized_model_coordination
    # 5 finalized_model_endurance
    # 6 finalized_model_flexibility
    # 7 finalized_model_power
    # 8 finalized_model_speed
    # 9 finalized_model_stamina
    # 10 finalized_model_strength

    # config = {
    #     'type': [1],  # 1- Male, 2- Female
    #     'values': [1, 2, 3],
    # }


