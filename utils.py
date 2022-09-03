import os
import pandas as pd
import streamlit as st
import tensorflow as tf
from tensorflow import keras


@st.experimental_singleton
def read_models(root: str,
                cnn_model_file: str,
                time_serie_model_file: str):

    # cnn_model = tf.keras.models.load_model(os.path.join(root,
    #                                              cnn_model_file))
    cnn_model = ''
    time_serie_model = tf.keras.models.load_model(os.path.join(root,
                                                        time_serie_model_file))

    return cnn_model, time_serie_model


@st.experimental_singleton
def read_time_serie_data():
    data_root = 'C:\\PUC\\datasets\\timeserie_covid'
    covid_data = pd.read_csv(os.path.join(data_root,
                                          'HIST_PAINEL_COVIDBR_2020_Parte1_19ago2022.csv'),
                             sep=';')
    dataframe = covid_data[covid_data['regiao'] == 'Brasil']['casosNovos']
    return dataframe
