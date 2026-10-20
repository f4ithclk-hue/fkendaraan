# APEX GARAGE

Sistem Manajemen Kendaraan berbasis Python CLI dengan konsep Pemrograman Berorientasi Objek (PBO).

## Fitur
- Menambahkan data kendaraan.
- Menampilkan daftar kendaraan di terminal.
- Menyimpan data kendaraan ke `kendaraan.csv`.
- Validasi kolom wajib agar tidak kosong.

## Struktur proyek
- `main.py` — menu utama.
- `models.py` — class `Kendaraan` dan `Pelanggan`.
- `tambah_buku.py` — modul pendaftaran kendaraan (nama file dipertahankan dari struktur proyek awal).
- `tampil_buku.py` — modul tampilan daftar kendaraan berbasis CLI.
- `kendaraan.csv` — penyimpanan data kendaraan.

## Menjalankan
Jalankan dari terminal:

```bash
python main.py
```

Pastikan seluruh file berada di folder proyek yang sama dan gunakan Python 3.
