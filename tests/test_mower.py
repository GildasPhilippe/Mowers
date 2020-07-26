import unittest

from mowers.mower import Mower
from mowers.utils import EAST, NORTH, SOUTH, WEST, MOVE_FORWARD, TURN_LEFT, TURN_RIGHT


class MowerTest(unittest.TestCase):

    def test_turn_left(self):
        mower = Mower(0, 0, NORTH)
        mower.turn_left()
        self.assertEqual(WEST, mower.orientation)
        mower.turn_left()
        self.assertEqual(SOUTH, mower.orientation)
        mower.turn_left()
        self.assertEqual(EAST, mower.orientation)
        mower.turn_left()
        self.assertEqual(NORTH, mower.orientation)

    def test_turn_right(self):
        mower = Mower(0, 0, NORTH)
        mower.turn_right()
        self.assertEqual(EAST, mower.orientation)
        mower.turn_right()
        self.assertEqual(SOUTH, mower.orientation)
        mower.turn_right()
        self.assertEqual(WEST, mower.orientation)
        mower.turn_right()
        self.assertEqual(NORTH, mower.orientation)

    def test_move_to(self):
        mower = Mower(0, 0, NORTH)
        mower.move_to(3, 5)
        self.assertEqual(3, mower.x)
        self.assertEqual(5, mower.y)

    def test_get_next_position(self):
        mower = Mower(3, 3, NORTH)
        self.assertEqual((3, 4), mower.get_next_position())
        mower.orientation = SOUTH
        self.assertEqual((3, 2), mower.get_next_position())
        mower.orientation = WEST
        self.assertEqual((2, 3), mower.get_next_position())
        mower.orientation = EAST
        self.assertEqual((4, 3), mower.get_next_position())


if __name__ == '__main__':
    unittest.main()
