# Algoritma-ECC-Cantika
Repository ini berisi implementasi Elliptic Curve Cryptography (ECC) yang dibuat from scratch tanpa library kriptografi. Algoritma ini dipilih setelah mempertimbangkan beberapa alternatif karena menawarkan keamanan tinggi dengan kunci yang lebih efisien. Repo ini juga dilengkapi kode implementasi serta PDF penjelasan konsep ECC.

Elliptic Curve Cryptography (ECC) adalah algoritma kriptografi kunci publik yang menggunakan operasi matematika pada kurva eliptik. ECC digunakan untuk proses pembangkitan kunci, enkripsi, dan dekripsi data secara aman. Keamanan ECC didasarkan pada kesulitan menyelesaikan Elliptic Curve Discrete Logarithm Problem (ECDLP), yaitu sulit menentukan nilai k dari persamaan Q = kG pada kurva eliptik.

Langkah-langkah Implementasi ECC Berdasarkan Kode Program

1. Menentukan Parameter Kurva
Program terlebih dahulu menentukan parameter kurva eliptik dengan persamaan:
y^2 = x^3 + ax + b mod p
Parameter yang digunakan pada kode yaitu p = 97, a = 2, b = 3, dan generator point G = (3,6). Generator point ini digunakan sebagai titik dasar dalam operasi ECC.

2. Membuat Fungsi Modular Inverse
Program membuat fungsi mod_inverse() untuk menghitung invers suatu bilangan dalam modulo p. Fungsi ini digunakan saat menghitung slope pada operasi penjumlahan titik di kurva eliptik.

3. Mengimplementasikan Point Addition
Fungsi point_addition() digunakan untuk menjumlahkan dua titik pada kurva eliptik. Perhitungan dilakukan dengan mencari nilai slope terlebih dahulu, kemudian menghitung koordinat titik baru hasil penjumlahan.

4. Mengimplementasikan Scalar Multiplication
Fungsi scalar_multiplication() digunakan untuk mengalikan suatu titik pada kurva dengan bilangan bulat k. Operasi ini merupakan inti dari ECC dan digunakan dalam proses pembangkitan kunci serta enkripsi.

5. Proses Key Generation
Program menghasilkan pasangan kunci menggunakan fungsi generate_keys().
- Sistem memilih bilangan acak sebagai private key (d).
- Public key dihitung menggunakan rumus Q = d * G.

6. Proses Enkripsi
Fungsi encrypt() digunakan untuk mengenkripsi pesan. Pesan direpresentasikan sebagai titik pada kurva.
- Program memilih bilangan acak k.
- Menghitung C1 = k * G.
- Menghitung C2 = M + k * Q.
- Hasil enkripsi berupa pasangan titik (C1, C2).

7. Proses Dekripsi
Fungsi decrypt() digunakan untuk mengembalikan ciphertext menjadi pesan asli.
- Program menghitung S = d * C1.
- Pesan asli diperoleh dengan rumus M = C2 - d * C1.

8. Demonstrasi Program
Program kemudian dijalankan untuk menampilkan seluruh proses ECC mulai dari pembangkitan kunci, enkripsi, hingga dekripsi pesan. Output program akan menampilkan nilai private key, public key, ciphertext (C1, C2), serta hasil dekripsi.
Pada bagian akhir akan muncul output seperti:
Decrypted Message : (10, 7). Nilai tersebut merupakan titik pesan asli pada kurva eliptik yang berhasil dikembalikan setelah proses dekripsi. Jika nilai hasil dekripsi sama dengan pesan awal sebelum dienkripsi, maka dapat disimpulkan bahwa implementasi algoritma ECC pada program telah berjalan dengan benar.

<img width="561" height="79" alt="image" src="https://github.com/user-attachments/assets/92396b5f-99c1-4fee-a83e-65f44a4fc283" />

