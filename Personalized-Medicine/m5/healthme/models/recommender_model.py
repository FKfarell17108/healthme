from sklearn.tree import DecisionTreeClassifier

def train_model(data):
    # Data sederhana untuk klasifikasi (contoh hanya demo)
    X = data[["umur", "berat_badan", "tinggi_badan"]]
    y = data["riwayat_penyakit"]
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model
