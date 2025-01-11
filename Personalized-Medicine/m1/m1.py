import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, render_template, request, jsonify

# Inisialisasi Flask
app = Flask(__name__)

# Membuat DataFrame dari data yang telah disiapkan
data = {
    'Umur': [25, 45, 32, 28, 60, 23, 40, 30],
    'Jenis Kelamin': ['Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita'],
    'Berat Badan (kg)': [70, 60, 80, 55, 85, 50, 75, 68],
    'Tinggi Badan (cm)': [175, 160, 180, 162, 170, 158, 165, 170],
    'Riwayat Penyakit': ['Hipertensi', 'Diabetes', 'Tidak ada', 'Asma', 'Jantung', 'Tidak ada', 'Hipertensi, Kolesterol Tinggi', 'Tidak ada'],
    'Alergi': ['Tidak', 'Alergi Debu', 'Tidak', 'Alergi Debu', 'Tidak', 'Alergi Makanan Laut', 'Alergi Pollen', 'Tidak'],
    'Gaya Hidup': ['Olahraga 3x/minggu', 'Jarang Olahraga', 'Merokok, Minum Alkohol', 'Olahraga 2x/minggu', 'Tidak Olahraga', 'Olahraga Teratur', 'Olahraga Ringan', 'Diet Ketat'],
    'Gejala': ['Pusing, Sakit Kepala', 'Lemas, Sering Haus', 'Sakit Perut, Batuk', 'Sesak Napas, Batuk', 'Sesak Napas, Nyeri Dada', 'Mual, Pusing', 'Sakit Kepala, Pusing', 'Lemas, Sering Pusing'],
    'Pengobatan Sebelumnya': ['Obat Hipertensi, Diet Rendah Garam', 'Insulin, Diet Rendah Karbohidrat', 'Tidak Ada Pengobatan', 'Inhaler Asma', 'Obat Jantung', 'Tidak Ada Pengobatan', 'Obat Hipertensi, Obat Kolesterol', 'Tidak Ada Pengobatan'],
    'Rekomendasi Pengobatan': ['Obat Hipertensi, Diet Rendah Garam', 'Insulin, Diet Rendah Karbohidrat', 'Berhenti Merokok, Makan Seimbang', 'Olahraga Ringan, Hindari Debu', 'Obat Jantung', 'Tidak Ada Pengobatan', 'Obat Hipertensi, Obat Kolesterol', 'Makan dengan Seimbang, Rutin Berolahraga'],
    'Rekomendasi Gaya Hidup': ['Olahraga, Diet Sehat', 'Rutin Berolahraga, Makanan Sehat', 'Berhenti Merokok, Makan Seimbang', 'Olahraga Ringan, Hindari Debu', 'Olahraga Jalan Kaki, Diet Rendah Lemak', 'Makanan Sehat, Olahraga Teratur', 'Olahraga Rutin, Diet Sehat', 'Makan dengan Seimbang, Rutin Berolahraga']
}

df = pd.DataFrame(data)

# Preprocessing Data
label_encoder = LabelEncoder()

# Fit encoder dengan semua kategori yang ada
df['Jenis Kelamin'] = label_encoder.fit_transform(df['Jenis Kelamin'])
df['Riwayat Penyakit'] = label_encoder.fit_transform(df['Riwayat Penyakit'])
df['Alergi'] = label_encoder.fit_transform(df['Alergi'])
df['Gaya Hidup'] = label_encoder.fit_transform(df['Gaya Hidup'])
df['Gejala'] = label_encoder.fit_transform(df['Gejala'])
df['Pengobatan Sebelumnya'] = label_encoder.fit_transform(df['Pengobatan Sebelumnya'])
df['Rekomendasi Pengobatan'] = label_encoder.fit_transform(df['Rekomendasi Pengobatan'])
df['Rekomendasi Gaya Hidup'] = label_encoder.fit_transform(df['Rekomendasi Gaya Hidup'])

# Pisahkan fitur dan target
X = df[['Umur', 'Jenis Kelamin', 'Berat Badan (kg)', 'Tinggi Badan (cm)', 'Riwayat Penyakit', 'Alergi', 'Gaya Hidup', 'Gejala', 'Pengobatan Sebelumnya']]
y = df['Rekomendasi Pengobatan']

# Latih model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Fungsi untuk prediksi rekomendasi pengobatan
def get_recommendation(user_input):
    # Mengubah input menjadi numerik menggunakan label_encoder
    user_input_encoded = []
    
    # Encode setiap kategori
    for i, value in enumerate(user_input[1:]):  # Mulai dari indeks 1 karena umur sudah dalam bentuk angka
        if isinstance(value, str):
            try:
                encoded_value = label_encoder.transform([value])[0]
            except ValueError:
                # Jika tidak ada dalam kategori sebelumnya, beri nilai default
                encoded_value = label_encoder.transform([label_encoder.classes_[0]])[0]  # Pilih nilai default dari kelas pertama
            user_input_encoded.append(encoded_value)
        else:
            user_input_encoded.append(value)  # Untuk angka, tidak perlu di-encode
    
    # Menambahkan umur yang tidak di-encode
    user_input_encoded = [user_input[0]] + user_input_encoded
    
    # Prediksi rekomendasi pengobatan
    prediction = model.predict([user_input_encoded])
    return label_encoder.inverse_transform(prediction)[0]

# Rute utama untuk halaman web
@app.route('/')
def index():
    return render_template('index.html')

# Rute untuk mendapatkan rekomendasi pengobatan
@app.route('/get_recommendation', methods=['POST'])
def get_recommendation_from_web():
    # Ambil input dari form HTML
    umur = int(request.form['umur'])
    jenis_kelamin = request.form['jenis_kelamin']
    berat_badan = int(request.form['berat_badan'])
    tinggi_badan = int(request.form['tinggi_badan'])
    riwayat_penyakit = request.form['riwayat_penyakit']
    alergi = request.form['alergi']
    gaya_hidup = request.form['gaya_hidup']
    gejala = request.form['gejala']
    pengobatan_sebelumnya = request.form['pengobatan_sebelumnya']
    
    # Encode input untuk model
    user_input = [umur, jenis_kelamin, berat_badan, tinggi_badan, riwayat_penyakit, alergi, gaya_hidup, gejala, pengobatan_sebelumnya]
    
    # Prediksi rekomendasi pengobatan
    recommendation = get_recommendation(user_input)
    
    return jsonify({'rekomendasi': recommendation})

if __name__ == '__main__':
    app.run(debug=True)
