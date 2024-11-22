from matplotlib import pyplot as plt
import numpy as np
import os

def f(x,a,b):
    return 1 + (a/x)**b
x_right = np.linspace(0.01,200,20000)

plt.xlim(0,8)
plt.ylim(0,70)
plt.plot(x_right, f(x_right,1,1),label='α=1,β=1',color='blue')
plt.plot(x_right,f(x_right,2,1),label='α=2,β=1',color='green')
plt.plot(x_right,f(x_right,1,2),label='α=1,β=2',color='magenta')
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axix')
plt.title(r"$f(x)= \frac{x^{β}+α^{β}}{x^{β}}$ for different parameter values and x>0")
plt.legend()

plt.axes([0.2,0.7,0.2,0.2])
plt.plot(x_right, f(x_right,1,1),label='α=1,β=1',color='blue')
plt.plot(x_right,f(x_right,2,1),label='α=2,β=1',color='green')
plt.plot(x_right,f(x_right,1,2),label='α=1,β=2',color='magenta')
plt.xlim(0,200)
plt.ylim(0.9,1.2)
plt.text(10,0.93,'For bigger x values',fontdict={'size': 8})
plt.grid(True)

plt.axes([0.5,0.7,0.2,0.2])
plt.plot(x_right, f(x_right,1,1),label='α=1,β=1',color='blue')
plt.plot(x_right,f(x_right,2,1),label='α=2,β=1',color='green')
plt.plot(x_right,f(x_right,1,2),label='α=1,β=2',color='magenta')
plt.xlim(0,2)
plt.ylim(0,5)
plt.text(0.1,0.5,'For smaller x values',fontdict={'size': 8})
plt.grid(True)

plt.tight_layout()
plt.savefig(r"c:\pyhton\DZ_IZ\graphing\second_task",dpi=600)
plt.show()