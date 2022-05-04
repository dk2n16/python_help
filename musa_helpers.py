"""
Module of functions to deal with Python issues Musa has raised
"""
from pathlib import Path

import numpy as np
import pandas as pd

def prep_df(csv):
    """Returns datafame with headers set to row 6 (cols:[0,1,2]) and row 5 (cols: [3:])

    Parameters:
    -----------
    csv : str/Path
        Path to csv to open and prepare

    Returns:
    --------
    df : pd.DataFrame
        Dataframe with correct headers set and appropriate rows retained
    """
    df = pd.read_csv(csv, header=5, usecols=range(0, 13))
    df.rename(columns={'Unnamed: 0': df.iloc[0]['Unnamed: 0'],
                       'Unnamed: 1': df.iloc[0]['Unnamed: 1'],
                       'Unnamed: 2': df.iloc[0]['Unnamed: 2']}, inplace=True)
    df.dropna(inplace=True)
    df = df[df["Geographical Designation"] == 'Local Authority']
    cols = [x for x in df.columns if x.startswith('20')]  # Numeric columns (years)
    df[cols] = df[cols].replace('x', np.nan)
    df[cols] = df[cols].astype(np.float32)
    return df


if __name__ == "__main__":
    # Example of use
    BASE_DIR = Path(__file__).resolve().parent.joinpath('data/MUSA_TABLES')
    csvs = ['WorthwhileMeans.csv', 'LifeSatisfactionMeans.csv']
    for csv in csvs:
        df = prep_df(BASE_DIR.joinpath(csv))
        print(f'DATAFRAME FOR {csv}-------------->')
        print(df.head())