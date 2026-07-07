from matplotlib import pyplot as plt
from dataset_access import dataset as da
import numpy as np

ages=da("ages")
ppl_id=ages['Responder_id']
age=ages['Age']
bins=np.arange(0,100,5)
print(bins)
plt.hist(age,bins=bins)
plt.show()