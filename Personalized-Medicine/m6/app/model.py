def get_recommendations(data):
    """
    Fungsi untuk menghasilkan rekomendasi berdasarkan input data pengguna
    """
    rekomendasi = {
        'obat': [],
        'gaya_hidup': [],
        'nutrisi': [],
        'risiko_penyakit': [],
        'biaya_pengobatan': []
    }
    
    # Rekomendasi Obat berdasarkan riwayat penyakit dan pengobatan sebelumnya
    if data['riwayat_penyakit'] == 'Hipertensi':
        rekomendasi['obat'] = ['ACE Inhibitor atau ARB', 'Penghambat Saluran Kalsium']
    elif data['riwayat_penyakit'] == 'Diabetes':
        rekomendasi['obat'] = ['Metformin', 'Insulin', 'Salbutamol']
    
    # Rekomendasi Gaya Hidup
    if data['gaya_hidup'] == 'Jarang olahraga':
        rekomendasi['gaya_hidup'] = ['Jalan kaki atau Jogging ringan', 'Bersepeda']
    else:
        rekomendasi['gaya_hidup'] = ['Yoga dan Meditasi', 'Berenang']
    
    # Rekomendasi Nutrisi
    rekomendasi['nutrisi'] = ['Makanan rendah garam', 'Buah dan sayuran kaya kalium', 'Kacang-kacangan sehat', 'Sumber protein sehat']

    # Risiko Penyakit
    if data['riwayat_penyakit'] == 'Hipertensi':
        rekomendasi['risiko_penyakit'] = ['Penyakit Kardiovaskular', 'Penyakit Ginjal Kronis', 'Retinopati Hipertensi']
    elif data['riwayat_penyakit'] == 'Diabetes':
        rekomendasi['risiko_penyakit'] = ['Penyakit Jantung', 'Masalah Pernapasan', 'Gangguan Ginjal']
    
    # Biaya Pengobatan
    if data['riwayat_penyakit'] == 'Diabetes':
        rekomendasi['biaya_pengobatan'] = ['Biaya Perawatan Diabetes', 'Biaya Perawatan Jantung', 'Biaya Rawat Inap']
    else:
        rekomendasi['biaya_pengobatan'] = ['Biaya Pengobatan Bulanan', 'Biaya Pemeriksaan Laboratorium']

    return rekomendasi
