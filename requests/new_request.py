import requests


url = "https://prediction-mntl.onrender.com/predict/"
to_predict = {
    "age": 40,
    "workclass": "Private",
    "fnlgt": 165231,
    "education": "Doctorate",
    "education_num": 9,
    "marital_status": "Never-married",
    "occupation":  "Exec-managerial",
    "relationship": "Husband",
    "race": "Asian",
    "sex": "Male",
    "capital_gain": 100,
    "capital_loss": 0,
    "hours_per_week": 36,
    "native_country": "United-States"
    }

x = requests.post(url, json=to_predict)

print(x.status_code, x.content)
