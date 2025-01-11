def generate_recommendations(user_data):
    if user_data["riwayat_penyakit"] == "Hipertensi":
        return {
            "rekomendasi_obat": ["ACE Inhibitor", "Penghambat Saluran Kalsium"],
            "rekomendasi_gaya_hidup": ["Jalan Kaki", "Yoga", "Meditasi"],
            "rekomendasi_nutrisi": ["Makanan Rendah Garam", "Buah Kaya Kalium"],
            "risiko_penyakit": ["Penyakit Kardiovaskular", "Ginjal Kronis"],
            "biaya_pengobatan": ["Rp500.000/bulan", "Rp2.000.000/tahun"],
        }
    elif user_data["riwayat_penyakit"] == "Diabetes":
        return {
            "rekomendasi_obat": ["Metformin", "Insulin"],
            "rekomendasi_gaya_hidup": ["Olahraga Teratur", "Manajemen Stres"],
            "rekomendasi_nutrisi": ["Makanan Berserat Tinggi", "Rendah Karbohidrat"],
            "risiko_penyakit": ["Penyakit Jantung", "Gangguan Ginjal"],
            "biaya_pengobatan": ["Rp1.000.000/bulan", "Rp3.000.000/tahun"],
        }
