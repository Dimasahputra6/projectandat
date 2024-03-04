import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Menyiapkan data df_day
df_day = pd.read_csv("https://raw.githubusercontent.com/Dimasahputra6/projectandat/main/dashboard/day.csv")
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
st.header('Bike Rental Dashboard')

# Mengelompokkan data berdasarkan musim dan menghitung jumlah penggunaan terdaftar dan tidak terdaftar
seasonal_usage = df_day.groupby('season')[['registered', 'casual']].sum().reset_index()

with st.container():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Membuat bar plot
    ax.bar(
        seasonal_usage['season'],
        seasonal_usage['registered'],
        label='Registered',
        color='tab:red'
    )

    ax.bar(
        seasonal_usage['season'],
        seasonal_usage['casual'],
        label='Casual',
        color='tab:blue'
    )

    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.set_title('Jumlah penyewaan sepeda berdasarkan musim')
    ax.legend()

    st.pyplot(fig)


# Set Streamlit configuration option to suppress the warning
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.container():
    # Set up the figure
    fig, axes = plt.subplots(1, 3, figsize=(14, 6))

    # Scatter plot for 'temp' vs 'count'
    sns.scatterplot(
        x='temp',
        y='cnt',
        data=df_day,
        alpha=0.5,
        ax=axes[0]
    )
    axes[0].set_title('Temperature vs jumlah pengguna')

    # Scatter plot for 'atemp' vs 'count'
    sns.scatterplot(
        x='atemp',
        y='cnt',
        data=df_day,
        alpha=0.5,
        ax=axes[1]
    )
    axes[1].set_title('atemp vs jumlah pengguna')

    # Scatter plot for 'hum' vs 'count'
    sns.scatterplot(
        x='hum',
        y='cnt',
        data=df_day,
        alpha=0.5,
        ax=axes[2]
    )
    axes[2].set_title('Humidity/kelembaban vs jumlah pengguna')

    # Show the plot
    st.pyplot(fig)