# src Directory

The src/ folder contains Python code that is reused across the project. 
Notebooks are mainly for exploring data and running analysis, while src/ 
holds the functions and logic that support that work.

## Purpose of this folder

1. Reusable code  
   Functions that are used more than once are placed here. Examples include:
   - data cleaning
   - feature creation
   - model building
   - plotting helpers
   - small utility functions

   These modules can then be imported inside notebooks, for example:
   from src.cleaning import clean_data

2. Cleaner notebooks  
   Keeping functions in .py files helps notebooks stay organized and easier to read.

3. Easier updates  
   When shared code is stored in src/, changes only need to be made in one place.

## Common layout

src/
  cleaning.py
  features.py
  model.py
  visualize.py
  utils.py

The src/ folder contains the main code used throughout the project.
