import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset for a medical store
data = {
    'Medicine': ['Paracetamol', 'Amoxicillin', 'Ibuprofen', 'Cetirizine', 'Metformin'],
    'Category': ['Painkiller', 'Antibiotic', 'Painkiller', 'Antiallergic', 'Diabetes'],
    'Price': [10, 25, 15, 8, 30],
    'Stock': [100, 50, 70, 60, 40],
    'Sold': [40, 20, 50, 25, 35]
}

df = pd.DataFrame(data)

# Total revenue per medicine
df['Revenue'] = df['Price'] * df['Sold']

# Basic statistics
print(df.describe())

# Most sold medicines
top_sold = df.sort_values(by='Sold', ascending=False)
print("Top selling medicines:\n", top_sold[['Medicine', 'Sold']])

# Plot revenue per medicine
plt.figure(figsize=(8,4))
sns.barplot(x='Medicine', y='Revenue', data=df)
plt.title("Revenue per Medicine")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
