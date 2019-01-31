import numpy as ny
from matplotlib import pyplot
fs=int(input("enter a number"))
f=int(input("enter a number"))
n=ny.linspace(0,10,30)
x=ny.sin(2*3.14*f*n/fs)
pyplot.stem(x)
pyplot.show()