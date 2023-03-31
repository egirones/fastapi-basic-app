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