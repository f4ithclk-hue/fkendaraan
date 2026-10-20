import subprocess
import sys
from pathlib import Path

FOLDER_PROYEK = Path(__file__).resolve().parent



def buka_tambah_kendaraan():
    subprocess.run(
        [sys.executable, str(FOLDER_PROYEK / "tambah_kendaraan.py")],
        cwd=FOLDER_PROYEK
    )


def buka_tampil_kendaraan():
    subprocess.run(
        [sys.executable, str(FOLDER_PROYEK / "tampil_kendaraan.py")],
        cwd=FOLDER_PROYEK
    )



def menu_utama():
    while True:
        print("\n" + "=" * 46)
        print(" APEX GARAGE ".center(46))
        print(" SISTEM MANAJEMEN KENDARAAN ".center(46))
        print("=" * 46)
        print("1. Tambah Kendaraan")
        print("2. Tampilkan Kendaraan")
        print("0. Keluar")
        print("-" * 46)

        pilihan = input("APEX > Pilih menu: ").strip()

        if pilihan == "1":
            buka_tambah_kendaraan()
        elif pilihan == "2":
            buka_tampil_kendaraan()
        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan APEX GARAGE.")
            break
        else:
            print("[PERINGATAN] Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    menu_utama()
