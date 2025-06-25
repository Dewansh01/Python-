#------------------------------------------------SEABORN----------------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.get_dataset_names()
df = sns.load_dataset('flights')
df


# Box plot
sns.barplot(x="year", y="passengers", data = df, color = 'black', label = 'Flight 01')
plt.grid()
plt.show()
plt.legend()
