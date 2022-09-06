import datetime
import numpy as np
import pandas as pd
import streamlit as st

from utils import read_models, read_time_serie_data

today = datetime.date.today()

dataframe = read_time_serie_data()

cnn_model, time_serie_model = read_models('.\models',
                                          'cnn_model.h5',
                                          'covid_time_serie_model.h5')

st.title('Data Application: COVID-19')


days_to_predict = st.slider('Days to predict', 0, 60, 0)
st.write(f'Days to predict {days_to_predict}')

start_day = st.slider('Start Day', 0, dataframe.shape[0], 0)
st.write(f'Start Day {start_day}')

end_day = st.slider('End Day', start_day, dataframe.shape[0], 0)
st.write(f'End Day {end_day}')

st.line_chart(dataframe.values.tolist()[start_day:end_day])


def read_image(name='image'):
  image = st.file_uploader("Upload an " + name, type=["png", "jpg", "jpeg"])
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
    st.write(queryText)

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])

st.map(df)

# col1.subheader("Chart")


start_date = st.date_input('Start date', today)
print(type(start_date))
print(start_date.strftime("%Y-%m-%d"))

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')



col2.subheader("MAP")
col2.map(df)