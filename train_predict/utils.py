import pickle
import pandas as pd
from train_predict.ml.data import process_data
from train_predict.train_model import cat_features

with open("./model/encoder.pkl", 'rb') as pickle_file:
    encoder = pickle.load(pickle_file)


def predict(item_to_predict):
    process_data(item_to_predict, categorical_features=cat_features,)

def preprocess_data(input):
    dict_fields = dict(input)
    item = pd.DataFrame(dict_fields, index=[0])
    item.columns = item.columns.str.replace('_', '-')
    return item