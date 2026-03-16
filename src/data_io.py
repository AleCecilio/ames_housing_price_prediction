from pathlib import Path
import pandas as pd

DATA_RAW = Path("data/raw")
DATA_PROCESSED = Path("data/processed")

def load_raw(filename):
    path = DATA_RAW / filename
    return pd.read_csv(path)

def load_processed(filename):
    path = DATA_PROCESSED / filename
    return pd.read_csv(path)

def save_processed(df, filename):
    path = DATA_PROCESSED / filename
    df.to_csv(path, index=False)