import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import database that includes stations for 3 different cites: Vancouver, Victoria and Prince George

df = pd.read_csv("climate_three_cities.csv")

# P is precipitation and Tm is Temperature Monthly Mean

trimmed = df.loc[:, ["Stn_Name", "Tm", "P", "Year","Month","Date"]]

# some cities are missing temperature and precipitation data. This line of code filters out
# by_year = trimmed.loc[(trimmed.Year >= 1957) & (trimmed.Year <= 2017). Saanichton has the fewest null values and
# a complete dataset from 1917 onwards

saanichton = trimmed.loc[trimmed.Stn_Name == "SAANICHTON CDA",:]

# variable that represents the yearly average of monthly precipitation
# P is the column

saanichton["Yearly_Precip"] = saanichton.groupby("Year").P.transform('sum')


# # regression function
d = np.polyfit(saanichton['Year'],saanichton["Yearly_Precip"],1)
f = np.poly1d(d)


saanichton.insert(6,'Regression Line',f(saanichton['Year']))

ax = saanichton.plot(x ='Year',y="Yearly_Precip")
saanichton.plot(x='Year', y='Regression Line',color='Red',ax=ax)

plt.title("Yearly Precipitation in Saanichton, BC (1917-2017)")
plt.ylabel("Yearly Precipitation (mm)")


plt.show()

