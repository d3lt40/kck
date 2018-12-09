import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
dane=pd.read_csv("state_crime.csv")
print(dane.head(0))
pojazdy=pd.Series(dane["Rates.Property.Motor"])
wlamania=pd.Series(dane["Rates.Property.Burglary"])
#print(st.pearsonr(pojazdy, wlamania))

okrutne_morderstwa=pd.Series(dane["Rates.Violent.Murder"])
ludzie=pd.Series(dane["Population"])
#print(st.pearsonr(okrutne_morderstwa, ludzie))

gwalty=pd.Series(dane["Rates.Violent.Rape"])
#print(st.pearsonr(okrutne_morderstwa, gwalty))



morderstwa_total=dane["Totals.Violent.Murder"]

stany=['Alabama', 'Alaska', 'Arizona','Arkansas','California','Colorado', 'Connecticut','Delaware',
'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
'New Jersey', 'New Mexico', 'New York', 'North Carolina']
srednie_morderst_dla_stanow=[]

for i in stany:
    srednia=morderstwa_total[dane.State==i].mean()
    srednie_morderst_dla_stanow.append(srednia)


series=pd.Series(srednie_morderst_dla_stanow, stany)

top5UlubionychImprez = series.nlargest(n=5, keep='first')

#print(series)
print(top5UlubionychImprez)
zmienna=['California', 'New York', 'Florida', 'Illlinois', 'Michigan']
plt.bar(zmienna, top5UlubionychImprez, color='b', label='gdzie najwiecej morderstw') ##wykres##
plt.xlabel("Nazwa Stanu")
plt.ylabel("Średnia liczba morderstw")
plt.show()

##Średnia liczba przestępstw i liczebność stanu - texas, ohaio, columbia.

#Suma każdej kolumny, policzyć procenty – macierz do wykresu kolowego.
