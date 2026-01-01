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
# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
