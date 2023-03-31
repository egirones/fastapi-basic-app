from fastapi.testclient import TestClient
from train_predict.utils import preprocess_data
from train_predict.predict import convert_to_numpy
from main import app

client = TestClient(app)


def test_column_conversion(data_dict):
    new_column_names = preprocess_data(data_dict)
    for c in new_column_names:
        assert "_" not in c


def test_convert_numpy(data_dict):
    np_array = convert_to_numpy(preprocess_data(data_dict))
    assert np_array.shape == (1, 108)


def test_api_get_root():
    r = client.get("/")
    assert r.json() ==  {"message":"Hello World"}
    assert r.status_code == 200
