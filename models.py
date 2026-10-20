class Kendaraan:
    def __init__(self, id_kendaraan, merk, model, tahun, plat_nomor, status="Tersedia"):
        self.id_kendaraan = id_kendaraan
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.plat_nomor = plat_nomor
        self.status = status

    def to_list(self):
        return [self.id_kendaraan, self.merk, self.model, self.tahun, self.plat_nomor, self.status]

    def __str__(self):
        return (
            f"{self.id_kendaraan} | {self.merk} {self.model} ({self.tahun}) "
            f"| Plat: {self.plat_nomor} | Status: {self.status}"
        )


class Pelanggan:
    def __init__(self, id_pelanggan, nama, no_hp):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.no_hp = no_hp

    def to_list(self):
        return [self.id_pelanggan, self.nama, self.no_hp]

    def __str__(self):
        return f"{self.nama} ({self.id_pelanggan}) - No. HP {self.no_hp}"
