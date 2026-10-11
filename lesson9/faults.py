
def generate_faults(net):
    return [net + "_SA0", net + "_SA1"]


def count_faults(fault_list):
    return len(fault_list)
