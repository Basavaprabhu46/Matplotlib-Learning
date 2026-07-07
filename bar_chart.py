from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

taxis = pd.read_csv("dataset/taxis.csv")

pu_count = Counter(taxis["pickup_zone"].dropna())
top_10=pu_count.most_common(20)
print(top_10)

plt.barh([x[0] for x in top_10],[x[1] for x in top_10])
plt.xlabel("Number of Pickups")
plt.ylabel("Pickup Zone")
plt.show()
