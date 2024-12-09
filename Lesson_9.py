#Task1
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
#Task2
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
#Task3
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
#Task4
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