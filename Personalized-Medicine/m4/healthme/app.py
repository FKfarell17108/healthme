from flask import Flask, render_template, request
import pandas as pd
from model import get_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Mengambil data yang dimasukkan pengguna
        age = int(request.form['age'])
        gender = request.form['gender']
        weight = int(request.form['weight'])
        height = int(request.form['height'])
        disease_history = request.form['disease_history']
        allergies = request.form['allergies']
        lifestyle = request.form['lifestyle']
        symptoms = request.form['symptoms']
        previous_treatment = request.form['previous_treatment']

        # Mendapatkan rekomendasi berdasarkan input pengguna
        recommendations = get_recommendation(age, gender, weight, height, disease_history, allergies, lifestyle, symptoms, previous_treatment)
        
        # Menampilkan hasil rekomendasi
        return render_template('result.html', recommendations=recommendations)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
