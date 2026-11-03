#Tempat menyimpan riwayat perubahan status (dipakai bersama)
import datetime

dataRiwayat = []

def catatRiwayat(idLaporan, status):
    dataRiwayat.append({
        "idLaporan": idLaporan,
        "status": status,
        "tanggal": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    })