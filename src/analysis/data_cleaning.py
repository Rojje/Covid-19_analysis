
import pandas as pd 
def drop_columns(df, columns):
    
    return df.drop(columns=columns, errors="ignore")  