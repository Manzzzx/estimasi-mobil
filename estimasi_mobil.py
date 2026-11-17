import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Tahun Mobil', min_value=1990, max_value=2024, value=2019)
mileage = st.number_input('Jarak Tempuh (dalam km)', min_value=0, value=5000)
tax = st.number_input('Pajak (dalam EUR)', min_value=0, value=145)
mpg = st.number_input('MPG (Miles per Gallon)', min_value=0.0, value=30.2)
engineSize = st.number_input('Ukuran Mesin (dalam liter)', min_value=0.0, value=2.0)

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
      )
    st.write('Estimasi harga mobil bekas dalam EUR: ', predict)
    st.write('Estimasi harga mobil bekas dalam IDR: ', predict * 19000)