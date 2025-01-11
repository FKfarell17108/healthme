import streamlit as st
import requests

# Fungsi untuk memanggil API nutrisi
def get_nutrition_info(food_item):
    try:
        # URL dan API Key dari penyedia API nutrisi (misal: Nutritionix atau API lain yang sesuai)
        url = "https://api.nutritionix.com/v1_1/search"
        api_key = "YOUR_API_KEY"  # Ganti dengan API key yang sesuai
        app_id = "YOUR_APP_ID"    # Ganti dengan App ID yang sesuai

        # Parameter query
        params = {
            'appId': app_id,
            'appKey': api_key,
            'query': food_item,
            'fields': ['item_name', 'nf_calories', 'nf_protein', 'nf_total_fat', 'nf_total_carbohydrate', 'nf_dietary_fiber', 'nf_sugars']
        }

        # Memanggil API
        response = requests.get(url, params=params)
        data = response.json()

        # Menyaring hasil pertama
        if data and 'hits' in data and len(data['hits']) > 0:
            result = data['hits'][0]['fields']
            return {
                'Nama': result['item_name'],
                'Kalori (kcal)': result['nf_calories'],
                'Protein (g)': result['nf_protein'],
                'Lemak (g)': result['nf_total_fat'],
                'Karbohidrat (g)': result['nf_total_carbohydrate'],
                'Serat (g)': result['nf_dietary_fiber'],
                'Gula (g)': result['nf_sugars']
            }
        else:
            return None
    except Exception as e:
        st.write("Error:", e)
        return None

# Aplikasi Streamlit
def main():
    st.title('Aplikasi Estimasi Kalori dan Nutrisi Makanan (Input Bebas)')
    
    st.write('Masukkan nama makanan atau bahan-bahan yang ingin Anda cek kandungan nutrisinya.')
    
    # Input makanan dari user
    food_input = st.text_input('Nama Makanan/Bahan').strip()
    
    # Ketika user memasukkan makanan
    if food_input:
        # Memanggil API untuk mendapatkan data nutrisi
        nutrition_data = get_nutrition_info(food_input)
        
        if nutrition_data:
            st.write(f"**Nama Makanan:** {nutrition_data['Nama']}")
            st.write(f"**Kalori:** {nutrition_data['Kalori (kcal)']} kcal")
            st.write(f"**Protein:** {nutrition_data['Protein (g)']} g")
            st.write(f"**Lemak:** {nutrition_data['Lemak (g)']} g")
            st.write(f"**Karbohidrat:** {nutrition_data['Karbohidrat (g)']} g")
            st.write(f"**Serat:** {nutrition_data['Serat (g)']} g")
            st.write(f"**Gula:** {nutrition_data['Gula (g)']} g")
        else:
            st.write("Data tidak tersedia untuk makanan ini. Coba masukkan makanan lain.")

if __name__ == "__main__":
    main()
