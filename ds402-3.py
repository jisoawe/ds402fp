#git+https://github.com/drvinceknight/Nashpy.git

from ast import Return
from re import X
import streamlit as st
#import nashpy as nash
import numpy as np


st.title('Price of Anarchy Implementation')
st.header('Jiso Awe & Thomas Schindler')
st.write('This is our interface for our Data Science 402 final project.')

"st.session_state object:", st.session_state

##clicked1 = st.button('1x1')


if st.button('2x2'):
    st.write('Type in your four desired payoffs')

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



elif st.button('3x3'):
    st.write('Type in your nine desired payoffs')

    Pa1 = int(input())
    Pa2 = int(input())
    Pa3 = int(input())
    Pa4 = int(input())
    Pa5 = int(input())
    Pa6 = int(input())
    Pa7 = int(input())
    Pa8 = int(input())
    Pa9 = int(input())

    Pb1 = int(input())
    Pb2 = int(input())
    Pb3 = int(input())
    Pb4 = int(input())
    Pb5 = int(input())
    Pb6 = int(input())
    Pb7 = int(input())
    Pb8 = int(input())
    Pb9 = int(input())

    Utility1 = Pa1 + Pb1
    Utility2 = Pa2 + Pb2
    Utility3 = Pa3 + Pb3
    Utility4 = Pa4 + Pb4
    Utility5 = Pa5 + Pb5
    Utility6 = Pa6 + Pb6
    Utility7 = Pa7 + Pb7
    Utility8 = Pa8 + Pb8
    Utility9 = Pa9 + Pb9

    payoffs = [Utility1, Utility2, Utility3, Utility4, Utility5, Utility6, Utility7,Utility9, Utility9]
    payoffs.sort()
    po = payoffs[3]


    A = np.array([[Pa1,Pa2,Pa3], [Pa4,Pa5,Pa6], [Pa7,Pa8,Pa9]])
    B = np.array([[Pb1,Pb2,Pb3], [Pb4,Pb5,Pb6], [Pb7,Pb8,Pb9]])
    rps = nash.Game(A,B)



'''
option = st.selectbox(
'What type of matrix would you like to test prisoners dilemma on?',
('1x1', '2x2', '3x3'))

st.write('You selected:', option)
'''

st.write(rps)

equilibrium = []

eqs = rps.support_enumeration()
for eq in eqs:
    x = list(eq)
    equilibrium.append(x)


length = len(equilibrium)

nashs = [9]

for i in equilibrium:
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
    nashs.append(f)

nashs.sort()
nashl = nashs[0]
poa = po/nashl
st.write(poa)
