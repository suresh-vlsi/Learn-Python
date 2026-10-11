#example1
gates = ["AND", "OR", "NOT"]
print(1)
print("-----")
for gate in gates:
    print(gate)
print()

#example2
print(2)
print("-----")
for i in range(4):
    print(i)
print()

#example3
count = 0
print(3)
print("-----")
while count < 3:
    print(count)
    count += 1
print()

#example4
gates = ["N1", "N2"]
print(4)
print("-----")
for gate in gates:
    print(gate + "_SA0")
    print(gate + "_SA1")
print()

#example5
gates = ["AND1", "OR1", "NOT1"]
print(5)
print("-----")
for gate in gates:
    print("Processing:", gate)
    print(gate + "_SA0")
    print(gate + "_SA1")

print("Fault generation complete.")
print()

#example6
print(6)
print("-----")
count = 0

while count < 4:
    print("Iteration:", count)
    count += 1

print("Loop finished.")
print()

#example7
probabilities = [0.15, 0.62, 0.91, 0.38, 0.77]
predictions = []
print(7)
print("-----")
for probability in probabilities:
    if probability >= 0.5:
        prediction = 1
    else:
        prediction = 0

    predictions.append(prediction)

print("Predictions:", predictions)
print()

#example8
nets = ["N1", "N2", "N3", "OUT"]
faults = []
print(8)
print("-----")
for net in nets:
    faults.append(net + "_SA0")
    faults.append(net + "_SA1")

print("Total fault hypotheses:", len(faults))

for fault in faults:
    print(fault)
print()

#example9
print(9)
print("-----")
for i in range(1, 4):
    print(i)
print()
