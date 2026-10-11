#example1

# A list of circuit net names
nets = ["A", "B", "Y", "Z", "OUT"]
print("example1")
print("First net:", nets[0])
print("Last net:", nets[-1])
print("Middle section:", nets[1:4])
print()


#example2

# A tiny ML dataset: (feature, label)
dataset = [
    (0.2, 0),
    (0.7, 1),
    (0.9, 1)
]

sample = dataset[1]
print("example2")
print("Selected sample:", sample)
print("Feature:", sample[0])
print("Label:", sample[1])
print()

#example3

# Each row contains [feature_1, feature_2, label]
dataset = [
    [1.2, 3.4, 0],
    [2.1, 4.5, 1],
    [0.8, 2.7, 0],
    [3.0, 5.1, 1]
]

# Select the second sample
sample = dataset[1]

# Separate its features and label
features = sample[:2]
label = sample[2]
print("example3")
print("Selected sample:", sample)
print("Features:", features)
print("Label:", label)

# Select the first two samples
batch = dataset[:2]
print("Batch size:", len(batch))
print()

#example4


gates = [
    ["AND", "A", "B", "N1"],
    ["OR", "N1", "C", "N2"],
    ["NOT", "N2", None, "OUT"]
]

print("example4")
for gate in gates:
    gate_type = gate[0]
    output_net = gate[3]

    print("Gate:", gate_type)
    print("Output:", output_net)

    if gate_type == "NOT":
        print("This gate has one input.")
print()

#example5
circuit = [
    ["AND1", "A", "B", "Y"],
    ["NOT1", "Y", "Z"]
]
print("example5")
print(circuit[0])
print(circuit[0][0])
print(circuit[0][3])
print(circuit[1][2])
print(circuit[-1][-1])
print(circuit[1][3])
print()
