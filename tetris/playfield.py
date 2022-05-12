# AUTOGENERATED! DO NOT EDIT! File to edit: 02_playfield.ipynb (unless otherwise specified).

__all__ = ['Playfield']

# Cell
from math import inf
from .piece import Piece

class Playfield:
    def __init__(self, rows:int = 20, cols:int = 10):
        self._rows = rows
        self._cols = cols
        self._playfield = [[None] * cols for _ in range(rows)]
        self._column_height = [-1] * cols
        self._num_added = 0

    def toarray(self) -> [[bool]]:
        return self._playfield

    @property
    def col_height(self):
        return self._column_height

    @property
    def height(self) -> int:
        return max(height+1 for height in self._column_height)

    def add(self, piece:Piece, col:int) -> int:
        "Add the given piece to the playfield. It settles at the highest point of first contact."

        # Determine the row of the playfield where the bottom row of the piece
        # will land. If there are no populated blocks on the playfield then the
        # default landing row is the bottom of the playfield (row 0). Otherwise
        # it is the highest point of collision.
        resting_row = 0

        for i in range(piece.num_cols):
            if self._column_height[col+i] < 0:
                resting_row = max(resting_row, 0)
                continue

            #print(f'{i}: self._column_height[col+i]: {self._column_height[col+i]} piece.floor({i}): {piece.floor(i)}')
            collision_height = (self._column_height[col+i] + 1) - piece.floor(i)
            resting_row = max(resting_row, collision_height)
            #print(f'col_height: {collision_height} resting_row: {resting_row}')
        #print('resting_row:', resting_row)
        A = piece.toarray()

        self._num_added += 1
        for i, prow in enumerate(A):
            for j, pcol in enumerate(prow):
                if pcol:
                    self._playfield[resting_row+i][col+j] = self._num_added
                    self._column_height[col+j] = resting_row + piece.ceil(j)
        #print(self._column_height)
        return resting_row

    def clear(self, bottom_row:int, num_rows: int) -> int:
        "Clears any full rows, adjusting column heights. Returns number of cleared rows."
        top_row = bottom_row + num_rows
        cur_row = bottom_row
        cleared_lines = 0
        while cur_row < top_row:
            if all(self._playfield[cur_row]):
                del self._playfield[cur_row]
                self._rows -= 1
                top_row -= 1
                cleared_lines += 1
                self._column_height = [height-1 for height in self._column_height]
            else:
                cur_row += 1
        return cleared_lines

    def add_with_clear(self, piece:Piece, col:int) -> int:
        "Adds a piece at [col] and potentially clears any effected rows."
        resting_row = self.add(piece, col)
        return self.clear(resting_row, piece.height)