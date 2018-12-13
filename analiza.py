import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
dane=pd.read_csv("state_crime.csv")
print(dane.head(0))

##pytanie 1
pojazdy=pd.Series(dane["Rates.Property.Motor"])
wlamania=pd.Series(dane["Rates.Property.Burglary"])
#print(st.pearsonr(pojazdy, wlamania))

##pytanie2
okrutne_morderstwa=pd.Series(dane["Rates.Violent.Murder"])
ludzie=pd.Series(dane["Population"])
#print(st.pearsonr(okrutne_morderstwa, ludzie))


##pytanie4
gwalty=pd.Series(dane["Rates.Violent.Rape"])
#print(st.pearsonr(okrutne_morderstwa, gwalty))

##pytanie 3

morderstwa_total=dane["Totals.Violent.Murder"]

stany=['Alabama', 'Alaska', 'Arizona','Arkansas','California','Colorado', 'Connecticut','Delaware',
'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

srednie_morderst_dla_stanow=[]

for i in stany:
    srednia=morderstwa_total[dane.State==i].mean()
    srednie_morderst_dla_stanow.append(srednia)


series=pd.Series(srednie_morderst_dla_stanow, stany)

top5UlubionychImprez = series.nlargest(n=5, keep='first')

#print(series)
print(top5UlubionychImprez)
zmienna=['California', 'Texas', 'New York', 'Florida', 'Illlinois']
plt.bar(zmienna, top5UlubionychImprez, color='lightskyblue', label='gdzie najwiecej morderstw') ##wykres##
plt.xlabel("Nazwa Stanu")
plt.ylabel("Średnia liczba morderstw")
plt.show()

##Średnia liczba przestępstw i liczebność stanu - texas, ohaio, columbia.

##pytanie 5 ?
dane['wszystkiePrzest']= dane["Rates.Property.All"] + dane["Rates.Violent.All"]
sredniaProperty=pd.Series(dane["Rates.Property.All"])
sredniaViolent=pd.Series(dane["Rates.Violent.All"])
print(dane['wszystkiePrzest'])
print(st.pearsonr(dane['wszystkiePrzest'], ludzie))
print(st.pearsonr(sredniaProperty, ludzie))
#print(st.pearsonr(sredniaViolent, ludzie))

##pytanie 6 i 7

zmiennaBurg=dane["Totals.Property.Burglary"]

TPburglary=dane.loc[dane["State"] == "United States", "Totals.Property.Burglary"]
TPlarceny=dane.loc[dane["State"] == "United States", "Totals.Property.Larceny"]
TPmotor=dane.loc[dane["State"] == "United States", "Totals.Property.Motor"]
TVassault=dane.loc[dane["State"] == "United States", "Totals.Violent.Assault"]
TVmurder=dane.loc[dane["State"] == "United States", "Totals.Violent.Murder"]
TVrape=dane.loc[dane["State"] == "United States", "Totals.Violent.Rape"]
TVrobbery=dane.loc[dane["State"] == "United States", "Totals.Violent.Robbery"]

p1=TPburglary.sum()
p2=TPlarceny.sum()
p3=TPmotor.sum()
property=[p1, p2, p3]
podpisy1=['Burglary', 'Larceny', 'Motor']

v1=TVassault.sum()
v2=TVmurder.sum()
v3=TVrape.sum()
v4=TVrobbery.sum()
violent=[v1, v2, v3, v4]
podpisy2=['Assault', 'Murder', 'Rape', 'Robbery']
colors = ['yellowgreen', 'lightskyblue', 'lightcoral', 'gold']

##wykresik 1 kółeczko
plt.figure(1, figsize=(6,6))
plt.pie(property, labels=podpisy1, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()

colors = ['lightskyblue', 'gold', 'lightcoral', 'yellowgreen']
#wykresik 2 kółeczko
plt.figure(1, figsize=(6,6))
plt.pie(violent, labels=podpisy2, colors=colors, autopct='%1.1f%%', shadow=True)
plt.show()

##pytanie 5 ?????????
