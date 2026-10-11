#example1
# List: ordered fault hypotheses
faults = ["N1_SA0", "N1_SA1", "N1_SA0"]

# Set: remove duplicate entries
unique_faults = set(faults)

# Tuple: fixed row-column coordinate
coordinate = (2, 10)

# Dictionary: signal names and logic values
signals = {"A": 1, "B": 0}

signals["B"] = 1
print("example1")
print("Original faults:", faults)
print()
print("Unique faults:", unique_faults)
print("Unique fault count:", len(unique_faults))
print()
print("Coordinate:", coordinate)
print()
print("Updated signals:", signals)
print()

#example2

# Each tuple contains (input feature, class label)
dataset = [
    (0.2, 0),
    (0.7, 1),
    (0.9, 1),
    (0.3, 0)
]

predictions = [0, 1, 1, 1]

correct = 0

for i in range(len(dataset)):
    actual_label = dataset[i][1]
    predicted_label = predictions[i]

    if actual_label == predicted_label:
        correct += 1

accuracy = correct / len(dataset)

metrics = {"accuracy": accuracy}
print("example2")
print("Correct predictions:", correct)
print("Metrics:", metrics)
print()

#example3

signals = {
    "A": 1,
    "B": 0
}

faults = [
    {"net": "A", "stuck_at": 0},
    {"net": "B", "stuck_at": 1}
]

print("example3")

for fault in faults:
    net = fault["net"]
    stuck_value = fault["stuck_at"]

    observed_value = signals[net]

    if observed_value != stuck_value:
        detected = True
    else:
        detected = False

    print(net, "detected:", detected)
