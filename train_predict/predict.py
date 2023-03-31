import pickle
from train_predict.train_model import process_data, cat_features
import numpy as np


def inference(model, X):
    """ Run model inferences and return the predictions.
    Inputs
    ------
    model : trained model
        Trained machine learning model.
    X : pandasD
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    with open("./model/lb.pkl", 'rb') as pickle_file:
        lb = pickle.load(pickle_file)
    with open("./model/encoder.pkl", 'rb') as pickle_file:
        encoder = pickle.load(pickle_file)
    
    X_categorical = X[cat_features].values
    X_continuous = X.drop(*[cat_features], axis=1)

    X_categorical = encoder.transform(X_categorical)

    X = np.concatenate([X_continuous, X_categorical], axis=1)
    
    prediction = model.predict(X)

    return {"prediction": lb.classes_[prediction][0]}