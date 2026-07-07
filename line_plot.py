from matplotlib import pyplot as plt
from dataset_access import dataset as da

# Load dataset
data = da("data")

# Sort by x values
sorted_data = data.sort_values(by="x")

# Plot
plt.plot(
    sorted_data["x"],
    sorted_data["y"],
    marker="o",
    linewidth=2
)

# Fill below the curve
plt.fill_between(
    sorted_data["x"],
    sorted_data["y"],
    alpha=0.3
)

# Axis labels
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Line Plot")

# Graph-paper style scale
plt.xlim(4, 14)
plt.ylim(4, 11)

plt.xticks(range(4, 15, 1))
plt.yticks(range(4, 12, 1))

# Grid
plt.grid(True)

plt.show()