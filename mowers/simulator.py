from threading import Thread

from mowers.lawn import Lawn
from mowers.mower import Mower
from mowers.utils import EAST, NORTH, SOUTH, WEST, MOVE_FORWARD, TURN_LEFT, TURN_RIGHT


class Simulator:

    """Simulation manager for a lawn mowing process"""

    def __init__(self, input=None):
        if input:
            self.lawn = self.parse_input(input)
        else:
            self.lawn = Lawn()

    @staticmethod
    def parse_input(input):
        """Parse a string input, check its consistency and return a made lawn out of it"""
        lines = input.split("\n")
        width, height = map(int, lines[0].split(" "))

        if width <= 0 or height <= 0:
            raise ValueError("Lawn area should be strictly positive")

        mowers = []
        for i in range((len(lines)-1)//2):
            x, y, orientation = lines[2*i + 1].split(" ")
            x, y = int(x), int(y)
            movements = list(lines[2*i + 2])

            input_verification = [
                0 <= x <= width,
                0 <= y <= height,
                orientation in [NORTH, SOUTH, WEST, EAST]
            ] + list(map(lambda move: move in [MOVE_FORWARD, TURN_LEFT, TURN_RIGHT], movements))

            mowers.append(Mower(x, y, orientation, movements))

            if not all(input_verification):
                raise ValueError("Wrong input for mower number {}".format(i))

        return Lawn(width, height, mowers)

    @staticmethod
    def make_output(mowers):
        """Return a string of the formatted output"""
        lines = []
        for mower in mowers:
            lines.append("{x} {y} {o}".format(x=mower.x, y=mower.y, o=mower.orientation))
        return "\n".join(lines)

    def run(self):
        """For each mower on the lawn run the movements in a new thread. Return a formatted output once all ended"""
        threads = [Runner(self.lawn, mower) for mower in self.lawn.mowers]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        return self.make_output(self.lawn.mowers)


class Runner(Thread):

    """Thread class in order to run a mower movement list"""

    def __init__(self, lawn, mower):
        self.lawn = lawn
        self.mower = mower
        Thread.__init__(self)

    def run(self):
        """Run all the mower's movement list"""
        for movement in self.mower.movements:
            self.lawn.move_mower(self.mower, movement)
            # Uncomment the next line in order to print the execution parallelism:
            # print(self.lawn.mowers_positions.keys())
