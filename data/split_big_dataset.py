import pickle

import numpy as np


def main():
    """
    Split "train.pickle" dataset into smaller file, so that file size is below GitHub storage limit (100MB) each
    """
    with open("train.pickle", "rb") as pickle_file:
        dataset = pickle.load(pickle_file)

    print("-"*100)
    print("Train pickle size")
    print(f"Keys: {dataset.keys()}")
    for key in dataset.keys():
        print(f"Column: {key} | Count: {len(dataset[key])}")
    print("-" * 100)

    coords = dataset["coords"]
    sizes = dataset["sizes"]
    labels = dataset["labels"]
    features = dataset["features"]

    half_dataset_index = int(len(coords) / 2)
    half_dataset_1 = {"coords": coords[:half_dataset_index], "sizes": sizes[:half_dataset_index],
                      "labels": labels[:half_dataset_index], "features": features[:half_dataset_index]}
    with open("train_1.pickle", "wb") as pickle_file:
        pickle.dump(half_dataset_1, pickle_file)

    half_dataset_2 = {"coords": coords[half_dataset_index:], "sizes": sizes[half_dataset_index:],
                      "labels": labels[half_dataset_index:], "features": features[half_dataset_index:]}
    with open("train_2.pickle", "wb") as pickle_file:
        pickle.dump(half_dataset_2, pickle_file)

    print(f"Splitted 'train.pickle' into 2 smaller at index {half_dataset_index}")

    with open("train_1.pickle", "rb") as pickle_file:
        dataset_1 = pickle.load(pickle_file)
    with open("train_2.pickle", "rb") as pickle_file:
        dataset_2 = pickle.load(pickle_file)

    print("-" * 100)
    print(f"Dataset 1 size: {len(dataset_1['coords'])}")
    print(f"Dataset 2 size: {len(dataset_2['coords'])}")
    print("-" * 100)
    combined = {}
    for column in ["coords", "sizes", "labels", "features"]:
        combined[column] = np.concatenate((dataset_1[column], dataset_2[column]), axis=0)
    print("Combined pickle")
    print(f"Keys: {combined.keys()}")
    for key in combined.keys():
        print(f"Column: {key} | Count: {len(combined[key])}")
    print("-" * 100)


if __name__ == "__main__":
    main()
