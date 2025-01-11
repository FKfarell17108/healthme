import pandas as pd

# Data Dummy di dalam kode
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

# Membuat DataFrame dari data
df = pd.DataFrame(data)

def get_recommendation(age, gender, weight, height, disease_history, allergies, lifestyle, symptoms, previous_treatment):
    # Fuzzy matching / Matching yang lebih longgar dengan str.contains()
    filtered_df = df[
        (df['Umur'] == age) & 
        (df['Jenis Kelamin'] == gender) & 
        (df['Berat Badan (kg)'] == weight) & 
        (df['Tinggi Badan (cm)'] == height) & 
        (df['Riwayat Penyakit'].str.contains(disease_history, case=False, na=False)) &
        (df['Alergi'].str.contains(allergies, case=False, na=False)) & 
        (df['Gaya Hidup'].str.contains(lifestyle, case=False, na=False)) & 
        (df['Gejala'].str.contains(symptoms, case=False, na=False)) & 
        (df['Pengobatan Sebelumnya'].str.contains(previous_treatment, case=False, na=False))
    ]
    
    if not filtered_df.empty:
        result = filtered_df.iloc[0]
        recommendations = {
            'rekomendasi_pengobatan': result['Rekomendasi Pengobatan'],
            'rekomendasi_gaya_hidup': result['Rekomendasi Gaya Hidup']
        }
    else:
        recommendations = {
            'rekomendasi_pengobatan': 'Tidak ada rekomendasi yang ditemukan.',
            'rekomendasi_gaya_hidup': 'Tidak ada rekomendasi yang ditemukan.'
        }
    
    return recommendations
