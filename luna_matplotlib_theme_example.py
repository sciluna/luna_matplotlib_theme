#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["requests>=2.32", "pandas>=2.2", "matplotlib>=3.10"]
# ///

import requests
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import StringIO

from luna_matplotlib_theme import apply_luna_theme

# (Optional) Setup matplotlib Backend
# Use a backend that doesn't require a GUI
matplotlib.use("Agg")

# Download Dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv"
response = requests.get(url)
response.raise_for_status()
csv_text = response.text

# Load Data with Pandas
df = pd.read_csv(StringIO(csv_text))

# Compute Sepal Length Means per Species
means_dict = df.groupby("species")["sepal_length"].mean().to_dict()

# Plot Bar Chart and Save to PDF
species = list(means_dict.keys())
means = list(means_dict.values())

apply_luna_theme()

plt.figure(figsize=(6, 4))
plt.bar(species, means)
plt.title("Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length")
plt.tight_layout()
plt.savefig("sepal_length_means.pdf")

print("Plot saved.")