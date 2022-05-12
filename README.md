# Tetris
> Simplified Tetris engine.


Objects to simulate some primitive operations in the game of Tetris.

## How to use

Execute `main.py` to run test input and print resulting line height to stdout:

`./main.py <input.txt >output.txt`

## Install Optional Dependencies

The basic program should work without external dependencies. In order to execute Jupyter Notebook, work with renderer, etc:

`poetry install`

The project is implemented as an [nbdev](https://github.com/fastai/nbdev) notebook. Docs are generated from notebooks in literate programming fashion best viewed on Github or in Jupyter Notebook.

## Testing

Tests are run against the notebooks and CI executed in Github Actions (`./.github/workflows`).

Can be run from dev machine via:

$ `nbdev_test_nbs`

## The Class Library

```python
from tetris.core import *
from tetris.piece import Piece
from tetris.playfield import Playfield
from tetris.piece_loader import PieceLoader
from tetris.renderer import Renderer
```

## Playfield and Renderer

## Run interactively in Jupyter Notebook

Game objects are easily instantiated and rendered inside a Jupyter session:

```python
pf = Playfield()
rndr = Renderer()
rndr.playfield_to_svg(pf)
```




    
![svg](docs/images/output_12_0.svg)
    



## Piece

Instantiated with a row per line, pieces are described as strings. `*` for brick present, `-` for negative space.

```python
i = Piece("****")
rndr.piece_to_svg(i)
```




    
![svg](docs/images/output_14_0.svg)
    



```python
pf.add(i, 0) # i piece added at column 0
rndr.playfield_to_svg(pf)
```




    
![svg](docs/images/output_15_0.svg)
    



```python
pf.height
```




    1



## PieceLoader

Loads known piece definitions from a given data directory.

```python
loader = PieceLoader()
```

```python
from IPython.display import SVG, display

    
for name, piece in loader.pieces.items():
    print(name)
    display(rndr.piece_to_svg(piece))
```

    i



    
![svg](docs/images/output_19_1.svg)
    


    z



    
![svg](docs/images/output_19_3.svg)
    


    t



    
![svg](docs/images/output_19_5.svg)
    


    s



    
![svg](docs/images/output_19_7.svg)
    


    j



    
![svg](docs/images/output_19_9.svg)
    


    q



    
![svg](docs/images/output_19_11.svg)
    


    l



    
![svg](docs/images/output_19_13.svg)
    


## Controller

Implements a method `process` which can take a comma-delimited series of instructions `<piece><column>`. Pieces are added and lines are cleared. Takes an optional `Renderer`, renders SVG of current `Playfield` after every add/clear when run from Jupyter Notebook.

```python
from tetris.controller import Controller

c = Controller()
```

## Example 1

```python
pf = c.process('I0,I4,Q8', rndr)
```


    
![svg](docs/images/output_23_0.svg)
    



    
![svg](docs/images/output_23_1.svg)
    



    
![svg](docs/images/output_23_2.svg)
    


```python
assert(pf.height == 1)
```

```python
pf = c.process('T1,Z3,I4', rndr)
```


    
![svg](docs/images/output_25_0.svg)
    



    
![svg](docs/images/output_25_1.svg)
    



    
![svg](docs/images/output_25_2.svg)
    


```python
assert(pf.height == 4)
```

## Example 3

```python
pf = c.process('Q0,I2,I6,I0,I6,I6,Q2,Q4', Renderer())
```


    
![svg](docs/images/output_28_0.svg)
    



    
![svg](docs/images/output_28_1.svg)
    



    
![svg](docs/images/output_28_2.svg)
    



    
![svg](docs/images/output_28_3.svg)
    



    
![svg](docs/images/output_28_4.svg)
    



    
![svg](docs/images/output_28_5.svg)
    



    
![svg](docs/images/output_28_6.svg)
    



    
![svg](docs/images/output_28_7.svg)
    


```python
assert(pf.height == 3)
```
