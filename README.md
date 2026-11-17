# Estimasi Harga Mobil Bekas

Aplikasi web berbasis Streamlit untuk memperkirakan harga mobil bekas Toyota menggunakan model Linear Regression. Pengguna dapat memasukkan tahun kendaraan, jarak tempuh, pajak, konsumsi bahan bakar, dan ukuran mesin untuk mendapatkan estimasi harga dalam EUR serta konversi perkiraan dalam IDR.

## Fitur

- Antarmuka estimasi harga yang interaktif
- Prediksi menggunakan model machine learning yang tersimpan dalam `estimasi_mobil.sav`
- Input tahun, jarak tempuh, pajak, MPG, dan ukuran mesin
- Tampilan hasil estimasi dalam EUR dan IDR

## Teknologi

- Python
- Streamlit
- pandas
- scikit-learn
- pickle
- Jupyter Notebook

## Struktur Proyek

```text
Estimasi Mobil/
├── estimasi_mobil.py       # Aplikasi Streamlit
├── estimasi_mobil.ipynb    # Proses pelatihan dan analisis model
├── estimasi_mobil.sav      # Model Linear Regression yang telah dilatih
├── toyota.csv              # Dataset mobil Toyota
├── requirements.txt        # Daftar dependensi Python
└── README.md
```

## Persyaratan

- Python 3.10–3.12
- pip

## Instalasi

1. Masuk ke direktori proyek:

```powershell
cd "d:\Manzz\Learning\Vscode\Estimasi Mobil"
```

2. Buat dan aktifkan environment virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instal dependensi:

```powershell
pip install -r requirements.txt
```

## Menjalankan Aplikasi

Pastikan `estimasi_mobil.sav` berada satu direktori dengan `estimasi_mobil.py`, lalu jalankan:

```powershell
streamlit run estimasi_mobil.py
```

Aplikasi kemudian dapat dibuka melalui alamat yang ditampilkan oleh Streamlit, biasanya `http://localhost:8501`.

## Cara Penggunaan

1. Masukkan tahun mobil pada rentang 1990–2024.
2. Masukkan jarak tempuh dalam kilometer.
3. Masukkan nilai pajak dalam EUR.
4. Masukkan nilai MPG (Miles per Gallon).
5. Masukkan ukuran mesin dalam liter.
6. Tekan tombol **Estimasi Harga** untuk menampilkan hasil.

## Input Model

| Input | Satuan | Nilai bawaan |
|---|---|---:|
| Tahun mobil | Tahun | 2019 |
| Jarak tempuh | Kilometer | 5000 |
| Pajak | EUR | 145 |
| MPG | Miles per Gallon | 30.2 |
| Ukuran mesin | Liter | 2.0 |

## Catatan

- Prediksi EUR diperkirakan oleh model Linear Regression dari dataset Toyota.
- Konversi ke IDR menggunakan kurs tetap sebesar `1 EUR = 19.000 IDR`, sehingga hasilnya bukan kurs aktual.
- Hasil prediksi hanya digunakan sebagai estimasi dan tidak menjamin harga pasar sesungguhnya.
