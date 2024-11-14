from matplotlib import pyplot as plt
import numpy as np
import os

def f(x,a,b):
    return 1 + (a/x)**b
x_right = np.linspace(0.01,200,20000)
plt.xlim(0,8)
plt.ylim(0,70)
plt.plot(x_right,f(x_right,1,1))
plt.axes([0.2,0.2,0.2,0.2])
plt.plot(x_right, f(x_right,1,1),label='α=1,β=1',color='blue')
plt.plot(x_right,f(x_right,2,1),label='α=2,β=1',color='green')
plt.plot(x_right,f(x_right,1,2),label='α=1,β=2',color='magenta')
plt.xlim(0,200)
plt.ylim(0.9,1.2)
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axix')
plt.title('For bigger x values')
plt.legend(prop={'size': 6})
plt.tight_layout()
plt.show()