# AUTOGENERATED! DO NOT EDIT! File to edit: 03_piece_loader.ipynb (unless otherwise specified).

__all__ = ['PieceLoader']

# Cell
from .piece import Piece
import os

class PieceLoader:
    def load(self, directory:str) -> None:
        self._pieces = {}
        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                with open(f, 'r') as inf:
                    data = inf.read()
                    self._pieces[filename] = Piece(data)

    def __getitem__(self, item):
         return self._pieces[item]

    @property
    def pieces(self):
        return self._pieces

    def __init__(self, directory:str = "data/"):
        self.load(directory)