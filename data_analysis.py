import pandas as pd

# Load the dataset (replace with the actual file path)
df = pd.read_csv('sales_data.csv')

# Display basic info about the dataset
print(df.head())
print(df.info())