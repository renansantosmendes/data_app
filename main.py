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
# st.line_chart(dataframe)

start_date = st.date_input('Start date', today)
print(type(start_date))
print(start_date.strftime("%Y-%m-%d"))

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')


def read_image(name='image'):
  image = st.file_uploader("Upload an "+ name, type=["png", "jpg", "jpeg"])
  if image:
    im = Image.open(image)
    im.filename = image.name
    return im



with st.sidebar.form("Input"):
     read_image()
     queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
     btnResult = st.form_submit_button('Run')

if btnResult:
    st.sidebar.text('Button pushed')

    # run query
    st.write(queryText)

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

# col1.subheader("A wide column with a chart")
# col1.line_chart(dataframe)
#
# col2.subheader("A narrow column with the data")
# col2.write(data)



df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)

col1.subheader("Chart")
col1.line_chart(dataframe)

col2.subheader("MAP")
col2.map(df)