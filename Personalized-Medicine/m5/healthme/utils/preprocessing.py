def preprocess_user_input(input_data):
    # Contoh preprocessing: normalisasi atau encoding
    return {
        "umur": input_data["umur"],
        "jenis_kelamin": 1 if input_data["jenis_kelamin"] == "Pria" else 0,
        "bmi": input_data["berat_badan"] / ((input_data["tinggi_badan"] / 100) ** 2),
        "riwayat_penyakit": input_data["riwayat_penyakit"],
        "alergi": input_data["alergi"],
        "gaya_hidup": input_data["gaya_hidup"],
        "gejala": input_data["gejala"],
        "pengobatan_sebelumnya": input_data["pengobatan_sebelumnya"],
    }
