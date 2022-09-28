import streamlit as st
import pandas as pd
import numpy as np

folder = "F:/Google Drive/Proyectos/UCongreso - Profesorado para profesionales/Primer semestre/Instituciones Educativas/Para presentaciones grupales/Participación/"

df = pd.read_excel(folder + 'escuelas-coordenadas-agosto-2018.xlsx')

st.header('Escuelas')

df = df.query("departamento == 'SAN RAFAEL'")
df = df[['lat','lon']]
#print(df.head())
st.map(df)
