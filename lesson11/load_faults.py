
def load_faults(filename):
    faults = []

    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            parts = line.split()

            if not parts:
                continue

            if len(parts) != 2:
                raise ValueError(
                    f"Malformed fault on line {line_number}: {line.strip()!r}"
                )

            net, fault_type = parts

            if fault_type not in ("SA0", "SA1"):
                raise ValueError(
                    f"Unsupported fault type on line {line_number}: "
                    f"{fault_type}"
                )

            faults.append({
                "net": net,
                "fault_type": fault_type
            })

    return faults


if __name__ == "__main__":
    faults = load_faults("faults.txt")

    for fault in faults:
        print(fault)

    print("Total faults:", len(faults))
