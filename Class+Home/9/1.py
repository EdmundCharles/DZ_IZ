from matplotlib import pyplot as plt
import numpy as np
import os


def f(x,a,b):
    return 1 + (a/x)**b

x_left = np.linspace(-200,-0.01,20000)
x_right = np.linspace(0.01,200,20000)
plt.plot(x_left,f(x_left,1,1),color='blue')
plt.plot(x_left,f(x_left,2,1),color='green')
plt.plot(x_left,f(x_left,1,2),color='magenta')

plt.plot(x_right, f(x_right,1,1),label='α=1,β=1',color='blue')
plt.plot(x_right,f(x_right,2,1),label='α=2,β=1',color='green')
plt.plot(x_right,f(x_right,1,2),label='α=1,β=2',color='magenta')

plt.xlim(-5,5)
plt.ylim(-25,25)

plt.vlines(0,-100,100,linestyles='dashed',colors='red')
plt.hlines(1,-100,100,linestyles='dashed',colors='red')

plt.grid(True)
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axix')
plt.title(r"$f(x)= \frac{x^{β}+α^{β}}{x^{β}}$ for different parameter values")

plt.savefig(r"c:\pyhton\DZ_IZ\graphing\first_task",dpi=600)
plt.show()