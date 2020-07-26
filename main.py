import sys

from mowers.simulator import Simulator


def run_input(path):
    with open(path, "r") as f:
        input = f.read()
    simulator = Simulator(input)
    print(simulator.run())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
    else:
        input_path = "inputs/input1.txt"
    run_input(input_path)
