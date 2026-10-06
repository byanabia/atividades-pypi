import streamlit as st

# Line 1: slider para escolher o valor de x
x = st.slider("Selecione um valor")

# Line 2: exibe o texto e o resultado do quadrado de x
st.write(x, "o quadrado é", x * x)