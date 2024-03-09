import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

##depurar un poco la base de datos
pinguinos = pd.read_csv("penguins.csv")
pinguinos.drop(['rowid','Unnamed: 9','Unnamed: 10','Unnamed: 11'],axis=1,inplace=True)

##eliminando NaN
pinguinos=pinguinos.dropna()
print(pinguinos.to_string())

##conteo de variables importantes
especies = pinguinos['species'].value_counts()
islas = pinguinos['island'].value_counts()
print(especies)
print(islas)

##grafica especies y islas
fig, axes = plt.subplots(1,2)
fig.suptitle("grafico especies y islas")
sns.countplot(ax=axes[0],data=pinguinos,hue='species',x='species',palette='Set1')
sns.countplot(ax=axes[1],data=pinguinos,hue='island',x='island',palette='Set2')
plt.show()

##separacion de datos por islas #####################################################################
islas = pinguinos.groupby(pinguinos.island)
isla1 = islas.get_group('Biscoe')
isla2 = islas.get_group('Dream')
isla3 = islas.get_group('Torgersen')

fig1, axes = plt.subplots(1,3)
fig1.suptitle("Cantidad de especies por isla")
sns.countplot(ax=axes[0],data=isla1,hue='species',x='species',palette='Set1',legend='auto').set_xlabel("Biscoes")
sns.countplot(ax=axes[1],data=isla2,hue='species',x='species',palette='Set1',legend='auto').set_xlabel("Dream")
sns.countplot(ax=axes[2],data=isla3,hue='species',x='species',palette='Set1',legend='auto').set_xlabel("Torgersen")
plt.show()

print('isla1:',isla1['species'].value_counts(),sep="\n")
print('isla2:',isla2['species'].value_counts(),sep="\n")
print('isla3:',isla3['species'].value_counts(),sep="\n")

##poblacion de machos y hembras en cada isla

##Biscoes
especxisla = pinguinos.groupby(isla1.species)
isla1_espe1=especxisla.get_group('Adelie')
isla1_espe2=especxisla.get_group('Gentoo')

fig1, axes = plt.subplots(1,2)
fig1.suptitle("Biscoes genero")
sns.countplot(ax=axes[0],data=isla1_espe1,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Adelie")
sns.countplot(ax=axes[1],data=isla1_espe2,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Gentoo")
plt.show()

##Dream
especxisla = pinguinos.groupby(isla2.species)
isla2_espe1=especxisla.get_group('Adelie')
isla2_espe3=especxisla.get_group('Chinstrap')

fig1, axes = plt.subplots(1,2)
fig1.suptitle("Dream genero")
sns.countplot(ax=axes[0],data=isla2_espe1,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Adelie")
sns.countplot(ax=axes[1],data=isla2_espe3,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Chinstrap")
plt.show()


##Torgersen
especxisla = pinguinos.groupby(isla3.species)
isla3_espe1=especxisla.get_group('Adelie')

fig1 = plt.figure(figsize=(8,6))
fig1.suptitle("Torgersen genero")
sns.countplot(data=isla3_espe1,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Adelie")
plt.show()

#################################################################################################
##separacion por especies
pings = pinguinos.groupby(pinguinos.species)
pin1 = pings.get_group('Adelie')
pin2 = pings.get_group('Gentoo')
pin3 = pings.get_group('Chinstrap')

fig, axes = plt.subplots(1,3)
sns.countplot(ax=axes[0],data=pin1,hue='island',x='island',palette='Set1',legend='auto').set_xlabel("Adelie")
sns.countplot(ax=axes[1],data=pin2,hue='island',x='island',palette='Set1',legend='auto').set_xlabel("Gentoo")
sns.countplot(ax=axes[2],data=pin3,hue='island',x='island',palette='Set1',legend='auto').set_xlabel("Chinstrap")

print('Adelie:',pin1['island'].value_counts(),sep="\n")
print('Gento:',pin2['island'].value_counts(),sep="\n")
print('Chinstrap:',pin3['island'].value_counts(),sep="\n")

#Generos de cada especie 

##especie Adelie
islaxespecie = pinguinos.groupby(pin1.island)
especie1_isla1=islaxespecie.get_group('Torgersen')
especie1_isla2=islaxespecie.get_group('Biscoe')
especie1_isla3=islaxespecie.get_group('Dream')


fig1, axes = plt.subplots(1,3)
fig1.suptitle("Biscoes genero tres islas")
sns.countplot(ax=axes[0],data=especie1_isla1,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Torgersen")
sns.countplot(ax=axes[1],data=especie1_isla2,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Biscoe")
sns.countplot(ax=axes[2],data=especie1_isla3,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Dream")
plt.show()

##especie Gentoo
islaxespecie = pinguinos.groupby(pin2.island)
especie2_isla2=islaxespecie.get_group('Biscoe')


fig1 = plt.figure(figsize=(8,6))
fig1.suptitle("Gentoo genero isla Biscoe")
sns.countplot(data=especie2_isla2,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Gentoo")
plt.show()

##especie Chinstrap
islaxespecie = pinguinos.groupby(pin3.island)
especie3_isla3=islaxespecie.get_group('Dream')


fig1 = plt.figure(figsize=(8,6))
fig1.suptitle("Chinstrap genero isla Dream")
sns.countplot(data=especie3_isla3,hue='sex',x='sex',palette='Set1',legend='auto').set_xlabel("Chinstrap")
plt.show()

###################################################################################################
##grafica valores mas importantes
plt.figure(figsize=(6,4))
sns.heatmap(pinguinos.corr(),annot=True,cmap="Reds")
plt.show()

##densidad poblacional por año
plt.figure(figsize=(8,6))
sns.kdeplot(data=pinguinos, x="year", hue="species")
#pinguinos.describe()

###eliminando el año
pinguinos.drop('year',axis=1,inplace=True)

##grafica valores mas importantes
plt.figure(figsize=(6,4))
sns.heatmap(pinguinos.corr(),annot=True,cmap="Reds")
plt.show()

##densidad poblacional por año
plt.figure(figsize=(8,6))
sns.kdeplot(data=pinguinos, x="year", hue="species")


####################################################################################################
#Propiedades de especies
fig1, axes = plt.subplots(2,2)
fig1.suptitle('Porpiedades de Especies ')
sns.boxplot(ax=axes[0,0],x='species',y='bill_length_mm',data=pinguinos,hue='species')
sns.boxplot(ax=axes[0,1],x='species',y='bill_depth_mm',data=pinguinos,hue='species')
sns.boxplot(ax=axes[1,0],x='species',y='flipper_length_mm',data=pinguinos,hue='species')
sns.boxplot(ax=axes[1,1],x='species',y='body_mass_g',data=pinguinos,hue='species')
plt.show()

#cada propiedad
fig1, axes = plt.subplots(1,2)
fig1.suptitle('bill_length_mm ')
sns.histplot(ax=axes[0],data=pinguinos,x='species',y='bill_length_mm',bins=20)
sns.violinplot(ax=axes[1],x='bill_length_mm',y='species',data=pinguinos, hue='species')
plt.show()


fig1, axes = plt.subplots(1,2)
fig1.suptitle('bill_depth_mm')
sns.histplot(ax=axes[0],data=pinguinos,x='species',y='bill_depth_mm',bins=20)
sns.violinplot(ax=axes[1],x='bill_depth_mm',y='species',data=pinguinos, hue='species')
plt.show()

fig1, axes = plt.subplots(1,2)
fig1.suptitle('flipper_length_mm')
sns.histplot(ax=axes[0],data=pinguinos,x='species',y='flipper_length_mm',bins=20)
sns.violinplot(ax=axes[1],x='flipper_length_mm',y='species',data=pinguinos, hue='species')
plt.show()

fig1, axes = plt.subplots(1,2)
fig1.suptitle('body_mass_g')
sns.histplot(ax=axes[0],data=pinguinos,x='species',y='body_mass_g',bins=20)
sns.violinplot(ax=axes[1],x='body_mass_g',y='species',data=pinguinos, hue='species')
plt.show()

#################################################################################################
#propiedades por isla
fig1, axes = plt.subplots(2,2)
fig1.suptitle('Porpiedades de isla ')
sns.boxplot(ax=axes[0,0],x='island',y='bill_length_mm',data=pinguinos,hue='island')
sns.boxplot(ax=axes[0,1],x='island',y='bill_depth_mm',data=pinguinos,hue='island')
sns.boxplot(ax=axes[1,0],x='island',y='flipper_length_mm',data=pinguinos,hue='island')
sns.boxplot(ax=axes[1,1],x='island',y='body_mass_g',data=pinguinos,hue='island')
plt.show()

##propiedas de cada isla
fig1, axes = plt.subplots(1,2)
fig1.suptitle('bill_length_mm ')
sns.histplot(ax=axes[0],data=pinguinos,x='species',y='bill_length_mm',bins=20)
sns.violinplot(ax=axes[1],x='bill_length_mm',y='island',data=pinguinos, hue='island')
plt.show()

fig1, axes = plt.subplots(1,2)
fig1.suptitle('bill_depth_mm')
sns.histplot(ax=axes[0],data=pinguinos,x='species',y='bill_depth_mm',bins=20)
sns.violinplot(ax=axes[1],x='bill_depth_mm',y='island',data=pinguinos, hue='island')
plt.show()

fig1, axes = plt.subplots(1,2)
fig1.suptitle('flipper_length_mm')
sns.histplot(ax=axes[0],data=pinguinos,x='island',y='flipper_length_mm',bins=20)
sns.violinplot(ax=axes[1],x='flipper_length_mm',y='island',data=pinguinos, hue='island')
plt.show()

fig1, axes = plt.subplots(1,2)
fig1.suptitle('body_mass_g')
sns.histplot(ax=axes[0],data=pinguinos,x='island',y='body_mass_g',bins=20)
sns.violinplot(ax=axes[1],x='body_mass_g',y='island',data=pinguinos, hue='island')
plt.show()