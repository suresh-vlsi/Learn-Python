
def load_numbers(filename):
    numbers = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            value = line.strip()

            if value:
                numbers.append(float(value))

    return numbers


def main():
    numbers = load_numbers("readings.txt")

    print("Loaded values:", numbers)
    print("Number of readings:", len(numbers))
    print("Average:", sum(numbers) / len(numbers))


if __name__ == "__main__":
    main()
