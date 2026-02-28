import seabornEg as sns
import matplotlib.pyplot as plt
from seabornEg import load_dataset

# Load the Iris dataset
iris = load_dataset("iris")

# Scatter plot: Petal length vs Petal width, colored by species
plt.figure(figsize=(8, 6))
sns.scatterplot(data=iris, x="petal_length", y="petal_width", hue="species", palette="viridis")
plt.title("Scatter Plot: Petal Length vs Petal Width", fontsize=14)
plt.xlabel("Petal Length (cm)", fontsize=12)
plt.ylabel("Petal Width (cm)", fontsize=12)
plt.legend(title="Species", fontsize=10)
plt.grid(True)
plt.show()

# Boxplot: Sepal length across different species
plt.figure(figsize=(8, 6))
sns.boxplot(data=iris, x="species", y="sepal_length", palette="pastel")
plt.title("Boxplot: Sepal Length Across Species", fontsize=14)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepal Length (cm)", fontsize=12)
plt.grid(axis='y')
plt.show()