"""
cleaning.py

All data cleaning functions are performed here.
"""


from pathlib import Path
from shared.utils import io

DATA_PATH = Path(".../data/raw/Insurance_complaints__All_data_20251211.csv")

df = io.load_csv(DATA_PATH)