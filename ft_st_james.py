import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("BC_data.csv")

# new year/month column to facilitate sorting and check consistencies


df["Date"] = pd.to_datetime(df[['Year', 'Month']].assign(Day=1))
st_james = df[df["Stn_Name"] == "FORT ST JAMES"]
st_james_trimmed = st_james.loc[:, ["Stn_Name", "Tx", "Tm", "Year","Month","Date"]]
st_james_trimmed["Mean_Temp"] = st_james_trimmed.groupby("Year").Tm.transform('mean')

# regression function


d = np.polyfit(st_james_trimmed['Year'],st_james_trimmed["Mean_Temp"],1)
f = np.poly1d(d)
st_james_trimmed.insert(6,'Regression Line',f(st_james_trimmed['Year']))
ax = st_james_trimmed.plot(x ='Year',y="Mean_Temp")
st_james_trimmed.plot(x='Year', y='Regression Line',color='Red',ax=ax)

plt.title("Mean Temperature in St James, BC (1917-2017)")
plt.ylabel("Annual Mean Temperature (C)")

ax.get_legend().remove()
plt.show()


