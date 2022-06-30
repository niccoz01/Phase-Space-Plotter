# Phase-Space-Plotter
A phase portrait is a geometric representation of the trajectories of a dynamical system in the phase space. Such system can be written using differential equations of the form:

![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7Bdx%7D%7Bdt%7D=%20f(x,y)%20%5C;%5C;%5C;%5C;and%5C;%5C;%5C;%5C;%5Cfrac%7Bdy%7D%7Bdt%7D=g(x,y))

Phase portraits are a key tool in the study of dynamical systems. A phase portrait of a dynamical system illustrates the system's trajectories, stability states and instability states in the state space. The axes are the state variables.
This repository provides a simple phase space plotter using Python only.

## Requisites
The script is fully written in Python, version 3.8.3, which can be downloaded [here](https://www.python.org/downloads/release/python-383/). If you already have python you can check its version by typing in the command line:
```cmd
python --version
```
If you want to upgrade it:
```cmd
pip install python -- upgrade
```
In order to run the script, three additional modules are required
* [SymPy](https://www.sympy.org/en/index.html): Python library for symbolic mathematics
* [NumPy](https://numpy.org/): Package for scientific computing
* [MatplotLib](https://matplotlib.org/): Python visualization library
It is possible to install all of them by simply typing:
```cmd
pip install sympy numpy matplotlib
```

## How to use
The way to run the code is straightforward. In the command line just type:
```cmd
python run.py --d 'f(x,y)' 'g(x,y)' --xmin XMIN --xmax XMAX --ymin YMIN --ymax YMAX --n N --f F
```
Please note that only --d is required and the other arguments are optional (default values in the documentation).

## Examples
* Simple Pendulum (L=2g):


  ![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D=%20-%5Cfrac%7Bsin(x)%7D%7B2%7D%20%5Cequiv%20%5Cbegin%7Bcases%7D%20%20%20%20%20%20%20%20%20%5Cfrac%7Bdx%7D%7Bdt%7D=y%20%5C%5C%20%5Cfrac%7Bdy%7D%7Bdt%7D%20=%20-%20%5Cfrac%7Bsin(x)%7D%7B2%7D%5Cend%7Bcases%7D)


```cmd
python run.py --d 'y' '(-0.5*sin(x))' --xmin -10 --xmax 10 --ymin -4 --ymax 4
```

* Van der Poll oscillator (μ=3):


  ![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7Bdx%7D%7Bdt%7D=y)

  ![equation](https://latex.codecogs.com/svg.image?%5Cfrac%7Bdy%7D%7Bdt%7D=3(1-x%5E2)y-x)


```cmd
python run.py --d 'y' '3*(1-x**2)*y-x' --xmin -10 --xmax 10 --ymin -4 --ymax 4
```
