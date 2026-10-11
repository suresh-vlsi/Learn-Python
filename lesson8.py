#example1

class LogicGate:
    print()
    print("example1")
    def __init__(self, name, gate_type):
        self.name = name
        self.gate_type = gate_type

    def describe(self):
        print(f"{self.name} is an {self.gate_type} gate.")


gate_a = LogicGate("G1", "AND")
gate_b = LogicGate("G2", "OR")

gate_a.describe()
gate_b.describe()
print()


#example2


class LogicGate:
    def __init__(self, name, gate_type):
        self.name = name
        self.gate_type = gate_type

    def evaluate(self, a, b=None):
        if self.gate_type == "AND":
            return a & b
        elif self.gate_type == "OR":
            return a | b
        elif self.gate_type == "NOT":
            return 1 - a
        else:
            raise ValueError("Unsupported gate type")


and_gate = LogicGate("G1", "AND")
or_gate = LogicGate("G2", "OR")
not_gate = LogicGate("G3", "NOT")

print("example2")
print("and of 1 and 0 is", and_gate.evaluate(1, 0))
print("or of 1 and 0 is", or_gate.evaluate(1, 0))
print("not of 1 is", not_gate.evaluate(1))
print()

#example3


import math


class LogisticModel:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def predict_probability(self, x):
        z = x * self.weight + self.bias
        return 1 / (1 + math.exp(-z))

    def predict(self, x):
        probability = self.predict_probability(x)
        return 1 if probability >= 0.5 else 0


model = LogisticModel(weight=1.0, bias=-1.0)

x = 2.0

print("example3")
print("Probability:", round(model.predict_probability(x), 4))
print("Prediction:", model.predict(x))
print()