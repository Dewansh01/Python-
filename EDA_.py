import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(df.head())
print(df.describe())

df.hist(figsize=(8, 6))
plt.suptitle("Feature Distributions")
plt.tight_layout()
plt.show()
