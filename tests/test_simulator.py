import unittest

from mowers.lawn import Lawn
from mowers.mower import Mower
from mowers.simulator import Simulator
from mowers.utils import EAST, NORTH, SOUTH, WEST, MOVE_FORWARD, TURN_LEFT, TURN_RIGHT


class SimulatorTest(unittest.TestCase):

    def test_parse_input(self):
        simulator = Simulator()
        input = "\n".join([
            "5 3",
            "1 2 N",
            "LFLFLFLFF",
            "3 3 E",
            "FFRFFRFRRF"
        ])
        lawn = simulator.parse_input(input)
        mowers = lawn.mowers
        self.assertEqual(5, lawn.width)
        self.assertEqual(3, lawn.height)
        self.assertEqual(2, len(mowers))
        self.assertEqual((1, 2, NORTH), (mowers[0].x, mowers[0].y, mowers[0].orientation))
        self.assertEqual(["L", "F", "L", "F", "L", "F", "L", "F", "F"], mowers[0].movements)
        self.assertEqual((3, 3, EAST), (mowers[1].x, mowers[1].y, mowers[1].orientation))
        self.assertEqual(["F", "F", "R", "F", "F", "R", "F", "R", "R", "F"], mowers[1].movements)

    def test_parse_input_erros(self):
        simulator = Simulator()
        inputs = [
            "\n".join([
                "-2 3",  # width <= 0
                "1 2 N",
                "FFRFFRFRRF"
            ]),
            "\n".join([
                "5 3",
                "1 5 N",  # y > height
                "LFLFLFLFF"
            ]),
            "\n".join([
                "5 3",
                "3 3 F",  # F not an orientation
                "FFRFFRFRRF"
            ]),
            "\n".join([
                "5 3",
                "1 2 N",
                "LFLFLFNFF",  # N not a move
            ])
        ]
        for input in inputs:
            with self.assertRaises(Exception):
                simulator.parse_input(input)

    def test_make_output(self):
        simulator = Simulator()
        mowers = [
            Mower(1, 2, NORTH),
            Mower(6, 7, SOUTH),
            Mower(0, 0, EAST)
        ]
        self.assertEqual("1 2 N\n6 7 S\n0 0 E", simulator.make_output(mowers))

    def test_run(self):
        simulator = Simulator()
        mower1 = Mower(1, 2, NORTH, list("LFLFLFLFF"))
        mower2 = Mower(3, 3, EAST, list("FFRFFRFRRF"))
        simulator.lawn = Lawn(5, 5, [mower1, mower2])
        result = simulator.run()
        expected = "1 3 N\n5 1 E"
        self.assertEqual(expected, result)
        self.assertEqual((1, 3, NORTH), (mower1.x, mower1.y, mower1.orientation))
        self.assertEqual((5, 1, EAST), (mower2.x, mower2.y, mower2.orientation))


if __name__ == '__main__':
    unittest.main()
