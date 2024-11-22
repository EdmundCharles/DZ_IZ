from matplotlib import pyplot as plt
import numpy as np
import os

def f(x,a,b):
    return 1 + (a/x)**b

x_right = np.linspace(0.01,200,20000)
plt.subplot(1,3,1)
plt.plot(x_right, f(x_right,1,0),label='α=1,β=0',color='red')
plt.plot(x_right,f(x_right,1,-1),label='α=1,β=-1',color='blue')
plt.plot(x_right, f(x_right,1,0.5),label='α=1,β=0.5',color='magenta')
plt.plot(x_right,f(x_right,1,0.8),label='α=1,β=0.8',color='purple')
plt.xlim(0,3)
plt.ylim(0,5)
plt.xlabel('X-axis')
plt.ylabel('Y-axix')
plt.grid(True)
plt.legend(loc='upper right')


plt.subplot(1,3,2)
plt.plot(x_right, f(x_right,1,0),label='α=1,β=0',color='red')
plt.plot(x_right,f(x_right,1,-1),label='α=1,β=-1',color='blue')
plt.plot(x_right, f(x_right,1,-0.5),label='α=1,β=−0.5',color='magenta')
plt.plot(x_right,f(x_right,1,-0.8),label='α=1,β=−0.8',color='purple')
plt.xlim(0,3)
plt.ylim(0,5)
plt.xlabel('X-axis')
plt.ylabel('Y-axix')
plt.grid(True)
plt.legend(loc='upper right')

plt.subplot(1,3,3)
plt.plot(x_right, f(x_right,1,0),label='α=1,β=0',color='red')
plt.plot(x_right,f(x_right,1,-1),label='α=1,β=-1',color='blue')
plt.plot(x_right, f(x_right,1,-1.5),label='α=1,β=−1.5',color='magenta')
plt.plot(x_right,f(x_right,1,-2.5),label='α=1,β=−2.5',color='purple')
plt.xlim(0,3)
plt.ylim(0,5)
plt.xlabel('X-axis')
plt.ylabel('Y-axix')
plt.grid(True)
plt.legend(loc='upper right')
plt.suptitle(r"$f(x)= \frac{x^{β}+α^{β}}{x^{β}}$ for different parameter values")

plt.tight_layout()
plt.savefig(r"c:\pyhton\DZ_IZ\graphing\fourth_task",dpi=600)
plt.show()