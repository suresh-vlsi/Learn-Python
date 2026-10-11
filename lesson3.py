#example1
temperature = 105
if temperature > 100:
    print(1)
    print("High temperature")
    print()

#example2
probability = 0.35

print(2)
if probability >= 0.5:
    prediction = 1
    print("Class 1 selected")
else:
    prediction = 0
    print("Class 0 selected")

print("Prediction:", prediction)
print()

#example3
score = 85
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"
print(3)
print(grade)
print()

#example4
def classify_binary(probability):
    if probability >= 0.70:
        return 1
    elif probability < 0.30:
        return 0
    else:
        return "Uncertain"

print(4)
for p in [0.15, 0.50, 0.85]:
    print(p, "->", classify_binary(p))
print()

#example5
print(5)
def evaluate_fault(fault_name, detected):
    if detected:
        status = "DETECTED"
    else:
        status = "UNDETECTED"

    print(f"{fault_name}: {status}")


evaluate_fault("N1_SA0", True)
evaluate_fault("N2_SA1", False)
print()