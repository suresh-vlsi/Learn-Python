x = 10
print(1)
print("x > 5", x > 5)    # True
print("x == 10", x == 10)  # True
print("x != 7", x != 7)   # True
print("x < 5", x < 5)    # False
print()

voltage = 1
enabled = True
print(2)
print("voltage=", voltage)
print("enabled=", enabled)
print("voltage == 1 and enabled", voltage == 1 and enabled)  # True
print("voltage == 0 or enabled", voltage == 0 or enabled)   # True
print("not enabled", not enabled)               # False
print()

column = 10
number_of_banks = 4

bank = column % number_of_banks
local_column = column // number_of_banks
print(3)
print("Bank:", bank)
print("Local Column:", local_column)
print()

# Arithmetic operators
a = 17
b = 5
print(4)
print("Addition:", a + b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print()
# Comparisons
print("a greater than b:", a > b)
print("a equals b:", a == b)
print()

# Logical operators
ready = True
has_error = False
print(5)
print("Can proceed:", ready and not has_error)
print()


def calculate_address(row, column):
    bank = column % 4
    local_address = 64 * row + column // 4
    physical_address = 16384 * bank + local_address

    return bank, local_address, physical_address


row = 2
column = 10

bank, local, physical = calculate_address(row, column)
print(6)
print("Bank:", bank)
print("Local address:", local)
print("Physical address:", physical)
print()