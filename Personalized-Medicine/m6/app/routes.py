from flask import Blueprint, render_template, request
from .model import get_recommendations
from .utils import calculate_bmi, validate_input

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Ambil data dari form input
        data = {
            'umur': request.form.get('umur', type=int),
            'jenis_kelamin': request.form.get('jenis_kelamin'),
            'berat_badan': request.form.get('berat_badan', type=int),
            'tinggi_badan': request.form.get('tinggi_badan', type=int),
            'riwayat_penyakit': request.form.get('riwayat_penyakit'),
            'alergi': request.form.get('alergi'),
            'gaya_hidup': request.form.get('gaya_hidup'),
            'gejala': request.form.get('gejala'),
            'pengobatan_sebelumnya': request.form.get('pengobatan_sebelumnya')
        }

        # Validasi input
        is_valid, message = validate_input(data)
        if not is_valid:
            return render_template('index.html', error=message)

        # Hitung BMI (opsional)
        data['bmi'] = calculate_bmi(data['berat_badan'], data['tinggi_badan'])

        # Dapatkan rekomendasi berdasarkan data input
        hasil = get_recommendations(data)
        return render_template('result.html', hasil=hasil)

    return render_template('index.html')
