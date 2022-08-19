import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import database that includes stations for 3 different cites: Vancouver, Victoria and Prince George

df = pd.read_csv("climate_three_cities.csv")

# Tx is Temperature Maximum is precipitation and Tm is Temperature Monthly Mean

trimmed = df.loc[:, ["Stn_Name", "Tm", "Tx", "Year","Month","Date"]]

saanichton = trimmed.loc[trimmed.Stn_Name == "SAANICHTON CDA",:]

# variable that represents the yearly average of monthly precipitation
# P is the column

saanichton_summer = saanichton.loc[(saanichton["Month"] > 5) & (saanichton["Month"] < 9)]

saanichton_summer["Max_Temp"] = saanichton_summer.groupby("Year").Tx.transform('max')
saanichton_summer["Mean_Temp"] = saanichton_summer.groupby("Year").Tm.transform('mean')

saanichton_trimmed = saanichton_summer[saanichton_summer["Month"] == 6]

print(saanichton_trimmed)

# # regression function
#
d = np.polyfit(saanichton_trimmed['Year'],saanichton_trimmed["Mean_Temp"],1)
f = np.poly1d(d)
saanichton_trimmed.insert(6,'Regression Line',f(saanichton_trimmed['Year']))
ax = saanichton_trimmed.plot(x ='Year',y="Mean_Temp")
saanichton_trimmed.plot(x='Year', y='Regression Line',color='Red',ax=ax)
#
# ax_1 = saanichton_trimmed.plot(x='Year', y='Max_Temp')
# saanichton_trimmed.plot(x='Year', y='Mean_Temp', ax=ax_1)


# plt.title("'Summer Average' Precipitation in Saanichton, BC (1917-2017)")
# plt.ylabel("June-July-August Mean Precipitation (mm)")
#
#
plt.show()

