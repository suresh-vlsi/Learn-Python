gate_name = "AND"
number_of_inputs = 2
delay = 1.5
is_enabled = True
print(1)
print(type(gate_name))
print(type(number_of_inputs))
print(type(delay))
print(type(is_enabled))
print()
print("Gate:", gate_name)
print("Number of Inputs:", number_of_inputs)
print("Delay:", delay)
print("Is Enabled:", is_enabled)
print()
gate_name = "XOR"
number_of_inputs = 2
delay = 3.2

print(2)
print("Gate:", gate_name)
print("Number of Inputs:", number_of_inputs * 2)
print("Delay:", delay + 1)
print()

gate_name = "NAND1"

stuck_at_0 = gate_name + "_SA0"
stuck_at_1 = gate_name + "_SA1"

faults = [stuck_at_0, stuck_at_1]

print(3)
print(type(faults))
print()
print("Gate:", gate_name)
print("Fault hypotheses:", faults)
print("Total hypotheses:", len(faults))
print()