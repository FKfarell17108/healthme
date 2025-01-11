import pandas as pd

def get_data():
    data = {
        "umur": [25, 16],
        "jenis_kelamin": ["Pria", "Wanita"],
        "berat_badan": [80, 60],
        "tinggi_badan": [180, 170],
        "riwayat_penyakit": ["Hipertensi", "Diabetes"],
        "alergi": ["Kacang", "Debu"],
        "gaya_hidup": ["Pasif", "Aktif"],
        "gejala": ["Lemas", "Sesak Napas"],
        "pengobatan_sebelumnya": ["Obat Hipertensi", "Insulin"],
    }
    return pd.DataFrame(data)
