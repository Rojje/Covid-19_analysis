import pandas as pd

def show_display_fuction(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df



