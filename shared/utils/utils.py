"""
utils.py

General helper functions that are useful across multiple data-science projects.
These functions do not depend on any specific dataset.
"""

import time
import pandas as pd
from IPython.display import display


# --------------------------------------------------
# Timer utilities
# --------------------------------------------------

def timer(func, *args, **kwargs):
    """
    Measure how long a function takes to run. Returns (result, elapsed_time).
    """
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return result, end - start


def print_time(label, seconds):
    """
    Print timing results in a friendly format.
    """
    print(f"{label}: {seconds:.4f} seconds")


# --------------------------------------------------
# DataFrame preview helpers
# --------------------------------------------------

def preview(df, n=5):
    """
    Display the first n rows of a DataFrame.
    """
    display(df.head(n))


def info(df):
    """
    Show basic information about a DataFrame in a readable format.
    """
    print("Shape:", df.shape)
    print("\nColumn types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isnull().sum())


# --------------------------------------------------
# Column cleaning helpers
# --------------------------------------------------

def strip_whitespace(df):
    """
    Remove leading/trailing whitespace from all string columns in the DataFrame.
    """
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].str.strip()
    return df


def lowercase_columns(df):
    """
    Convert all column names to lowercase.
    """
    df.columns = [col.lower() for col in df.columns]
    return df


# --------------------------------------------------
# Simple error-safe extraction
# --------------------------------------------------

def safe_get(dictionary, key, default=None):
    """
    Return dictionary[key] if it exists, otherwise return a default value.
    """
    return dictionary[key] if key in dictionary else default