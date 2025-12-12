"""
features.py

Reusable feature engineering helpers for data-science projects.
These functions are meant to be generic and work with many different datasets.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder


# --------------------------------------------------
# Scaling numeric columns
# --------------------------------------------------

def scale_numeric(df, columns):
    """
    Scale numeric columns using StandardScaler.

    Returns:
        scaled_df: DataFrame with scaled columns
        scaler: fitted StandardScaler object
    """
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df[columns])

    scaled_df = df.copy()
    scaled_df[columns] = scaled_values
    return scaled_df, scaler


def apply_scaler(df, columns, scaler):
    """
    Apply a previously fitted StandardScaler to new data.
    Useful when train and test sets must use the same scaling.
    """
    scaled_df = df.copy()
    scaled_df[columns] = scaler.transform(df[columns])
    return scaled_df


# --------------------------------------------------
# One-hot encoding for categorical columns
# --------------------------------------------------

def oh_encode(df, columns):
    """
    One-hot encode categorical columns using pandas.get_dummies.

    Returns:
        encoded_df: DataFrame with one-hot encoded columns
    """
    encoded_df = pd.get_dummies(df, columns=columns, drop_first=False)
    return encoded_df


# --------------------------------------------------
# Date/time features
# --------------------------------------------------

def add_datetime_parts(df, column, prefix=None):
    """
    Add common datetime features (year, month, day, weekday) based on a datetime column.

    Example:
        add_datetime_parts(df, "timestamp", prefix="ts")
        -> columns: ts_year, ts_month, ts_day, ts_weekday
    """
    dt = pd.to_datetime(df[column])
    pre = prefix if prefix is not None else column

    df = df.copy()
    df[f"{pre}_year"] = dt.dt.year
    df[f"{pre}_month"] = dt.dt.month
    df[f"{pre}_day"] = dt.dt.day
    df[f"{pre}_weekday"] = dt.dt.weekday
    return df


# --------------------------------------------------
# Interaction features
# --------------------------------------------------

def add_ratio(df, numerator, denominator, new_col_name=None):
    """
    Add a ratio feature: numerator / denominator.

    If denominator is zero, result is set to NaN.
    """
    df = df.copy()
    name = new_col_name if new_col_name is not None else f"{numerator}_over_{denominator}"
    df[name] = df[denominator].replace(0, pd.NA)
    df[name] = df[numerator] / df[name]
    return df


def add_product(df, col1, col2, new_col_name=None):
    """
    Add a feature equal to the product of two numeric columns.
    """
    df = df.copy()
    name = new_col_name if new_col_name is not None else f"{col1}_times_{col2}"
    df[name] = df[col1] * df[col2]
    return df