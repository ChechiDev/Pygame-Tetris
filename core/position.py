# position.py

class Position:
    def __init__(self, row: int, col: int) -> None:
        """
        Initialize a Position object with the given row and column.

        Args:
            row (int): The row index.
            col (int): The column index.
        """
        self._row = row
        self._col = col