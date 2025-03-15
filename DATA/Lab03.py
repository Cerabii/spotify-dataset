import csv
import os
import random
import argparse


def splitData(dataset):
    split_index = int(len(dataset) * 0.8)
    train_data = dataset[:split_index]
    test_data = dataset[split_index:]

    return train_data, test_data

def splitDataRandom(dataset):
    shuffled = dataset.copy()       # Copy the dataset
    random.shuffle(shuffled)        # Randomly shuffle the dataset (for more randomness)

    # Portion and assign the data into 70%, 15%, and 15% respectively
    total_length = len(dataset)
    train_end = int(total_length * 0.7)
    val_end = train_end + int(total_length * 0.15)      # And test data is the rest of it!

    # Split the data into three parts
    train = shuffled[:train_end]
    validate = shuffled[train_end:val_end]
    test_data = shuffled[val_end:]

    return train, validate, test_data

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to the dataset")
    args = parser.parse_args()

    filePath = os.path.abspath("Most Streamed Spotify Songs 2024.csv")

    with open(filePath, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        dataset = list(reader)
pass