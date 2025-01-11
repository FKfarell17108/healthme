from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthme.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model untuk menyimpan data kesehatan
class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    disease_history = db.Column(db.String(200), nullable=True)
    allergies = db.Column(db.String(100), nullable=True)
    lifestyle = db.Column(db.String(200), nullable=True)
    symptoms = db.Column(db.String(200), nullable=True)
    past_treatments = db.Column(db.String(200), nullable=True)
    recommended_treatment = db.Column(db.String(200), nullable=True)
    recommended_lifestyle = db.Column(db.String(200), nullable=True)

# Membuat database jika belum ada
with app.app_context():
    db.create_all()

# Model machine learning untuk prediksi
class HealthPredictor:
    def __init__(self):
        # Data pelatihan contoh
        self.data = {
            'age': [25, 45, 32, 28, 60, 23, 40, 30],
            'gender': ['Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita', 'Pria', 'Wanita'],
            'weight': [70, 60, 80, 55, 85, 50, 75, 68],
            'height': [175, 160, 180, 162, 170, 158, 165, 170],
            'disease_history': ['Hipertensi', 'Diabetes', 'Tidak ada', 'Asma', 'Jantung', 'Tidak ada', 'Hipertensi, Kolesterol Tinggi', 'Tidak ada'],
            'allergies': ['Tidak', 'Alergi Debu', 'Tidak', 'Alergi Debu', 'Tidak', 'Alergi Makanan Laut', 'Alergi Pollen', 'Tidak'],
            'lifestyle': ['Olahraga 3x/minggu', 'Jarang Olahraga', 'Merokok, Minum Alkohol', 'Olahraga 2x/minggu', 'Tidak Olahraga', 'Olahraga Teratur', 'Olahraga Ringan', 'Diet Ketat'],
            'symptoms': ['Pusing, Sakit Kepala', 'Lemas, Sering Haus', 'Sakit Perut, Batuk', 'Sesak Napas, Batuk', 'Sesak Napas, Nyeri Dada', 'Mual, Pusing', 'Sakit Kepala, Pusing', 'Lemas, Sering Pusing'],
            'past_treatments': ['Obat Hipertensi, Diet Rendah Garam', 'Insulin, Diet Rendah Karbohidrat', 'Tidak Ada Pengobatan', 'Inhaler Asma', 'Obat Jantung', 'Tidak Ada Pengobatan', 'Obat Hipertensi, Obat Kolesterol', 'Tidak Ada Pengobatan'],
            'recommended_treatment': ['Obat Hipertensi, Diet Rendah Garam', 'Insulin, Diet Rendah Karbohidrat', 'Berhenti Merokok, Makan Seimbang', 'Olahraga Ringan, Hindari Debu', 'Obat Jantung', 'Tidak Ada Pengobatan', 'Obat Hipertensi, Obat Kolesterol', 'Makan dengan Seimbang, Rutin Berolahraga'],
            'recommended_lifestyle': ['Olahraga, Diet Sehat', 'Rutin Berolahraga, Makanan Sehat', 'Berhenti Merokok, Makan Seimbang', 'Olahraga Ringan, Hindari Debu', 'Olahraga Jalan Kaki, Diet Rendah Lemak', 'Makanan Sehat, Olahraga Teratur', 'Olahraga Rutin, Diet Sehat', 'Makan dengan Seimbang, Rutin Berolahraga']
        }

        # Mengubah data menjadi DataFrame untuk training
        df = pd.DataFrame(self.data)

        # Menyusun fitur dan label
        self.X = pd.get_dummies(df[['age', 'weight', 'height', 'disease_history', 'allergies', 'lifestyle', 'symptoms', 'past_treatments']])
        self.y_treatment = df['recommended_treatment']
        self.y_lifestyle = df['recommended_lifestyle']

        # Membuat model Decision Tree untuk pengobatan dan gaya hidup
        self.model_treatment = DecisionTreeClassifier()
        self.model_lifestyle = DecisionTreeClassifier()

        # Melatih model
        self.model_treatment.fit(self.X, self.y_treatment)
        self.model_lifestyle.fit(self.X, self.y_lifestyle)

    def predict(self, data):
        # Mengubah input pengguna menjadi format yang sesuai
        input_data = pd.get_dummies(pd.DataFrame([data]))
        
        # Menyelaraskan kolom input dengan kolom yang digunakan dalam pelatihan
        input_data = input_data.reindex(columns=self.X.columns, fill_value=0)
        
        # Melakukan prediksi pengobatan dan gaya hidup
        treatment = self.model_treatment.predict(input_data)[0]
        lifestyle = self.model_lifestyle.predict(input_data)[0]
        
        return treatment, lifestyle
    
@app.route("/view_data")
def view_data():
    # Mengambil semua data dari tabel HealthRecord
    records = HealthRecord.query.all()
    
    # Mengirim data ke template view_data.html
    return render_template("view_data.html", records=records)

# Instance dari HealthPredictor
predictor = HealthPredictor()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Mengambil data dari form
        age = request.form['age']
        gender = request.form['gender']
        weight = request.form['weight']
        height = request.form['height']
        disease_history = request.form['disease_history']
        allergies = request.form['allergies']
        lifestyle = request.form['lifestyle']
        symptoms = request.form['symptoms']
        past_treatments = request.form['past_treatments']
        
        # Data input untuk prediksi
        input_data = {
            'age': int(age),
            'weight': float(weight),
            'height': int(height),
            'disease_history': disease_history,
            'allergies': allergies,
            'lifestyle': lifestyle,
            'symptoms': symptoms,
            'past_treatments': past_treatments
        }

        # Prediksi rekomendasi
        recommended_treatment, recommended_lifestyle = predictor.predict(input_data)

        # Menyimpan data ke database
        new_record = HealthRecord(
            age=int(age),
            gender=gender,
            weight=float(weight),
            height=int(height),
            disease_history=disease_history,
            allergies=allergies,
            lifestyle=lifestyle,
            symptoms=symptoms,
            past_treatments=past_treatments,
            recommended_treatment=recommended_treatment,
            recommended_lifestyle=recommended_lifestyle
        )
        db.session.add(new_record)
        db.session.commit()
        
        return render_template("index.html", success=True, recommended_treatment=recommended_treatment, recommended_lifestyle=recommended_lifestyle)

    return render_template("index.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
