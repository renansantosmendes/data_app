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
    files = os.listdir(data_root)
    files.sort()
    for i in files:
        print(i)
    data_list = [pd.read_csv(os.path.join(data_root, file_name), sep=';') for file_name in files]
    data = pd.concat(data_list[:], axis=0)
    data.head()
    dataframe = data[data['regiao'] == 'Brasil']['casosNovos']
    return dataframe


@st.experimental_singleton
def generate_dataset(dataframe):
    dataset = dataframe.values
    dataset = dataset.astype('float32')
    return dataset


@st.experimental_singleton
def generate_scaler(dataset):
    scaler = MinMaxScaler(feature_range=(0, 1))
    dataset = scaler.fit_transform([[i] for i in dataset])
    return scaler, dataset
