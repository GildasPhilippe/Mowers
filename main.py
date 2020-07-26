from os import listdir
from os.path import join
import sys

from mowers.simulator import Simulator


def run_input(path):
    print("TESTING {}".format(path))
    with open(path, "r") as f:
        input = f.read()
    simulator = Simulator(input)
    print(simulator.run())
    print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_path = sys.argv[1]
        run_input(input_path)
    else:
        input_folder = "inputs/"
        inputs = [join(input_folder, fname) for fname in listdir(input_folder)]
        for input_path in inputs:
            run_input(input_path)
