# Gunakan image Python 3.10 untuk lingkungan FastAPI
FROM python:3.10-slim

# Tetapkan direktori kerja
WORKDIR /app

# Salin file requirements ke dalam container
COPY requirements.txt .

# Instal dependensi
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode aplikasi ke dalam container
COPY src /app/src

# Jalankan FastAPI dengan Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]