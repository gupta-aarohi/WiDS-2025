import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/ENB2012_data.csv")

EMISSION_FACTOR = 0.82  # kg CO2 per kWh

df["CO2_Emissions_kg"] = df["Heating_Load"] * EMISSION_FACTOR

df.head()

plt.scatter(df["Heating_Load"], df["CO2_Emissions_kg"])
plt.xlabel("Heating Load")
plt.ylabel("CO2 Emissions (kg)")
plt.title("CO2 Emissions vs Heating Load")
plt.show()
