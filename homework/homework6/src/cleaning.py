# src/cleaning.py
from __future__ import annotations
from typing import Iterable, Literal
import pandas as pd
import numpy as np

def _ensure_list(cols: Iterable[str] | None, df: pd.DataFrame) -> list[str]:
    if cols is None:
        return list(df.columns)
    return list(cols)

def fill_missing_median(df: pd.DataFrame, cols: Iterable[str] | None = None) -> pd.DataFrame:
    """
    Fill NaNs in the given numeric columns with their column-wise median.
    Non-numeric columns in `cols` are ignored safely.

    Parameters
    ----------
    df : DataFrame
    cols : list of column names (or None to apply to all columns)

    Returns
    -------
    DataFrame (copy)
    """
    out = df.copy()
    cols = _ensure_list(cols, out)

    for c in cols:
        if c not in out.columns:
            continue
        # only attempt if column is numeric-like
        if pd.api.types.is_numeric_dtype(out[c]):
            med = out[c].median(skipna=True)
            # if all values are NaN, median is NaN; leave column as-is
            if pd.notna(med):
                out[c] = out[c].fillna(med)
    return out


def drop_missing(
    df: pd.DataFrame,
    threshold: float = 0.5,
    axis: Literal["row", "column"] = "row",
) -> pd.DataFrame:
    """
    Drop rows (default) or columns with a fraction of missing values > threshold.

    Examples
    --------
    drop_missing(df, 0.5)         # drop rows with >50% NaN
    drop_missing(df, 0.4, "column")  # drop columns with >40% NaN
    """
    if not (0.0 <= threshold <= 1.0):
        raise ValueError("threshold must be in [0, 1]")

    out = df.copy()
    if axis == "row":
        # count NaNs per row and divide by number of columns
        frac_missing = out.isna().sum(axis=1) / out.shape[1]
        return out.loc[frac_missing <= threshold].reset_index(drop=True)
    elif axis == "column":
        frac_missing = out.isna().sum(axis=0) / out.shape[0]
        return out.loc[:, frac_missing <= threshold]
    else:
        raise ValueError("axis must be 'row' or 'column'")


def normalize_data(
    df: pd.DataFrame,
    cols: Iterable[str] | None = None,
    method: Literal["minmax", "zscore"] = "minmax",
) -> pd.DataFrame:
    """
    Normalize the selected numeric columns.

    method='minmax'  -> (x - min) / (max - min)  scaled to [0,1]
    method='zscore'  -> (x - mean) / std

    Columns that are non-numeric are skipped.
    Constant columns are left as 0.0 for minmax (or 0.0 for zscore).

    Returns a copy.
    """
    out = df.copy()
    cols = _ensure_list(cols, out)

    for c in cols:
        if c not in out.columns or not pd.api.types.is_numeric_dtype(out[c]):
            continue

        s = out[c].astype(float)  # ensure float for division

        if method == "minmax":
            mn = s.min(skipna=True)
            mx = s.max(skipna=True)
            rng = mx - mn
            if pd.isna(mn) or pd.isna(mx):
                # all NaN; skip
                continue
            if rng == 0:
                out[c] = s.where(s.isna(), 0.0)  # constant column -> 0.0
            else:
                out[c] = (s - mn) / rng
        elif method == "zscore":
            mu = s.mean(skipna=True)
            sd = s.std(ddof=0, skipna=True)
            if pd.isna(mu) or pd.isna(sd) or sd == 0:
                out[c] = s.where(s.isna(), 0.0)
            else:
                out[c] = (s - mu) / sd
        else:
            raise ValueError("method must be 'minmax' or 'zscore'")
    return out
