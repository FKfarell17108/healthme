from data.data_dummy import get_data
from utils.preprocessing import preprocess_user_input
from utils.recommendation_logic import generate_recommendations

if __name__ == "__main__":
    # Input dari pengguna
    user_input = {
        "umur": 25,
        "jenis_kelamin": "Pria",
        "berat_badan": 80,
        "tinggi_badan": 180,
        "riwayat_penyakit": "Hipertensi",
        "alergi": "Kacang",
        "gaya_hidup": "Pasif",
        "gejala": "Lemas",
        "pengobatan_sebelumnya": "Obat Hipertensi",
    }

    # Preprocessing input
    processed_data = preprocess_user_input(user_input)

    # Rekomendasi
    recommendations = generate_recommendations(processed_data)

    # Tampilkan hasil
    print("Rekomendasi:")
    for key, value in recommendations.items():
        print(f"{key}: {value}")
