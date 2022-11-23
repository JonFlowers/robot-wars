class Arena:

    x = 0
    y = 0

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def is_arena_ready(self):
        if self.x == 0 or self.y == 0:
            return False
        return True

    def is_valid_location(self, x, y):
        if x > self.x or y > self.y or x == 0 or y == 0:
            return False
        return True