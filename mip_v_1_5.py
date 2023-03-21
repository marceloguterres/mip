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
import time

        
# Dados básicos  streamlit
st.title('Projeto Impacto')



#=============================================================================
# funções
#=============================================================================

     
@st.cache_data
def load_matriz_nereus(ano_analise):
    n = matriz.Nereus(ano_analise)
    return n
        

#=============================================================================
# Configurção sidebar
#=============================================================================

with st.sidebar:
    
    st.title('MIP 1.5')
    st.sidebar.header('Seleção dos parâmetros') 
    ano_analise = st.text_input('Ano de Análise', '2015')
    name_utp    = st.text_input('Nome da UTP', 'São José dos Campos')


#=============================================================================


# Create a text element and let the reader know the data is loading
m = load_matriz_nereus(ano_analise)  # Load objeto matriz nereus para o ano de referencia


progress_text = "Carregando matriz nereus."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.050)
    my_bar.progress(percent_complete + 1, text=progress_text)








