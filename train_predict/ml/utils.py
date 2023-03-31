"""
Name: Edgar Gironés
Date: 21.03.2023
Save pickle
"""
import pickle


def save_pickle(filename: str, object_to_pickle):
    """
    Save pickle
    """
    with open(f"./model/{filename}.pkl", "wb") as f:
        pickle.dump(object_to_pickle, f)
