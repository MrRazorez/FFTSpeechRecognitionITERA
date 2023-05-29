# Menerapkan Speech Recognition dengan Menggunakan Average Energy dan Silent Ratio Sebagai Feature Extraction Suara untuk Mengidentifikasi Suara Manusia Ke Dalam Python dengan library Librosa dan Perhitungan Manual dengan dibantu oleh Numpy

## PENGANTAR
Biometric recognition adalah sistem yang digunakan untuk mengenali atau mengidentifikasi seseorang berdasarkan karakteristik biologis unik yang dimilikinya. Tujuan dari sistem ini adalah untuk keamanan dengan mengenali identitas seseorang. Speech recognition adalah proses yang dilakukan oleh komputer untuk mengenali kata-kata yang diucapkan oleh seseorang tanpa memperhatikan identitas orang tersebut. Pola peningkatan dan penurunan sinyal suara merupakan fitur khas dari seseorang saat berbicara, sehingga rata-rata energi suara dan rasio diam merupakan faktor penting dalam mendeteksi karakteristik dan pola suara seseorang. Algoritma Fourier Frequency Transform (FFT) digunakan untuk menggambarkan komponen-komponen data dalam domain frekuensi. Dari teori tersebut, penulis akan menerapkannya menggunakan library Librosa untuk percobaan perhitungan singkat dan Numpy untuk percobaan langkah demi langkah sesuai jurnal penelitian pada Python.

Hal - hal yang perlu dilakukan selama penelitian, antara lain :

* Akuisisi Signal Audio => Pada percobaan ini, 2 audio hasil dari AI Text-to-Speech Generator digunakan sebagai sampel yang akan diuji.
* Ekstraksi Ciri Suara => Untuk mengenali pola dari suatu sinyal suara, harus dengan mengekstraksi ciri sinyal tersebut :
    * Membagi sinyal suara berdasarkan range waktu sebesar 0,2 detik.
    * Setiap potongan kemudian diolah ke dalam domain frekuensi dengan menggunakan Fourier Frequency Transform (FFT).
    * Dari FFT, terdapat power atau energy tekanan tiap puncak sinyal terhadap frekuensi. Hitung rata-rata energinya.
    * Ekstraksi ciri untuk suara kedua adalah Silent ratio dimana setiap akuisisi suara selalu ada suara yang berada dalam keadaan tenang hingga diambang diam. Untuk mendapatkan signal suara yang khas harus dikurangi dengan ambang keadaan diam (silent).
    * Jumlahkan Average Energy dan Signal Ratio dari setiap potongan sehingga menghasilkan nilai rata - rata untuk setiap suara.

Kata kunci: Average Energy, Fourier Frequency Transform, Speech recognition, Silent Ratio

Referensi :
* [Kurniawan, Wawan. IDENTIFIKASI SPEECH RECOGNITION MANUSIA DENGAN MENGGUNAKAN AVERAGE ENERGY DAN SILENT RATIO SEBAGAI FEATURE EXTRACTION SUARA PADA KOMPUTER.](<https://online-journal.unja.ac.id/biospecies/article/view/2879>)
* [Kusuma, Dine Tiara. Fast Fourier Transform (FFT) Dalam Transformasi Sinyal Frekuensi Suara Sebagai Upaya Perolehan Average Energy (AE) Musik.](<https://jurnal.itpln.ac.id/petir/article/view/1022>)