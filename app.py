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
logo = "logo.png"

# sidebar
st.sidebar.image(logo, width=200)


# konten
st.subheader("Data Preview")
st.dataframe(df.head(100))


# distribusi negara asal 
st.subheader("Distribusi negara asal")

country_counts = df["country"].value_counts().head(10)
fig1, ax1 = plt.subplots()
country_counts.plot(kind='bar', ax=ax1)

st.pyplot(fig1)


# tren tahun film release
st.subheader("Tren tahun release")
year_tren = df.groupby("release_year").size()
fig2, ax2 = plt.subplots()
year_tren.plot(kind='line', ax=ax2)

st.pyplot(fig2)

# distribusi tipe
st.subheader("Distribusi tipe film")

type_counts = df["type"].value_counts()
fig3, ax3 = plt.subplots()
type_counts.plot(kind="pie", autopct="%1.2f")
st.pyplot(fig3)
