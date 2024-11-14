from matplotlib import pyplot as plt
import numpy as np
import os

def f(x,a,b):
    return 1 + (a/x)**b

x_left = np.linspace(-200,-0.01,20000)

plt.plot(x_left,f(x_left,1,1),label='α=1,β=1',color='blue')
plt.plot(x_left,f(x_left,2,1),label='α=2,β=1',color='green')
plt.plot(x_left,f(x_left,1,2),label='α=1,β=2',color='magenta')
plt.hlines(1,-100,100,linestyles='dashed',colors='red')
plt.xlim(-5,0)
plt.ylim(-24,26)
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axix')
plt.title(r"$f(x)= \frac{x^{β}+α^{β}}{x^{β}}$ for different parameter values and x<0")
plt.legend()


plt.axes([0.2,0.2,0.5,0.2])
plt.xlim(-200,0)
plt.ylim(0.8,1.2)
plt.grid(True)
plt.plot(x_left,f(x_left,1,1),label='α=1,β=1',color='blue')
plt.plot(x_left,f(x_left,2,1),label='α=2,β=1',color='green')
plt.plot(x_left,f(x_left,1,2),label='α=1,β=2',color='magenta')
plt.text(-190,0.85,'For x approaching -∞')
plt.savefig(r"c:\pyhton\DZ_IZ\graphing\third_task",dpi=600)
plt.show()