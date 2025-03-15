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
    split_index = int(len(shuffled) * 0.8)
    train_data = shuffled[:split_index]
    test_data = shuffled[split_index:]

    return train_data, test_data

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to the dataset")
    args = parser.parse_args()

    filePath = os.path.abspath("Most Streamed Spotify Songs 2024.csv")

    with open(filePath, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        dataset = list(reader)
pass