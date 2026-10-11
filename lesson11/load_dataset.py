
import csv
import numpy as np


def load_dataset(filename):
    features = []
    labels = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        expected = {"feature1", "feature2", "label"}
        if not reader.fieldnames or not expected.issubset(reader.fieldnames):
            raise ValueError("CSV is missing required columns.")

        for row_number, row in enumerate(reader, start=2):
            try:
                x1 = float(row["feature1"])
                x2 = float(row["feature2"])
                label = int(row["label"])
            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"Invalid data on CSV row {row_number}."
                ) from error

            if label not in (0, 1):
                raise ValueError(
                    f"Label on row {row_number} must be 0 or 1."
                )

            features.append([x1, x2])
            labels.append(label)

    X = np.array(features, dtype=float).reshape(-1, 2)
    y = np.array(labels, dtype=int)

    if len(y) == 0:
        raise ValueError("Dataset contains no samples.")

    return X, y


if __name__ == "__main__":
    X, y = load_dataset("dataset.csv")

    print("Features:\n", X)
    print("Labels:", y)
    print("Feature matrix shape:", X.shape)
    print("Label vector shape:", y.shape)
