from datetime import datetime, timedelta
import time

def hitung_umur_detail(tanggal_lahir):
    tanggal_sekarang = datetime.now()
    
    tahun_lahir = tanggal_lahir.year
    bulan_lahir = tanggal_lahir.month
    hari_lahir = tanggal_lahir.day

    tahun_sekarang = tanggal_sekarang.year
    bulan_sekarang = tanggal_sekarang.month
    hari_sekarang = tanggal_sekarang.day

    umur_tahun = tahun_sekarang - tahun_lahir
    umur_bulan = bulan_sekarang - bulan_lahir
    umur_hari = hari_sekarang - hari_lahir

    # Koreksi jika umur hari atau bulan negatif
    if umur_hari < 0:
        umur_bulan -= 1
        umur_hari += 30  # Anggap 1 bulan = 30 hari

    if umur_bulan < 0:
        umur_tahun -= 1
        umur_bulan += 12

    return umur_tahun, umur_bulan, umur_hari

def tampilkan_waktu_umur(tanggal_lahir):
    while True:
        # Perbarui waktu setiap detik
        waktu_sekarang = datetime.now()
        umur_tahun, umur_bulan, umur_hari = hitung_umur_detail(tanggal_lahir)

        # Hapus baris sebelumnya dengan \r
        print("\r", end="")

        # Tampilkan waktu dan umur
        print(f"Waktu sekarang: {waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')} | Umur: {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari} hari.", end="")

        # Tunggu 1 detik sebelum memperbarui kembali
        time.sleep(1)

def main():
    print("\n------------------------|APLIKASI PENGHITUNG  UMUR|------------------------\n")
    print("(format DD-MM-YYYY)")
    # Masukkan tanggal lahir
    tanggal_lahir_str = input("Masukkan tanggal lahir : ")
    tanggal_lahir = datetime.strptime(tanggal_lahir_str, '%d-%m-%Y')

    print("\n  ------------------------|HASIL PENGHITUNG UMUR|------------------------\n")
    # Jalankan fungsi untuk menampilkan waktu dan umur secara real-time
    tampilkan_waktu_umur(tanggal_lahir)

if __name__ == "__main__":
    main()
