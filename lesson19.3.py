import seaborn as sns
import matplotlib.pyplot as plt

# Load the "tips" dataset
tips = sns.load_dataset("tips")

# Set style for Seaborn plots
sns.set(style="whitegrid")

# Scatter Plot
sns.scatterplot(x="total_bill", y="tip", data=tips)
plt.title("Scatter Plot")
plt.show()

# Line Plot
sns.lineplot(x="total_bill", y="tip", data=tips)
plt.title("Line Plot")
plt.show()

# Bar Plot (Categorical Data)
sns.barplot(x="day", y="total_bill", data=tips)
plt.title("Bar Plot (Categorical Data)")
plt.show()

# Count Plot (Categorical Data)
sns.countplot(x="day", data=tips)
plt.title("Count Plot (Categorical Data)")
plt.show()

# Box Plot (Categorical Data)
sns.boxplot(x="day", y="total_bill", data=tips)
plt.title("Box Plot (Categorical Data)")
plt.show()

# Violin Plot (Categorical Data)
sns.violinplot(x="day", y="total_bill", data=tips)
plt.title("Violin Plot (Categorical Data)")
plt.show()

# Histogram (Distribution)
sns.histplot(x="total_bill", data=tips, kde=True)
plt.title("Histogram (Distribution)")
plt.show()

# Pair Plot (Multiple Variables)
sns.pairplot(tips, hue="sex")
plt.title("Pair Plot (Multiple Variables)")
plt.show()

# Heatmap (Correlation)
correlation_matrix = tips.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title("Heatmap (Correlation)")
plt.show()

# Joint Plot (Bivariate Distribution)
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
plt.title("Joint Plot (Bivariate Distribution)")
plt.show()

# Regression Plot (Linear Regression)
sns.regplot(x="total_bill", y="tip", data=tips)
plt.title("Regression Plot (Linear Regression)")
plt.show()

# Swarm Plot (Categorical Data)
sns.swarmplot(x="day", y="total_bill", data=tips)
plt.title("Swarm Plot (Categorical Data)")
plt.show()