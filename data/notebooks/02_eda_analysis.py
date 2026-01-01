import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/ENB2012_data.csv")

df.head()

# Basic statistics
df.describe()
# Rename columns
df.columns = [
    "Relative_Compactness", "Surface_Area", "Wall_Area",
    "Roof_Area", "Overall_Height", "Orientation",
    "Glazing_Area", "Glazing_Distribution",
    "Heating_Load", "Cooling_Load"
]
print('Missing values per column:')
print(df.isnull().sum())

# Based on common interpretations of the ENB2012 dataset:
# X1: Relative Compactness
# X2: Surface Area
# X3: Wall Area
# X4: Roof Area
# X5: Overall Height
# X6: Orientation
# X7: Glazing Area
# X8: Glazing Area Distribution
# Y1: Heating Load
# Y2: Cooling Load
 
# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
