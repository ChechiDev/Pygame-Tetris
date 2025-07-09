# blocks.py

from block import Block
from position import Position

# Subclase heredada de Block, para configurar la pieza y rotación
class LBlock(Block):
    def __init__(self):
        super().__init__(id = 1)

        self._cells = {
            0: [Position(0, 2), Position(1, 0), Position(1, 1), Position(1, 2)],
            1: [Position(0, 1), Position(1, 1), Position(2, 1), Position(2, 2)],
            2: [Position(1, 0), Position(1, 1), Position(1, 2), Position(2, 0)],
            3: [Position(0, 0), Position(0, 1), Position(1, 1), Position(2, 1)],
        }
