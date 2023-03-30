# Script to train machine learning model.
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
from ml.data import process_data
from ml.model import train_model, compute_model_metrics
from ml.utils import save_pickle
# Add the necessary imports for the starter code.

# Add code to load in the data.
df = pd.read_csv("../data/census.csv")

# remove column spaces
df.columns = df.columns.str.replace(' ', '')


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
    train, 
    categorical_features=cat_features, 
    label="salary", 
    training=True
)

# Proces the test data with the process_data function.
X_test, y_test, encoder, lb = process_data(
    test, 
    categorical_features=cat_features, 
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb
)

model_trained = train_model(X_train, y_train)

pred = model_trained.predict(X_test)

save_pickle("model", model_trained)
save_pickle("encoder", encoder)
save_pickle("lb", lb)
# Train and save a model

print(compute_model_metrics(y_test, pred))