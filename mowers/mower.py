
from mowers.utils import EAST, NORTH, SOUTH, WEST, MOVE_FORWARD, TURN_LEFT, TURN_RIGHT


class Mower:

    """Mower entity class"""

    def __init__(self, x=0, y=0, orientation=NORTH, movements=[]):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.movements = movements

    def turn_left(self):
        """Update the mower's orientation to its left"""
        if self.orientation == NORTH:
            self.orientation = WEST
        elif self.orientation == WEST:
            self.orientation = SOUTH
        elif self.orientation == SOUTH:
            self.orientation = EAST
        elif self.orientation == EAST:
            self.orientation = NORTH
        else:
            raise ValueError("Inconsistent orientation")

    def turn_right(self):
        """Update the mower's orientation to its right"""
        if self.orientation == NORTH:
            self.orientation = EAST
        elif self.orientation == EAST:
            self.orientation = SOUTH
        elif self.orientation == SOUTH:
            self.orientation = WEST
        elif self.orientation == WEST:
            self.orientation = NORTH
        else:
            raise ValueError("Inconsistent orientation")

    def move_to(self, x, y):
        """Update the mower's coordinates to (x,y)"""
        self.x, self.y = x, y

    def get_next_position(self):
        """Return the coordinates of the mower in case it would move forward"""
        if self.orientation == NORTH:
            return self.x, self.y + 1
        elif self.orientation == SOUTH:
            return self.x, self.y - 1
        elif self.orientation == WEST:
            return self.x - 1, self.y
        elif self.orientation == EAST:
            return self.x + 1, self.y
        else:
            raise ValueError("Inconsistent orientation")
