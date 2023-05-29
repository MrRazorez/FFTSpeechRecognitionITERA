import librosa
import numpy as np
import math

# Fungsi untuk menghitung average energy
def compute_average_energy(signal):
    return np.mean(signal**2)

# Fungsi untuk menghitung silent ratio
def compute_silent_ratio(signal, threshold=0.01):
    silent_samples = np.sum(signal < threshold)
    return silent_samples / len(signal)

# Mendapatkan sinyal suara dari file audio
audio_file = str(input("Masukkan path:\n"))
signal, sr = librosa.load(audio_file, sr=11025)  # Frekuensi 11.025 Hz

# Ekstraksi ciri suara dengan membagi sinyal menjadi potongan 0,2 detik
segment_duration = 0.2  # Durasi potongan sinyal (dalam detik)
segment_length = int(segment_duration * sr)  # Panjang potongan sinyal (jumlah sampel)

# Inisialisasi array untuk menyimpan hasil ekstraksi ciri suara
silent_ratio_values = []
average_energy_values = []

# Inisialisasi variabel untuk menyimpan jumlah segment
num_segments = 0

# Ekstraksi ciri suara pada setiap potongan sinyal
for i in range(0, len(signal), segment_length):
    segment = signal[i:i+segment_length]

    # Konversi potongan sinyal ke dalam domain frekuensi menggunakan FFT
    segment_frequency = np.abs(librosa.stft(segment))

    silent_ratio = compute_silent_ratio(segment_frequency)
    average_energy = compute_average_energy(segment_frequency)

    silent_ratio_values.append(silent_ratio)
    average_energy_values.append(average_energy)

    num_segments += 1

# Menampilkan hasil ekstraksi ciri suara
print("Tabel 1. Silent Ratio dan Average Energy untuk Identifikasi Signal Suara")
print("No.\tWaktu\t\tSilent Ratio\tAverage Energy")
for i in range(num_segments):
    segment_number = i + 1
    segment_start = i * segment_duration
    segment_end = segment_start + segment_duration
    print(f"{segment_number}\t{segment_start:.1f}-{segment_end:.1f}\t\t{silent_ratio_values[i]:.4f}\t\t{average_energy_values[i]:.4f}")

# Menghitung nilai rata-rata
average_silent_ratio = np.mean(silent_ratio_values)
average_energy = np.mean(average_energy_values)

print("\nJumlah\t\t\t\t\tRata-rata")
print(f"Silent Ratio\t\t\t{average_silent_ratio:.5f}")
print(f"Average Energy\t\t\t{average_energy:.4f}")
