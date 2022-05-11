# Tetris
> Simplified Tetris engine.


This file will become your README and also the index of your documentation.

## Install

`poetry install`

## How to use

`./tetris.py <input.txt >output.txt`

```python
pf = Playfield()
pf
```




    
![svg](docs/images/output_5_0.svg)
    



```python
i = Piece("****")
i
```




    
![svg](docs/images/output_6_0.svg)
    



```python
pf.add(i, 0)
pf
```




    
![svg](docs/images/output_7_0.svg)
    



```python
pf.height
```




    1



```python
loader = PieceLoader()
```

```python
from IPython.display import SVG, display

    
for name, piece in loader.pieces.items():
    print(name)
    display(SVG(piece._repr_svg_()))

```

    i



    
![svg](docs/images/output_10_1.svg)
    


    z



    
![svg](docs/images/output_10_3.svg)
    


    t



    
![svg](docs/images/output_10_5.svg)
    


    s



    
![svg](docs/images/output_10_7.svg)
    


    j



    
![svg](docs/images/output_10_9.svg)
    


    q



    
![svg](docs/images/output_10_11.svg)
    


    l



    
![svg](docs/images/output_10_13.svg)
    


```python
from tetris.controller import Controller

c = Controller()
pf = c.process('I0,I4,Q8')
```

```python
pf = c.process('T1,Z3,I4')
```

```python
c.process('Q0,I2,I6,I0,I6,I6,Q2,Q4')
```




    
![svg](docs/images/output_13_0.svg)
    


