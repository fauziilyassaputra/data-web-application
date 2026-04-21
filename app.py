import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# load data
def load_data():
    df = pd.read_csv("netflix.csv")
    df = df.dropna()
    return df

df = load_data()



# title
st.write("analisis dashboard netflix")

# logo


# sidebar


# konten
st.subheader("Data Preview")


# distribusi negara asal 
st.subheader("Distribusi negara asal")


# tren tahun film release
st.subheader("Tren tahun release")


# distribusi tipe
st.subheader("Distribusi tipe film")

