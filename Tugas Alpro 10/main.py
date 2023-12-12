
import json

class Mahasiswa:
    def __init__(self, npm_mahasiswa, nama, umur, angkatan):
        self.npm_mahasiswa = npm_mahasiswa
        self.nama = nama
        self.umur = umur
        self.angkatan = angkatan

class DatabaseMahasiswa:
    def __init__(self, file_path="database_mahasiswa.json"):
        self.file_path = file_path
        self.mahasiswa = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return {int(npm_mahasiswa): Mahasiswa(int(npm_mahasiswa), mahasiswa['nama'], mahasiswa['umur'], mahasiswa['angkatan'])
                        for npm_mahasiswa, mahasiswa in data.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_data(self):
        with open(self.file_path, 'w') as file:
            data = {str(npm_mahasiswa): {'nama': mahasiswa.nama, 'umur': mahasiswa.umur, 'angkatan': mahasiswa.angkatan}
                    for npm_mahasiswa, mahasiswa in self.mahasiswa.items()}
            json.dump(data, file, indent=2)

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa[mahasiswa.npm_mahasiswa] = mahasiswa
        self._save_data()
        print(f"Mahasiswa {mahasiswa.nama} berhasil ditambahkan.")

    def hapus_mahasiswa(self, npm_mahasiswa):
        if npm_mahasiswa in self.mahasiswa:
            mahasiswa_terhapus = self.mahasiswa.pop(npm_mahasiswa)
            self._save_data()
            print(f"Mahasiswa {mahasiswa_terhapus.nama} berhasil dihapus.")
        else:
            print(f"Mahasiswa dengan NPM {npm_mahasiswa} tnpmak ditemukan.")

    def tampilkan_mahasiswa(self):
        print("Database Mahasiswa:")
        for npm_mahasiswa, mahasiswa in self.mahasiswa.items():
            print("-----------------------------------------------")
            print(f"\n\n NPM\t\t: {npm_mahasiswa}\n Nama\t\t: {mahasiswa.nama}\n Umur\t\t: {mahasiswa.umur}th\n angkatan\t: {mahasiswa.angkatan}\n\n")
            print("-----------------------------------------------")

    def perbarui_mahasiswa(self, npm_mahasiswa, nama=None, umur=None, angkatan=None):
        if npm_mahasiswa in self.mahasiswa:
            mahasiswa = self.mahasiswa[npm_mahasiswa]
            if nama is not None:
                mahasiswa.nama = nama
            if umur is not None:
                mahasiswa.umur = umur
            if angkatan is not None:
                mahasiswa.angkatan = angkatan
            self._save_data()
            print(f"Mahasiswa {mahasiswa.nama} berhasil diperbarui.")
        else:
            print(f"Mahasiswa dengan NPM {npm_mahasiswa} tnpmak ditemukan.")

# Membuat objek DatabaseMahasiswa
db = DatabaseMahasiswa()

# Input dari pengguna untuk menambahkan mahasiswa
while True:
    print("\nMenu:")
    print("1. Tambah Mahasiswa")
    print("2. hapus data")
    print("3. Tampilkan Mahasiswa")
    print("4. Keluar")

    pilihan = input("Pilih opsi (1/2/3/4): ")

    if pilihan == '1':
        npm_mahasiswa = int(input("Masukkan NPM : "))
        nama = input("Masukkan Nama : ")
        umur = int(input("Masukkan Umur : "))
        angkatan = input("Masukkan Tahun Angkatan : ")

        mahasiswa_baru = Mahasiswa(npm_mahasiswa, nama, umur, angkatan)
        db.tambah_mahasiswa(mahasiswa_baru)

    # Input dari pengguna untuk menghapus mahasiswa
    elif pilihan == '2':
        npm_mahasiswa_hapus = int(input("Masukkan NPM Mahasiswa yang akan dihapus: "))
        db.hapus_mahasiswa(npm_mahasiswa_hapus)

        
    elif pilihan == '3':
        db.tampilkan_mahasiswa()
        

    elif pilihan == '4':
        print("Program selesai.")
        break

    else:
        print("Pilihan tnpmak valnpm. Silakan pilih lagi.")
