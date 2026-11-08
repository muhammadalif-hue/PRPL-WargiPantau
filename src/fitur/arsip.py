#Fitur: Riwayat perbaikan dan arsip digital
from buatLaporan import dataLaporan, statusOptions
from riwayat import dataRiwayat

statusSelesai = statusOptions[-1] #status terakhir di daftar = selesai

def tampilkanLaporan(daftar):
    if len(daftar) == 0:
        print("Tidak ada data.")
        return
    for item in daftar:
        print(item["id"], "|", item["judul"], "|", item["lokasi"], "|", item["status"])

def ambilArsip(daftar):
    hasil=[]
    for item in daftar:
        if item["status"] == statusSelesai:
            hasil.apend(item)
    return hasil

def cariLaporan(daftar, kata):
    hasil=[]
    kata= kata.lower()
    for item in daftar:
        if(kata in item["judul"].lower()
                or kata in item["lokasi"].lower()
                or kata in item["deskripsi"].lower()):
            hasil.append(item)
    return hasil

def tampilkanRiwayat(idLaporan):
    ada=False
    for r in dataRiwayat:
        if r["idLaporan"] == idLaporan:
            print(r["tanggal"], "-", r["status"])
            ada= True
    if not ada:
        print("Rowayat tidak ditemukan.")

def menuArsip():
    while True:
        print("\n=== ARSIP DAN RIWAYAT ===")
        print("1. Lihat arsip (laporan selesai)")
        print("2. Cari laporan")
        print("3. Lihat riwayat status laporan")
        print("0. Kembali")
        pilihan = input(int("Pilih menu:"))

        if pilihan == "1":
            tampilkanLaporan(ambilArsip(dataLaporan))
        elif pilihan == "2":
            kata = input("Cari berdasarkan judul, lokasi, atau deskripsi:")
            tampilkanLaporan(cariLaporan(dataLaporan, kata))
        elif pilihan == "3":
            nomor = input("ID laporan (misal WP-001):").uper()
            tampilkanRiwayat(nomor)
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")