import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import database that includes stations for 3 different cites: Vancouver, Victoria and Prince George

df = pd.read_csv("climate_three_cities.csv")


# P is precipitation and Tm is Temperature Monthly Mean

trimmed = df.loc[:, ["Stn_Name", "Tm", "P", "Year", "Month", "Date"]]
saanichton = trimmed.loc[trimmed.Stn_Name == "SAANICHTON CDA",:]


# variable that represents the yearly average of monthly precipitation

saanichton_summer = saanichton.loc[(saanichton["Month"] > 5) & (saanichton["Month"] < 9)]
saanichton_summer["Summer_Precip"] = saanichton_summer.groupby("Year").P.transform('mean')
saanichton_trimmed = saanichton_summer[saanichton_summer["Month"] == 6]

print(saanichton_trimmed)

# regression function

d = np.polyfit(saanichton_trimmed['Year'],saanichton_trimmed["Summer_Precip"],1)
f = np.poly1d(d)
saanichton_trimmed.insert(6,'Regression Line',f(saanichton_trimmed['Year']))
ax = saanichton_trimmed.plot(x ='Year',y="Summer_Precip")
saanichton_trimmed.plot(x='Year', y='Regression Line',color='Red',ax=ax)

# saanichton_trimmed.plot(x='Year', y='Summer_Precip')

plt.title("'Summer Average' Precipitation in Saanichton, BC (1917-2017)")
plt.ylabel("June-July-August Mean Precipitation (mm)")


plt.show()

