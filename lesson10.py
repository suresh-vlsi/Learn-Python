#example1
print("example1")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

print()

#example2
print("example2")
def calculate_average(values):
    if not values:
        raise ValueError("The values list cannot be empty.")

    return sum(values) / len(values)


def main():
    readings = [10, 20, 30]

    try:
        average = calculate_average(readings)
    except ValueError as error:
        print("Input error:", error)
    else:
        print("Average:", average)
    finally:
        print("Calculation attempt finished.")


if __name__ == "__main__":
    main()

print()


#example3
print("example3")
def validate_net(record):
    if "name" not in record:
        raise ValueError("Net record is missing 'name'.")

    if "value" not in record:
        raise ValueError("Net record is missing 'value'.")

    if record["value"] not in (0, 1):
        raise ValueError(
            f"Invalid binary value for net {record['name']}."
        )

    return True


net = {"name": "N1", "value": 1}

try:
    validate_net(net)
except ValueError as error:
    print("Netlist error:", error)
else:
    print("Net record is valid.")
print()


#example4

import numpy as np
print("example4")
weights = np.array([0.2, 0.5, 0.1])
features = np.array([1.0, 2.0])

print("Weights shape:", weights.shape)
print("Features shape:", features.shape)

if weights.shape != features.shape:
    raise ValueError(
        "Feature count must match weight count."
    )

score = np.dot(weights, features)
print(score)

print()

