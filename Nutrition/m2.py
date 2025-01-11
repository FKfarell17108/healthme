import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data nutrisi makanan dari file Excel
@st.cache
def load_data():
    data = pd.read_excel('nutrisi_makanan.xlsx')
    return data

# Menyiapkan fitur dan target untuk model
def prepare_data(data):
    X = data[['Protein (g)', 'Lemak (g)', 'Karbohidrat (g)', 'Serat (g)', 'Gula (g)']]  # Fitur
    y = data['Kalori (kcal)']  # Target (kalori)
    return X, y

# Membuat model regresi linear dan melatih model
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Visualisasi hasil prediksi
def plot_predictions(y_test, y_pred):
    fig, ax = plt.subplots()
    sns.scatterplot(x=y_test, y=y_pred, ax=ax)
    ax.set_xlabel('Nilai Sebenarnya (Kalori)')
    ax.set_ylabel('Prediksi Kalori')
    ax.set_title('Perbandingan Prediksi vs Nilai Sebenarnya')
    st.pyplot(fig)

# Aplikasi Streamlit
def main():
    st.title('Aplikasi Prediksi Kalori Makanan')

    st.write('Masukkan nama makanan yang ingin diprediksi kandungan kalorinya.')

    # Memuat data
    data = load_data()

    # Menampilkan dataset kepada pengguna
    st.subheader('Dataset Nutrisi Makanan')
    st.dataframe(data)

    # Input nama makanan dari user
    makanan = st.text_input('Nama Makanan').strip().title()  # Membuat input case-insensitive

    if makanan:
        # Mencari makanan di dataset
        if makanan in data['Makanan'].values:
            selected_food = data[data['Makanan'] == makanan].iloc[0]
            
            st.write(f"**Makanan:** {selected_food['Makanan']}")
            st.write(f"**Kalori:** {selected_food['Kalori (kcal)']} kcal")
            st.write(f"**Protein:** {selected_food['Protein (g)']} g")
            st.write(f"**Lemak:** {selected_food['Lemak (g)']} g")
            st.write(f"**Karbohidrat:** {selected_food['Karbohidrat (g)']} g")
            st.write(f"**Serat:** {selected_food['Serat (g)']} g")
            st.write(f"**Gula:** {selected_food['Gula (g)']} g")

            # Persiapan data untuk model
            X, y = prepare_data(data)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Melatih model
            model = train_model(X_train, y_train)

            # Menghitung prediksi kalori untuk makanan yang dipilih
            input_features = selected_food[['Protein (g)', 'Lemak (g)', 'Karbohidrat (g)', 'Serat (g)', 'Gula (g)']].values.reshape(1, -1)
            predicted_calories = model.predict(input_features)[0]
            st.write(f"**Prediksi Kalori:** {predicted_calories:.2f} kcal")

            # Evaluasi model
            y_pred = model.predict(X_test)
            mae = mean_absolute_error(y_test, y_pred)
            st.write(f"**Mean Absolute Error (MAE):** {mae:.2f} kcal")

            # Visualisasi hasil prediksi
            plot_predictions(y_test, y_pred)
        
        else:
            st.write("Makanan tidak ditemukan dalam dataset. Silakan masukkan nama makanan lain.")

if __name__ == "__main__":
    main()
