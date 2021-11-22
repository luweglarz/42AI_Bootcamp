import pandas as pd

class FileLoader:
    @staticmethod
    def load(path):
        df = pd.read_csv(path)
        print("Loading dataset of dimensions:", df.shape)
        return df
    @staticmethod
    def display(df, n):
        print(df.head(n))
