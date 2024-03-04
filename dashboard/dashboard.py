import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# Menyiapkan data df_day
df_day = pd.read_csv("dashboard\day.csv")
df_day.head()

# mengubah data cuaca 1,2,3,4
df_day['weathersit'] = df_day['weathersit'].map({
    1: 'cerah berawan',
    2: 'berawan',
    3: 'hujan',
    4: 'cuaca ekstrem'
})

# mengubah data season/musim 1,2,3,4
df_day['season'] = df_day['season'].map({
    1: 'Semi', 2: 'panas', 3: 'gugur', 4: 'dingin'
})

# dashboard

#  judul
st.header('Bike Rental Dashboard 🚲')