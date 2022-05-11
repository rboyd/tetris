# Tetris
> Simplified Tetris engine.


```python
%pip install nbdev
```

    Requirement already satisfied: nbdev in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (1.2.8)
    Requirement already satisfied: ipykernel in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (6.2.0)
    Requirement already satisfied: pyyaml in /usr/local/lib/python3.9/site-packages (from nbdev) (6.0)
    Requirement already satisfied: jupyter in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (1.0.0)
    Requirement already satisfied: pip in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (21.1.3)
    Requirement already satisfied: packaging in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (21.0)
    Requirement already satisfied: jupyter-client<8 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (6.1.12)
    Requirement already satisfied: nbconvert>=6.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (6.1.0)
    Requirement already satisfied: Jinja2<3.1.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (3.0.1)
    Requirement already satisfied: fastrelease in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (0.1.16)
    Requirement already satisfied: fastcore>=1.4.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (1.4.2)
    Requirement already satisfied: ghapi in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (0.1.20)
    Requirement already satisfied: nbformat>=4.4.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbdev) (5.1.3)
    Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from Jinja2<3.1.0->nbdev) (2.0.1)
    Requirement already satisfied: traitlets in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter-client<8->nbdev) (5.0.5)
    Requirement already satisfied: jupyter_core>=4.6.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter-client<8->nbdev) (4.7.1)
    Requirement already satisfied: pyzmq>=13 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter-client<8->nbdev) (22.2.1)
    Requirement already satisfied: python-dateutil>=2.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter-client<8->nbdev) (2.8.2)
    Requirement already satisfied: tornado>=4.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter-client<8->nbdev) (6.1)
    Requirement already satisfied: mistune<2,>=0.8.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (0.8.4)
    Requirement already satisfied: pygments>=2.4.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (2.10.0)
    Requirement already satisfied: jupyterlab_pygments in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (0.1.2)
    Requirement already satisfied: entrypoints>=0.2.2 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (0.3)
    Requirement already satisfied: bleach in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (4.0.0)
    Requirement already satisfied: pandocfilters>=1.4.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (1.4.3)
    Requirement already satisfied: testpath in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (0.5.0)
    Requirement already satisfied: defusedxml in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (0.7.1)
    Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbconvert>=6.1->nbdev) (0.5.4)
    Requirement already satisfied: nest-asyncio in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbclient<0.6.0,>=0.5.0->nbconvert>=6.1->nbdev) (1.5.1)
    Requirement already satisfied: ipython_genutils in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbformat>=4.4.0->nbdev) (0.2.0)
    Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from nbformat>=4.4.0->nbdev) (3.2.0)
    Requirement already satisfied: setuptools in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4.0->nbdev) (57.0.0)
    Requirement already satisfied: attrs>=17.4.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4.0->nbdev) (21.2.0)
    Requirement already satisfied: six>=1.11.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4.0->nbdev) (1.16.0)
    Requirement already satisfied: pyrsistent>=0.14.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.4.0->nbdev) (0.18.0)
    Requirement already satisfied: webencodings in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from bleach->nbconvert>=6.1->nbdev) (0.5.1)
    Requirement already satisfied: ipython<8.0,>=7.23.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipykernel->nbdev) (7.26.0)
    Requirement already satisfied: matplotlib-inline<0.2.0,>=0.1.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipykernel->nbdev) (0.1.2)
    Requirement already satisfied: appnope in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipykernel->nbdev) (0.1.2)
    Requirement already satisfied: debugpy<2.0,>=1.0.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipykernel->nbdev) (1.4.1)
    Requirement already satisfied: jedi>=0.16 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipython<8.0,>=7.23.1->ipykernel->nbdev) (0.18.0)
    Requirement already satisfied: decorator in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipython<8.0,>=7.23.1->ipykernel->nbdev) (5.0.9)
    Requirement already satisfied: pickleshare in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipython<8.0,>=7.23.1->ipykernel->nbdev) (0.7.5)
    Requirement already satisfied: prompt_toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipython<8.0,>=7.23.1->ipykernel->nbdev) (3.0.19)
    Requirement already satisfied: backcall in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipython<8.0,>=7.23.1->ipykernel->nbdev) (0.2.0)
    Requirement already satisfied: pexpect>4.3 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from ipython<8.0,>=7.23.1->ipykernel->nbdev) (4.8.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jedi>=0.16->ipython<8.0,>=7.23.1->ipykernel->nbdev) (0.8.2)
    Requirement already satisfied: ptyprocess>=0.5 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from pexpect>4.3->ipython<8.0,>=7.23.1->ipykernel->nbdev) (0.7.0)
    Requirement already satisfied: wcwidth in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from prompt_toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython<8.0,>=7.23.1->ipykernel->nbdev) (0.2.5)
    Requirement already satisfied: jupyter-console in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter->nbdev) (6.4.0)
    Requirement already satisfied: qtconsole in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter->nbdev) (5.3.0)
    Requirement already satisfied: notebook in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from jupyter->nbdev) (6.4.3)
    Requirement already satisfied: ipywidgets in /usr/local/lib/python3.9/site-packages (from jupyter->nbdev) (7.6.3)
    Requirement already satisfied: widgetsnbextension~=3.5.0 in /usr/local/lib/python3.9/site-packages (from ipywidgets->jupyter->nbdev) (3.5.1)
    Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /usr/local/lib/python3.9/site-packages (from ipywidgets->jupyter->nbdev) (1.0.0)
    Requirement already satisfied: Send2Trash>=1.5.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from notebook->jupyter->nbdev) (1.8.0)
    Requirement already satisfied: argon2-cffi in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from notebook->jupyter->nbdev) (20.1.0)
    Requirement already satisfied: prometheus-client in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from notebook->jupyter->nbdev) (0.11.0)
    Requirement already satisfied: terminado>=0.8.3 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from notebook->jupyter->nbdev) (0.11.0)
    Requirement already satisfied: cffi>=1.0.0 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from argon2-cffi->notebook->jupyter->nbdev) (1.14.6)
    Requirement already satisfied: pycparser in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from cffi>=1.0.0->argon2-cffi->notebook->jupyter->nbdev) (2.20)
    Requirement already satisfied: pyparsing>=2.0.2 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from packaging->nbdev) (2.4.7)
    Requirement already satisfied: qtpy>=2.0.1 in /usr/local/Cellar/jupyterlab/3.1.7/libexec/lib/python3.9/site-packages (from qtconsole->jupyter->nbdev) (2.1.0)
    [33mWARNING: You are using pip version 21.1.3; however, version 22.0.4 is available.
    You should consider upgrading via the '/usr/local/Cellar/jupyterlab/3.1.7/libexec/bin/python3.9 -m pip install --upgrade pip' command.[0m
    Note: you may need to restart the kernel to use updated packages.


This file will become your README and also the index of your documentation.

## Install

`poetry install`

## How to use

`./main.py <input.txt >output.txt`

```python
pf = Playfield()
pf
```




    <tetris.playfield.Playfield at 0x11162f6d0>



```python
from nbdev.imports import IN_NOTEBOOK
```

```python
i = Piece("****")
i
```




    
![svg](docs/images/output_8_0.svg)
    



```python
from IPython.display import display
```

```python
pf.add(i, 0)
pf
```




    <tetris.playfield.Playfield at 0x11162f6d0>



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



    
![svg](docs/images/output_13_1.svg)
    


    z



    
![svg](docs/images/output_13_3.svg)
    


    t



    
![svg](docs/images/output_13_5.svg)
    


    s



    
![svg](docs/images/output_13_7.svg)
    


    j



    
![svg](docs/images/output_13_9.svg)
    


    q



    
![svg](docs/images/output_13_11.svg)
    


    l



    
![svg](docs/images/output_13_13.svg)
    


```python
from tetris.controller import Controller

c = Controller()
pf = c.process('I0,I4,Q8')
```


    <tetris.playfield.Playfield at 0x11162ebe0>



    <tetris.playfield.Playfield at 0x11162ebe0>



    <tetris.playfield.Playfield at 0x11162ebe0>


```python
from tetris.renderer import Renderer
renderer = Renderer()
renderer.playfield_to_svg(pf)
```




    
![svg](docs/images/output_15_0.svg)
    



```python
pf = c.process('T1,Z3,I4')
```


    <tetris.playfield.Playfield at 0x1116980a0>



    <tetris.playfield.Playfield at 0x1116980a0>



    <tetris.playfield.Playfield at 0x1116980a0>


```python
c.process('Q0,I2,I6,I0,I6,I6,Q2,Q4')
```


    <tetris.playfield.Playfield at 0x1116840a0>



    <tetris.playfield.Playfield at 0x1116840a0>



    <tetris.playfield.Playfield at 0x1116840a0>



    <tetris.playfield.Playfield at 0x1116840a0>



    <tetris.playfield.Playfield at 0x1116840a0>



    <tetris.playfield.Playfield at 0x1116840a0>



    <tetris.playfield.Playfield at 0x1116840a0>



    <tetris.playfield.Playfield at 0x1116840a0>





    <tetris.playfield.Playfield at 0x1116840a0>


