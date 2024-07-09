import pandas as pd

def load_csv(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df.dropna(inplace=True)
    df['col1'] = df['col1'].apply(lambda x: x.strip() if isinstance(x, str) else x)
    return df

def transform_data(df):
    df['col_sum'] = df['col1'] + df['col2']
    return df