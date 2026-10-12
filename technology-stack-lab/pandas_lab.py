import pandas as pd

# Create a small VLSI timing dataset
data = {
    "Circuit": ["ALU", "FIFO", "UART", "MAC", "ALU"],
    "Delay_ns": [2.5, 3.1, 1.8, 4.2, 2.7],
    "Power_mW": [12.0, 8.5, 3.2, 18.0, 11.5],
    "Timing_Violations": [0, 2, 0, 4, 1]
}

df = pd.DataFrame(data)

print("Complete dataset:")
print(df)

print("\nAverage delay:")
print(df["Delay_ns"].mean())

print("\nCircuits with delay greater than 2.5 ns:")
print(df[df["Delay_ns"] > 2.5])

print("\nCircuits with timing violations:")
print(df[df["Timing_Violations"] > 0])