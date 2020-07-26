import unittest

from mowers.lawn import Lawn
from mowers.mower import Mower
from mowers.utils import EAST, NORTH, SOUTH, WEST, MOVE_FORWARD, TURN_LEFT, TURN_RIGHT


class LawnTest(unittest.TestCase):

    def test_add_mower(self):
        mower1 = Mower(0, 0, NORTH)
        mower2 = Mower(3, 4, EAST)
        lawn = Lawn(5, 5)
        lawn.add_mower(mower1)
        lawn.add_mower(mower2)
        self.assertEqual([mower1, mower2], lawn.mowers)
        self.assertEqual(mower1, lawn.mowers_positions["[0, 0]"])
        self.assertEqual(mower2, lawn.mowers_positions["[3, 4]"])

    def test_move_mower(self):
        mower = Mower(0, 0, WEST)
        lawn = Lawn(5, 5, [mower])
        self.assertEqual(mower, lawn.mowers_positions["[0, 0]"])

        # Should be blocked on west border
        lawn.move_mower(mower, MOVE_FORWARD)
        self.assertEqual(mower, lawn.mowers_positions["[0, 0]"])
        self.assertEqual((mower.x, mower.y), (0, 0))
        self.assertEqual(mower.orientation, WEST)

        # Should turn right correctly
        lawn.move_mower(mower, TURN_LEFT)
        self.assertEqual(mower, lawn.mowers_positions["[0, 0]"])
        self.assertEqual((mower.x, mower.y), (0, 0))
        self.assertEqual(mower.orientation, SOUTH)

        # Should be blocked on South Border
        lawn.move_mower(mower, MOVE_FORWARD)
        self.assertEqual(mower, lawn.mowers_positions["[0, 0]"])
        self.assertEqual((mower.x, mower.y), (0, 0))
        self.assertEqual(mower.orientation, SOUTH)

        # Should turn left and move forward correctly
        lawn.move_mower(mower, TURN_LEFT)
        lawn.move_mower(mower, MOVE_FORWARD)
        self.assertEqual(mower, lawn.mowers_positions["[1, 0]"])
        self.assertEqual((mower.x, mower.y), (1, 0))
        with self.assertRaises(Exception):
            lawn.mowers_positions["[0, 0]"]

        # Should be blocked by second mower
        lawn.add_mower(Mower(1, 1))
        lawn.move_mower(mower, TURN_LEFT)
        lawn.move_mower(mower, MOVE_FORWARD)
        self.assertEqual((mower.x, mower.y), (1, 0))



if __name__ == '__main__':
    unittest.main()
