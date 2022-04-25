from ast import Return
from re import X
import nashpy as nash
import numpy as np


Pa1 = int(input())
Pa2 = int(input())
Pa3 = int(input())
Pa4 = int(input())

Pb1 = int(input())
Pb2 = int(input())
Pb3 = int(input())
Pb4 = int(input())

Utility1 = Pa1 + Pb1
Utility2 = Pa2 + Pb2
Utility3 = Pa3 + Pb3
Utility4 = Pa4 + Pb4

payoffs = [Utility1, Utility2, Utility3, Utility4]
payoffs.sort()
po = payoffs[3]


A = np.array([[Pa1,Pa2], [Pa3,Pa4]])
B = np.array([[Pb1,Pb2], [Pb3,Pb4]])
rps = nash.Game(A,B)


equilibrium = []

eqs = rps.support_enumeration()
for eq in eqs:
    x = list(eq)
    equilibrium.append(x)


length = len(equilibrium)

if length == 1:
    equil = equilibrium[0]
    length1 = len(equil)
    middle_index = length1 // 2
    playerA = equil[:middle_index]
    playerB = equil[middle_index:]

    a = (playerA[0])
    b = (playerB[0])
    sigma_r = np.array(a)
    sigma_c = np.array(b)
    pd = nash.Game(A,B)
    c = (pd[sigma_r, sigma_c])

    d = c[0]
    e = c[1]
    f = d + e

    poa = po / f
    print("The prive of anarchy is", poa)


if length == 2:
    middle_index = length // 2
    equilibrium1 = equilibrium[:middle_index]
    equilibrium2 = equilibrium[middle_index:]   

    equil = equilibrium1[0]
    length1 = len(equil)
    middle_index1 = length1 // 2
    playerA = equil[:middle_index1]
    playerB = equil[middle_index1:]

    a = (playerA[0])
    b = (playerB[0])
    sigma_r = np.array(a)
    sigma_c = np.array(b)
    pd = nash.Game(A,B)
    c = (pd[sigma_r, sigma_c])

    d = c[0]
    e = c[1]
    f = d + e
    
    equil1 = equilibrium2[0]
    length2 = len(equil1)
    middle_index2 = length2 // 2
    playerC = equil[:middle_index2]
    playerD = equil[middle_index2:]

    g = (playerC[0])
    h = (playerD[0])
    sigma_g = np.array(g)
    sigma_h = np.array(g)
    pd = nash.Game(A,B)
    i = (pd[sigma_r, sigma_c])

    j = i[0]
    k = i[1]
    l = j + k

    if l > f:
        poa = po / f
        print("The prive of anarchy is", poa)
    
    if f > l:
        poa = po / l
        print("The prive of anarchy is", poa)

    else:
        poa = po/f
        print("The prive of anarchy is", poa)

if length == 3:
    equilibrium.pop()
    middle_index = length // 2
    equilibrium1 = equilibrium[:middle_index]
    equilibrium2 = equilibrium[middle_index:]   

    equil = equilibrium1[0]
    length1 = len(equil)
    middle_index1 = length1 // 2
    playerA = equil[:middle_index1]
    playerB = equil[middle_index1:]

    a = (playerA[0])
    b = (playerB[0])
    sigma_r = np.array(a)
    sigma_c = np.array(b)
    pd = nash.Game(A,B)
    c = (pd[sigma_r, sigma_c])

    d = c[0]
    e = c[1]
    f = d + e
    
    equil1 = equilibrium2[0]
    length2 = len(equil1)
    middle_index2 = length2 // 2
    playerC = equil[:middle_index2]
    playerD = equil[middle_index2:]

    g = (playerC[0])
    h = (playerD[0])
    sigma_g = np.array(g)
    sigma_h = np.array(g)
    pd = nash.Game(A,B)
    i = (pd[sigma_r, sigma_c])

    j = i[0]
    k = i[1]
    l = j + k
    print(l)
    print(f)

    if l > f:
        poa = po / f
        print("The prive of anarchy is", poa)
    
    if f > l:
        poa = po / l
        print("The prive of anarchy is", poa)

    else:
        poa = po/f
        print("The prive of anarchy is", poa)

    