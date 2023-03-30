import pickle

def save_pickle(filename:str, object_to_pickle):
    with open(f"../model/{filename}.pkl", "wb") as f:
        pickle.dump(object_to_pickle, f) 