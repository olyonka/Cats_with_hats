import seaborn as sns

# Load the dataset
tips = sns.load_dataset("tips")

# Scatterplot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Lineplot
sns.lineplot(x="total_bill", y="tip", data=tips)

# Barplot
sns.barplot(x="day", y="total_bill", data=tips)

# Countplot
sns.countplot(x="day", data=tips)

# Boxplot
sns.boxplot(x="day", y="total_bill", data=tips)

# Violinplot
sns.violinplot(x="day", y="total_bill", data=tips)

# Stripplot
sns.stripplot(x="day", y="total_bill", data=tips)

# Swarmplot
sns.swarmplot(x="day", y="total_bill", data=tips)

# Pairplot
sns.pairplot(tips)

# Heatmap
sns.heatmap(tips.corr(), annot=True)

# Distplot
sns.distplot(tips["total_bill"])

# KDEplot
sns.kdeplot(tips["total_bill"])