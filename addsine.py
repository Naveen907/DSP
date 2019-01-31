import numpy as ny
from matplotlib import pyplot
fs=int(input("enter a number"))
f=int(input("enter a number"))
n=ny.arange(0,2000,1)
x=ny.sin(2*3.14*f*n/fs)
pyplot.plot(x)
pyplot.show()
fs2=int(input("enter a number"))
f2=int(input("enter a number"))
n2=ny.arange(0,2000,1)
x2=ny.sin(2*3.14*f2*n2/fs2)
pyplot.plot(x2)
pyplot.show()
y=x+x2
print("y")
pyplot.plot(y)
pyplot.show()