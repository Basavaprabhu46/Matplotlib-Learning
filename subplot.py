from matplotlib import pyplot as plt
from dataset_access import dataset as da
job=da('job')

# plt.gcf()  # get the current figure
# plt.gca()  #get the current axis

age=job['Age']
All_Devs=job['All_Devs']
Python=job['Python']
JavaScript=job['JavaScript']

fig,(ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1)


ax1.plot(age,Python)
ax2.plot(age,JavaScript)
ax3.plot(age,All_Devs)

plt.show()
