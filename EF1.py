#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:23:27 2021

@author: Saadia Bayou
"""

import matplotlib.pyplot as plt
import numpy as np

# Détermination de l'équation discrétisée de la fonction dérivé (dx(t)/dt)=-x0sin(wt)


# méthode numérique

# Données - constantes  
x0=1
w=1

# Initialisations
t=list(range(10))
x=[]
print("t = ",t)

# fonction dérivée - (dx(t)/dt)=-x0sin(wt)
for tn in t: 
    xn=-x0*np.sin(w*tn)
    x.append(xn)
print("\nx=",x)
# fonction delta x et delta t
dx=np.zeros((len(x)-1))
dt=np.zeros((len(t)-1))

# Initialisation listes-tableaux de valeur des deltas 
# et de la fonction dérivée -> équation discrétisée ->  df= (dx/dt)
ldx=[]
ldt=[]
ldf=[]
# Boucle de calcul delta x 
for i in range(len(x)-1):
#    print("\nxi=",x[i])
    dx[i]=x[i+1]-x[i]
    x[i]=x[i+1]
    ldx.append(dx[i])
# Liste delta x     
print("\nldx=",ldx)

# Boucle de calcul delta t
for n in range(len(t)-1):
#    print("\ntn=",t[n])
    dt[n]=t[n+1]-t[n]
    t[n]=t[n+1]
    ldt.append(dt[n])
# Liste delta t
print("\nldt=",ldt)
# Boucle imbriquée -> calcul de la dérivée discrétisée df 
for dx in ldx :
    for dt in ldt :
        df=(dx/dt)
    ldf.append(df)

print("\nldf=",ldf)


# Graphe fonction dérivée discrétisée

# Tracé  de df en fonction de t
plt.plot(t[0:(len(t)-1)],ldf,marker=".",color="r",linestyle='')

plt.title("Méthode numérique - Equation discrétisée")

plt.xlabel("Temps(s) - tn")
plt.ylabel("Déplacement (mm) - df(tn) ")

plt.savefig("Methode_numérique.png")
plt.show()









