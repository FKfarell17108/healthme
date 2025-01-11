def calculate_bmi(berat_badan, tinggi_badan):
    """
    Menghitung BMI (Body Mass Index).
    Berat badan dalam kg, tinggi badan dalam cm.
    """
    tinggi_meter = tinggi_badan / 100  # Konversi ke meter
    bmi = berat_badan / (tinggi_meter ** 2)
    return round(bmi, 2)

def validate_input(data):
    """
    Validasi input pengguna. Pastikan semua field terisi.
    """
    required_fields = [
        'umur', 'jenis_kelamin', 'berat_badan', 'tinggi_badan',
        'riwayat_penyakit', 'alergi', 'gaya_hidup', 'gejala', 'pengobatan_sebelumnya'
    ]
    for field in required_fields:
        if field not in data or data[field] == '':
            return False, f"Field {field} tidak boleh kosong."
    return True, "Valid"
