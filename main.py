import os
import datetime
import pandas as pd
import numpy as np
import streamlit as st

today = datetime.date.today()
data = pd.read_csv('C:\\Datasets\\time_series.csv')
root = 'C:\\PUC\\datasets\\timeserie_covid'
covid_data = pd.read_csv(os.path.join(root, 'HIST_PAINEL_COVIDBR_2020_Parte1_19ago2022.csv'), sep=';')

dataframe = covid_data[covid_data['regiao'] == 'Brasil']['casosNovos']



st.title('Data Application: COVID-19')

print(data.head())
# st.line_chart(data.iloc[:,1])
st.line_chart(dataframe)

start_date = st.date_input('Start date', today)
print(type(start_date))
print(start_date.strftime("%Y-%m-%d"))

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')


df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)