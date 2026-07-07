from matplotlib import pyplot as plt
import dataset_access as da
from collections import Counter
diamonds=da.dataset("diamonds")
d_count=Counter(diamonds["cut"])
# print(d_count)

# explode:
explode=[0.03,0,0,0,0] # makes a pie cut outwards
plt.pie(d_count.values(),labels=d_count.keys(),explode=explode, autopct='%1.1f%%')

plt.show()

# features available:
'''
1. wedges = drawlines at slices
2. colors = colors of slices
3. explode
4. shadow
5.stragnle = starting of frist item at some angle 
6. autopct=  autopercentage which labesl percentage of pie taken
'''
