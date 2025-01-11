import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Membuat dataset sintetis (untuk keperluan demo)
def create_synthetic_data():
    np.random.seed(42)

    data = {
        'Usia': np.random.randint(20, 80, 500),
        'Jenis Kelamin': np.random.choice(['Laki-laki', 'Perempuan'], 500),
        'BMI': np.random.uniform(18.5, 35, 500),
        'Tekanan Darah': np.random.randint(100, 180, 500),
        'Kadar Gula Darah': np.random.uniform(70, 200, 500),
        'Riwayat Keluarga': np.random.choice([0, 1], 500),
        'Status Merokok': np.random.choice([0, 1], 500),
        'Aktivitas Fisik': np.random.choice([0, 1, 2, 3], 500),
        'Penyakit Diabetes': np.random.choice([0, 1], 500, p=[0.8, 0.2]),
    }

    df = pd.DataFrame(data)
    df['Jenis Kelamin'] = df['Jenis Kelamin'].map({'Laki-laki': 1, 'Perempuan': 0})

    X = df.drop(columns=['Penyakit Diabetes'])
    y = df['Penyakit Diabetes']

    return X, y

# Pelatihan model
def train_model():
    X, y = create_synthetic_data()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Menyimpan model
    joblib.dump(model, 'diabetes_model.pkl')

# Memuat model yang sudah dilatih
def load_model():
    return joblib.load('diabetes_model.pkl')

# Prediksi menggunakan model
def predict(input_data):
    model = load_model()
    prediction = model.predict([input_data])
    return prediction[0]

# Menjalankan pelatihan model (gunakan ini sekali saja)
# train_model()
