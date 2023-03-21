#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 20:34:02 2023

@author: guterres
"""
# carrega módulo matriz
import matriz


ano_analise = '2016'
name_utp  = 'São José dos Campos'
 
 
 
# baixa dados na S3, constroi objeto Nereus e carrega na variável n
# dados disponíveis somente para 2015 por enquanto
n = matriz.Nereus(2017)
m = n.extrair_mipita()



tab_utp = m.utp[m.utp['Nome']== name_utp]


