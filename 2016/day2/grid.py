DIRECTIONS = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (-1, 0)
}
class Grid:
    def __init__(self):
        self._buttons = ["1","2","3","4","5","6","7","8","9","A","B","C","D"]

    def press_button(self, coord: tuple[int, int], direction: str) -> (str, tuple[int, int]):