"""
Name: Edgar Gironés
Date: 21.03.2023
Module to train data
"""
# Script to train machine learning model.
from sklearn.model_selection import train_test_split
import pandas as pd
from train_predict.ml.data import process_data
from train_predict.ml.model import train_model
from train_predict.ml.utils import save_pickle

# Add the necessary imports for the starter code.

# Add code to load in the data.
df = pd.read_csv("./data/census.csv")

# remove column spaces
df.columns = df.columns.str.replace(' ', '')

# Optional enhancement, use K-fold cross validation instead of a
# train-test split.
train, test = train_test_split(df, test_size=0.20, random_state=42)

cat_features = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

X_train, y_train, encoder, lb = process_data(
    train,
    categorical_features=cat_features,
    label="salary",
    training=True
)

# Process the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    test,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    label_b=lb
)

model_trained = train_model(X_train, y_train)

pred = model_trained.predict(X_test)


save_pickle("model", model_trained)
save_pickle("encoder", encoder)
save_pickle("lb", lb)
