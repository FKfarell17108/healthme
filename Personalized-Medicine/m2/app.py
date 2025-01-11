from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Mengambil input dari form
            usia = int(request.form["usia"])
            jenis_kelamin = 1 if request.form["jenis_kelamin"] == "Laki-laki" else 0
            bmi = float(request.form["bmi"])
            tekanan_darah = int(request.form["tekanan_darah"])
            kadar_gula_darah = float(request.form["kadar_gula_darah"])  # Pastikan nama field sesuai
            riwayat_keluarga = int(request.form["riwayat_keluarga"])
            status_merokok = int(request.form["status_merokok"])
            aktivitas_fisik = int(request.form["aktivitas_fisik"])

            # Membuat array dari data input
            user_data = [usia, jenis_kelamin, bmi, tekanan_darah, kadar_gula_darah, riwayat_keluarga, status_merokok, aktivitas_fisik]
            
            # Melakukan prediksi menggunakan fungsi predict
            result = predict(user_data)

            # Menampilkan hasil prediksi ke pengguna
            if result == 1:
                prediction = "Risiko tinggi terkena penyakit diabetes."
            else:
                prediction = "Risiko rendah terkena penyakit diabetes."

            return render_template("index.html", result=prediction)

        except KeyError as e:
            return f"Error: Missing field {e} in the form", 400  # Menampilkan error jika ada field yang hilang

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)