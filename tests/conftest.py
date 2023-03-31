import pytest


@pytest.fixture
def data_dict():
    return {
        "age": 1,
        "workclass": "something",
        "fnlgt": "something",
        "education": "something",
        "education_num": 0,
        "marital_status": "something",
        "occupation": "something",
        "relationship": "something",
        "race": "something",
        "sex": "something",
        "capital_gain": 0,
        "capital_loss": 0,
        "hours_per_week": 0,
        "native_country": "something"
    }


@pytest.fixture
def above_50():
    return {
        "age": 40,
        "workclass": "Private",
        "fnlgt": 165231,
        "education": "Doctorate",
        "education_num": 9,
        "marital_status": "Never-married",
        "occupation":  "Exec-managerial",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "capital_gain": 10000,
        "capital_loss": 0,
        "hours_per_week": 36,
        "native_country": "United-States"
    }


@pytest.fixture
def below_50():
    return {
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
