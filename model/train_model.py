# Script to train machine learning model.
from ml.data import process_data
from sklearn.model_selection import train_test_split
import pandas as pd
# Add the necessary imports for the starter code.

# Add code to load in the data.
df = pd.read_csv("../data/census.csv")

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(df, test_size=0.20)

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
    train, categorical_features=cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    test, categorical_features=cat_features, label="salary", training=True
)
# Train and save a model.
