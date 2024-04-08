import os
import requests
from typing import Optional
from dotenv import load_dotenv

import numpy as np
import pandas as pd

from datasets import load_dataset

load_dotenv()

########################
session = requests.Session()  # Allows persistent connection


def guard_score(prompt: str, category: str) -> float:
    """Makes a request to the Lakera Guard and returns the score for a category."""
    response = session.post(
        f"https://api.lakera.ai/v1/{category}",
        json={"input": prompt},
        headers={'Authorization': f'Bearer {os.getenv("LAKERA_GUARD_API_KEY")}'},
    )
    return response.json()["results"][0]["category_scores"][category]


def eval_guard(
        df: pd.DataFrame,
        category: str,
        max_size: Optional[int] = None,
        score_thr: Optional[float] = 0.5
):
    """Computes standard detection metrics on the input DataFrame for the given category."""

    if category not in ["prompt_injection", "pii", "sexual", "hate", "unknown_links"]:
        raise ValueError(f"The category {category} does not correspond to an existing endpoint.")

    predictions, labels = [], []

    max_size = max_size if max_size is not None else len(df)
    # Iterate over your dataset.
    for _, row in df.head(max_size).iterrows():
        predictions.append(guard_score(row.text, category) > score_thr)
        labels.append(row.label)

    predictions = np.array(predictions)
    labels = np.array(labels)

    false_positives = np.sum((predictions == 1) & (labels == 0))
    false_negatives = np.sum((predictions == 0) & (labels == 1))

    # Print relevant metrics.
    print(f"False positives: {false_positives} (total: {len(predictions)})")
    print(f"False negatives: {false_negatives} (total: {len(predictions)})")
    print(f"Accuracy: {np.mean(predictions == labels)}")


########################
ds_name = "Lakera/gandalf_ignore_instructions"

data = load_dataset(ds_name)
df = pd.DataFrame(data["test"])
df["label"] = 1

for _, row in df.head(5).iterrows():
    print(row.text)
    print()

########################
eval_guard(df, "prompt_injection", max_size=100)
eval_guard(df, "prompt_injection", max_size=100, score_thr=0.1)

########################
ds_name = "hotpot_qa"

data = load_dataset(ds_name, "fullwiki")
df = pd.DataFrame(data["test"])
df["label"] = 0
df.rename(columns={"question": "text"}, inplace=True)

for _, row in df.head(5).iterrows():
    print(row.text)
    print()

eval_guard(df, "prompt_injection", max_size=100)

########################
ds_name = "beki/privy"
data = load_dataset(ds_name, "small")
df = pd.DataFrame(data["test"])
df.rename(columns={"full_text": "text"}, inplace=True)
df["label"] = 1

df_final = []
classes = set([])
for _, row in df.iterrows():
    for s in row["spans"]:
        # Only add rows with emails or credit cards.
        if "CREDIT_CARD" in s or "@" in s:
            df_final.append(row)
            continue

# Create the filtered DataFrame.
df_filtered = pd.DataFrame(df_final)

for _, row in df_filtered.head(5).iterrows():
    print(row.text)
    print()

eval_guard(df_filtered, "pii", max_size=100)