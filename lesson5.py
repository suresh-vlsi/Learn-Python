#example1
def average(a, b):
    result = (a + b) / 2
    return result

print(1)
print("-----")
value = average(10, 20)
print("mean of 10 and 20 is:", value)
print()

#example2
def square(x):
    return x * x
print(2)
print("-----")
answer = square(4)
print("square of 4 is:", answer)
print()

#example3

def calculate_power(voltage, current):
    power = voltage * current
    return power


v = 5
i = 2

p = calculate_power(v, i)

print(3)
print("-----")
print("Voltage:", v, "V")
print("Current:", i, "A")
print("Power:", p, "W")
print()

#example4

import math


def linear_score(x, weight, bias):
    return x * weight + bias


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def predict(x, weight, bias):
    score = linear_score(x, weight, bias)
    probability = sigmoid(score)

    if probability >= 0.5:
        prediction = 1
    else:
        prediction = 0

    return probability, prediction


probability, prediction = predict(2, 1.0, -1.0)
print(4)
print("-----")
print("Probability:", round(probability, 4))
print("Prediction:", prediction)
print()

#example5

def generate_faults_for_net(net):
    return [net + "_SA0", net + "_SA1"]


def generate_faults_for_circuit(nets):
    all_faults = []

    for net in nets:
        net_faults = generate_faults_for_net(net)
        all_faults.extend(net_faults)

    return all_faults


nets = ["N1", "N2", "OUT"]
faults = generate_faults_for_circuit(nets)

print(5)
print("-----")
print("Fault count:", len(faults))
print("Fault list:", faults)
print()

