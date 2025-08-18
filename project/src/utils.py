# src/utils.py

import pandas as pd

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize DataFrame column names:
    - Strip leading/trailing spaces
    - Convert to lowercase
    - Replace spaces with underscores

    Args:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: DataFrame with cleaned column names.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def parse_dates(df: pd.DataFrame, date_cols: list[str]) -> pd.DataFrame:
    """
    Parse specified columns into datetime objects.
    Invalid values are set to NaT instead of raising errors.

    Args:
        df (pd.DataFrame): Input DataFrame.
        date_cols (list[str]): List of column names to parse as dates.

    Returns:
        pd.DataFrame: DataFrame with parsed datetime columns.
    """
    df = df.copy()
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df
