import pickle
import lightgbm as lgb


def prepare_model(saved_model_path):
    model = lgb.LGBMClassifier()
    with open(saved_model_path, "wb") as f:
        pickle.dump(model, f)

    return model


def predict(model, prediction_data):
    prediction = model.predict(prediction_data)[0]
    return prediction
