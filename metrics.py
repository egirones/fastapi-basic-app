"""
Name: Edgar Gironés
Date: 21.03.2023
Module to test for slices data
"""
import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
from train_predict.train_model import cat_features
from train_predict.ml.data import process_data
from train_predict.ml.model import compute_model_metrics


def compute_metrics_per_slice(feature="education"):
    with open("./model/lb.pkl", 'rb') as pickle_file:
        lb = pickle.load(pickle_file)
    with open("./model/encoder.pkl", 'rb') as pickle_file:
        encoder = pickle.load(pickle_file)
    with open("./model/model.pkl", 'rb') as pickle_file:
        model = pickle.load(pickle_file)

    df = pd.read_csv("./data/census.csv")

    # remove column spaces
    df.columns = df.columns.str.replace(' ', '')

    train, test = train_test_split(df, test_size=0.20, random_state=42)

    slices = test[feature].unique()
    results = [f"Test for {feature}\n"]

    for s in slices:
        slice_test = test[test[feature] == s]

        X_test, y_test, encoder, lb = process_data(
            slice_test,
            categorical_features=cat_features,
            label="salary",
            training=False,
            encoder=encoder,
            label_b=lb)

        y_pred = model.predict(X_test)
        met = compute_model_metrics(y_test, y_pred)
        results.append(
            f"{s}: precision {met[0]}, recall {met[1]}. fbeta {met[2]}\n"
        )

    for result in results:
        print(result)

    with open("./metrics/slice_output.txt", "w") as f:
        f.writelines(results)


compute_metrics_per_slice()
