import csv
import os
import random
import argparse
import pandas as pd


def splitData(dataset):
    split_index = int(len(dataset) * 0.8)
    train_data = dataset[:split_index]
    test_data = dataset[split_index:]

    return train_data, test_data

def splitDataRandom(dataset):
    shuffled = dataset.copy()       # Copy the dataset
    random.shuffle(shuffled)        # Randomly shuffle the dataset (for more randomness)

    # Portion and assign the data into 80% and 20% respectively
    split_index = int(len(shuffled) * 0.8)
    train_data = shuffled[:split_index]
    test_data = shuffled[split_index:]

    return train_data, test_data

def analyzeData(dataset, header):

    df = pd.DataFrame(dataset, columns=header)

    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            continue
    
    print("Dataframe statistics:")
    print("Mean:\n", df.mean(numeric_only=True))
    print("Max:\n", df.max(numeric_only=True))
    print("Min:\n", df.min(numeric_only=True))
    print("Correlation:\n", df.corr(numeric_only=True))

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to the dataset")
    args = parser.parse_args()

    filePath = os.path.abspath(args.file)

    with open(filePath, newline='', encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        dataset = list(reader)

    header = dataset[0]
    dataset = dataset[1:]

    train_data, test_data = splitDataRandom(dataset)

    print(f"Train data: {len(train_data)}")
    print(f"Test data: {len(test_data)}")

    analyzeData(train_data, header)

if __name__ == "__main__":
    main()