import math
import numpy as np
import sympy as S
def f(x) :
    return np.arctan(4**(x-20))
sum = 0

for i in range(40):
    sum += f(i)
res = 1/np.pi*(sum+np.pi/4)
print(res)
x = S.Symbol('x')
y = S.Symbol('y')
g =  -np.e**(x**2-18*x+81+2*np.log(3))

min = S.maximum(g,x)
print(min)

print(S.solveset((x**2-10*x+20)**2-10*(x**2-10*x+20)+20,x,domain = S.Reals))
print(5*np.cos(5*np.pi/21)+0.5+np.cos(3*np.pi/7)+np.cos(19*np.pi/21))