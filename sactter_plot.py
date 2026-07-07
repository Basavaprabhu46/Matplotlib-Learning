from matplotlib import pyplot as plt
from dataset_access import dataset as da
import numpy as np
plt.style.use('seaborn-v0_8')
# x=np.random.randint(0,11,15)
# y=np.random.randint(0,11,15)

# colors=np.random.randint(0,11,15)
# size=np.random.randint(100,400,15)

# # plt.scatter(x,y,s=100,marker='x')
# plt.scatter(x,y,c=colors,s=size,cmap='Greens',edgecolors='black',linewidths=1,alpha=0.5)
# plt.colorbar().set_label('saturation')

yt=da('2019-05-31-data')
likes=yt['likes']
views=yt['view_count']
ratio=yt['ratio']


plt.scatter(views,likes,c=ratio,cmap='Greens')
plt.xscale('log')
plt.yscale('log')
plt.colorbar().set_label('ratio')
plt.xlabel('views')
plt.ylabel('likes')
plt.show()
