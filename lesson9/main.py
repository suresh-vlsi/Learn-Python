
from faults import generate_faults, count_faults

nets = ["N1", "N2", "OUT"]
all_faults = []

for net in nets:
    all_faults.extend(generate_faults(net))

print("Faults:", all_faults)
print("Count:", count_faults(all_faults))
