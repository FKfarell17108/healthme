from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, NumberRange

class HealthForm(FlaskForm):
    age = IntegerField('Usia', validators=[DataRequired(message="Usia harus diisi.")])
    gender = SelectField('Jenis Kelamin', choices=[('M', 'Laki-laki'), ('F', 'Perempuan')], validators=[DataRequired()])
    weight = FloatField('Berat Badan (kg)', validators=[DataRequired(message="Berat badan harus diisi.")])
    height = FloatField('Tinggi Badan (m)', validators=[DataRequired(message="Tinggi badan harus diisi.")])
    lifestyle_score = IntegerField('Skor Gaya Hidup (1-10)', 
                                    validators=[
                                        DataRequired(message="Skor gaya hidup harus diisi."),
                                        NumberRange(min=1, max=10, message="Skor harus antara 1 dan 10.")
                                    ])
    medical_history = TextAreaField('Riwayat Penyakit')
    allergies = TextAreaField('Alergi')
    symptoms = TextAreaField('Gejala')
    past_treatments = TextAreaField('Pengobatan Sebelumnya')
    email = StringField('Email', 
                        validators=[
                            DataRequired(message="Email harus diisi."),
                            Email(message="Format email tidak valid.")
                        ])
    submit = SubmitField('Kirim')
