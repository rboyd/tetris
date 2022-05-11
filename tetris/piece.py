# AUTOGENERATED! DO NOT EDIT! File to edit: 01_piece.ipynb (unless otherwise specified).

__all__ = ['Piece']

# Cell
from math import inf

try: from nbdev.imports import IN_NOTEBOOK
except: IN_NOTEBOOK=False

if IN_NOTEBOOK:
    import svgwrite

class Piece:
    def __init__(self, rep:str):
        self.arr = []

        srows = rep.split('\n')
        self._height = len(srows)
        self._width = len(srows[0])
        self._ceil = [-1] * self._width
        self._floor = [inf] * self._width
        for i, line in enumerate(reversed(srows)):
            row = [True if ch == '*' else False for ch in line]
            for j, col in enumerate(row):
                if col:
                    self._ceil[j] = i
                    self._floor[j] = min(self._floor[j], i)
            self.arr.append(row)

    @property
    def height(self) -> int:
        return self._height

    @property
    def num_cols(self) -> int:
        return len(self.arr[0])

    @property
    def toarray(self) -> [[bool]]:
        return self.arr

    def ceil(self, col:int) -> int:
        return self._ceil[col]

    def floor(self, col:int) -> int:
        return self._floor[col]

    def _repr_svg_(self) -> str:
        if not IN_NOTEBOOK:
            return
        side_len = 10
        dwg = svgwrite.Drawing()
        dwg.viewbox(0,0,800,50)

        for row in range(len(self.arr)):
            for col in range(len(self.arr[0])):
                left_top = (col*side_len, (self._height-row)*side_len)
                width_height = (side_len, side_len)
                fill = 'blue' if self.arr[row][col] else 'black'
                dwg.add(dwg.rect(left_top, width_height, fill=fill))
        return dwg.tostring()