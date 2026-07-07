import pandas as pd
def dataset(x):
    dataset=pd.read_csv(f"dataset/{x}.csv")
    return dataset
