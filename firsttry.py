import streamlit as st

st.title('Price of Anarchy Implementation')
st.header('Jiso Awe & Thomas Schindler')
st.write('This is our interface for our Data Science 402 final project.')

if st.button('2x2'):
    st.write('Type in your four desired payoffs')

elif st.button('3x3'):
    st.write('Type in your nine desired payoffs')

else:
    st.write('lit')
