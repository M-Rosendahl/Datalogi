"""
io.py

Common input/output helper functions for loading and saving different file types.
"""

import pandas as pd
import json
import pickle
from pathlib import Path


# -------------------------------
# CSV
# -------------------------------

def load_csv(path):
    """
    Load a CSV file into a pandas DataFrame.
    """
    return pd.read_csv(Path(path))


def save_csv(df, path):
    """
    Save a pandas DataFrame to a CSV file.
    Creates the directory if it does not already exist.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


# -------------------------------
# Excel
# -------------------------------

def load_excel(path, sheet_name=0):
    """
    Load an Excel file (.xlsx or .xls) into a DataFrame.
    'sheet_name' can be a string (tab name) or an index.
    """
    return pd.read_excel(Path(path), sheet_name=sheet_name)


def save_excel(df, path, sheet_name="Sheet1"):
    """
    Save a DataFrame to an Excel file.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(path, index=False, sheet_name=sheet_name)


# -------------------------------
# JSON
# -------------------------------

def load_json(path):
    """
    Load a JSON file into a Python dictionary or list.
    """
    with open(Path(path), "r") as f:
        return json.load(f)


def save_json(obj, path, indent=2):
    """
    Save a Python dictionary or list to a JSON file.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(obj, f, indent=indent)


# -------------------------------
# Parquet (efficient columnar format)
# -------------------------------

def load_parquet(path):
    """
    Load a Parquet file into a DataFrame.
    Parquet loads much faster than CSV for large datasets.
    """
    return pd.read_parquet(Path(path))


def save_parquet(df, path):
    """
    Save a DataFrame to a Parquet file.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


# -------------------------------
# Pickle (fast Python object serialize/deserialize)
# -------------------------------

def load_pickle(path):
    """
    Load a Python object (DataFrame, dict, model, etc.) from a .pkl file.
    """
    with open(Path(path), "rb") as f:
        return pickle.load(f)


def save_pickle(obj, path):
    """
    Save a Python object to a .pkl file.
    Useful for caching models or expensive computations.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(obj, f)


# -------------------------------
# Raw Text Files
# -------------------------------

def load_text(path):
    """
    Load a plain text file and return the file contents as a string.
    """
    with open(Path(path), "r") as f:
        return f.read()


def save_text(text, path):
    """
    Save a string to a plain text file.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(text)