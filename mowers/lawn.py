from mowers.utils import EAST, NORTH, SOUTH, WEST, MOVE_FORWARD, TURN_LEFT, TURN_RIGHT


class Lawn:

    def __init__(self, width=5, height=5, mowers=[]):
        self.width = width
        self.height = height
        self.mowers = []
        self.mowers_positions = {}
        for mower in mowers:
            self.add_mower(mower)

    def add_mower(self, mower):
        self.mowers.append(mower)
        self.mowers_positions[str([mower.x, mower.y])] = mower

    def move_mower(self, mower, movement):
        if movement == TURN_LEFT:
            mower.turn_left()
        elif movement == TURN_RIGHT:
            mower.turn_right()
        elif movement == MOVE_FORWARD:
            x, y = mower.get_next_position()
            if 0 <= x <= self.width and 0 <= y <= self.height and str([x, y]) not in self.mowers_positions.keys():
                self.mowers_positions.pop(str([mower.x, mower.y]))
                mower.move_to(x, y)
                self.mowers_positions[str([mower.x, mower.y])] = mower
        else:
            raise ValueError("Unknown type of movement")
