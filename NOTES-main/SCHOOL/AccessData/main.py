import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("elec_access_data.csv",header = 0)

ourCountries=["Greenland","Jamaica","Canada","Cuba","Panama"]


uniqueCountries = df.Entity.unique()

for c in uniqueCountries:
    if c in ourCountries:
        years = df[df["Entity"]==c]['Year']
        elecAccess = df[df["Entity"]==c]['Access']
        

        plt.plot(years,elecAccess,label=c)


plt.ylabel("% of Country Population")
plt.xlabel("Years")
plt.title("% of Population with Electricity Access")
plt.legend()
plt.show()