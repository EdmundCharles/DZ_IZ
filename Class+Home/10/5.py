import pandas as pd
from matplotlib import pyplot as plt

df = pd.DataFrame({
    'age' : [i for i in range(0,13)],
    'weight_normal' : [3.4,4.3,5.1,5.8,6.5,7.1,7.6,8.2,8.6,9.1,9.5,9.8,10],
    'heavier_side' : [4.2,5.4,6.4,7.3,8.1,8.8,9.4,9.9,10.5,11,11.4,11.8,12.4],
    'lighter_side' : [2.7,3.3,3.9,4.5,5.1,5.6,6.1,6.6,7.1,7.5,8.2,8.5,9.1]
})

plt.plot(df['age'],df['weight_normal'],color='green',label='Average')
plt.plot(df['age'],df['heavier_side'],color='red',label='Heavier')
plt.plot(df['age'],df['lighter_side'],color='blue',label='Lighter')
plt.xlim(0,12)
plt.ylim(0,13)
plt.ylabel('Weight')
plt.xlabel('Age')
plt.title('Toddler weight depending on age and build')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()