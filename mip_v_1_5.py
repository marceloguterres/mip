# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#-----------------------------------------------------------------------------------
# Bibliotecas Python
import streamlit as st


# Bibliotecas Impacto
import matriz # carrega módulo matriz



# Dados básicos  streamlit
st.title('MIP 1.5')


# inputs

@st.cache_data
def load_matriz_nereus(ano_analise):
    n = matriz.Nereus(ano_analise) 
    return n

# Create a text element and let the reader know the data is loading
data_load_state = st.text('Loading matriz nereus')
# Load objeto matriz nereus para o ano de referencia
load_matriz_nereus(ano_analise = 2015)
data_load_state.text('Loading data...done!')

