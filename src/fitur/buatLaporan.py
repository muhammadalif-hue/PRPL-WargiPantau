import datetime

# ini buat nyimpen data
dataLaporan = []
dataDraf = []

statusOptions = [
    "Laporan Masuk Boskuh",
    "Diverifikasi",
    "Dalam Proses Perbaikan",
    "Selesai"
]

def buatLaporan(namaPelapor):
    print("\nFormulir Laporan Kerusakan Fasilitas Umum")
    
    judulLaporan = input("Masukkan Judul Laporan        : ")
    lokasiKerusakan = input("Masukkan Lokasi Kerusakan     : ")
    deskripsiKerusakan = input("Masukkan Deskripsi Kerusakan  : ")
    lampiranFoto = input("Masukkan Path Lampiran Foto (misal: lampiran/rusak.jpg): ")
    
    print("\nKonfirmasi Pengiriman")
    print(f"Judul Laporan       : {judulLaporan}") ##ini urang rapihin biar jadi sama tea gening titik duanya
    print(f"Lokasi Kerusakan    : {lokasiKerusakan}")
    print(f"Deskripsi Kerusakan : {deskripsiKerusakan}")
    print(f"Lampiran Foto       : {lampiranFoto}")
    
    opsi = input("Apakah Anda ingin mengirim laporan sekarang? (y/n): ").lower()
    
    if opsi == 'y':
        idLaporan = f"WP-{len(dataLaporan) + 1:03d}" ## ini teh WP = WargiPantau,semacam kode resi kalo di paket mah kekk kode pelapor gitu
        laporan = {
            "id": idLaporan,
            "pelapor": namaPelapor,
            "judul": judulLaporan,
            "lokasi": lokasiKerusakan,
            "deskripsi": deskripsiKerusakan,
            "foto": lampiranFoto if lampiranFoto else "Tidak ada",
            "status": "Laporan Masuk, Wargi!",
            "tanggal": datetime.datetime.now().strftime("%Y-%m-%d %H:%M") #data waktu sekarang, biar tau kapan laporannya dikirim
        }
        dataLaporan.append(laporan)
        print(f"\n[SUKSES] Laporan berhasil dikirim dengan ID: {idLaporan}")
    else:
        # kalo dibatalian, kesimpen di draf
        draf = {
            "judul": judulLaporan,
            "lokasi": lokasiKerusakan,
            "deskripsi": deskripsiKerusakan,
            "foto": lampiranFoto
        }
        dataDraf.append(draf)
        print("\n[INFO] Pengiriman dibatalkan. Laporan telah disimpan sebagai DRAF.")
    
    
    