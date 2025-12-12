"""
plotting.py

General plotting helper functions used across multiple data-science projects.
These functions provide simple, reusable visualizations that work with any dataset.
"""

import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# Basic Plot Style
# --------------------------------------------------

def style_default():
    """
    Apply a basic plot style for all charts. Makes plots look cleaner and more consistent.
    """
    sns.set_style("darkgrid")
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["axes.titlesize"] = 14
    plt.rcParams["axes.labelsize"] = 12


# --------------------------------------------------
# Histogram
# --------------------------------------------------

def plot_hist(df, column, bins=30, title=None):
    """
    Plot a histogram for a single numeric column.
    """
    plt.figure()
    sns.histplot(df[column], bins=bins, kde=False)
    plt.title(title if title else f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()


# --------------------------------------------------
# Histogram with KDE
# --------------------------------------------------

def plot_hist_kde(df, column, bins=30, title=None):
    """
    Plot a histogram with a KDE (smooth curve) overlay. Good for visualizing the distribution shape.
    """
    plt.figure()
    sns.histplot(df[column], bins=bins, kde=True)
    plt.title(title if title else f"{column} Distribution (KDE)")
    plt.xlabel(column)
    plt.ylabel("Density")
    plt.show()


# --------------------------------------------------
# Scatter Plot
# --------------------------------------------------

def plot_scatter(df, x, y, title=None):
    """
    Plot a scatter plot for two numeric columns.
    Useful for checking relationships between variables.
    """
    plt.figure()
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(title if title else f"{y} vs. {x}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()


# --------------------------------------------------
# Box Plot
# --------------------------------------------------

def plot_box(df, column, title=None):
    """
    Plot a box plot for a numeric column.
    Useful for checking outliers.
    """
    plt.figure()
    sns.boxplot(x=df[column])
    plt.title(title if title else f"Box Plot of {column}")
    plt.xlabel(column)
    plt.show()


# --------------------------------------------------
# Bar Chart
# --------------------------------------------------

def plot_bar(df, column, title=None):
    """
    Plot a bar chart for the counts of a categorical column.
    """
    plt.figure()
    df[column].value_counts().plot(kind="bar")
    plt.title(title if title else f"Counts of {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.show()