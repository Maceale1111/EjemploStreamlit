# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

#Prueba git commit . -m "Comentario" // git push
#from datetime import time
#import datetime

# -*- coding: utf-8 -*-
st.title('Mi primer proyecto de ciencia de datos')
st.write('Hola como estás')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.dataframe(df.head(15))
st.map(df)

#num=st.slider(label = 'num',min_value=0,max_value=100,step =5, disabled=False)
#st.write('El número seleccionado es {}'.format(num))

#appointment=st.slider(label='Programe horario de asesoria',
#                      value=(time(11,30), time(12,45)))
#st.write('Está agendado para:',appointment)

#d=st.date_input('Fecha de cumpleaños', datetime.date(2019,7,6))
#st.write('Tu cumpleaños es:',d)

#option=st.selectbox('Como desearia ser contactado(a)?',('Email','Telefono','Whatsapp','X'))
#st. write('Usted seleccionó la opción:', option)

#n = st.slider("n", 5, 100, step=1)
#chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
#st.line_chart(chart_data)


