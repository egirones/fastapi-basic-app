"""
Name: Edgar Gironés
Date: 21.03.2023
Package to preprocess data
"""
import pandas as pd


def preprocess_data(input_data):
    """
    Input: Receives input data
    Output: Transforms data for prediction
    """
    dict_fields = dict(input_data)
    item = pd.DataFrame(dict_fields, index=[0])
    item.columns = item.columns.str.replace('_', '-')
    return item
