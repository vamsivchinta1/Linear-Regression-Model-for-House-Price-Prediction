from datetime import datetime
import pandas as pd
import numpy as np

class powertools:
    @staticmethod
    def load_df(url):
        try:
            df = pd.read_csv(url)
            return df
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return None