import pandas as pd

# Load the Excel file
df = pd.read_excel('testData.xlsx')

# Select indices where 'Year' is greater than 2022
indices = df.index[df["Year"] > 2022].tolist()

print(indices)
