import streamlit as st

st.title('Price of Anarchy Implementation')
st.header('Jiso Awe & Thomas Schindler')
st.write('This is our interface for our Data Science 402 final project.')

option = st.selectbox(
'What type of matrix would you like to test prisoners dilemma on?',
('1x1', '2x2'))

st.write('You selected:', option)
