# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['process_stdin']

# Cell
from .controller import Controller
import sys

def process_stdin():
    c = Controller()
    for line in sys.stdin:
        line.rstrip('\n')
        pf = c.process(line)
        print(pf.height)