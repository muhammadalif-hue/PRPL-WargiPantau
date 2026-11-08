##NOTEESSSSSSS! 
# ini jadi file utama, nanti di run nya dari sini
# kalo misalnya mau bikin fitur, dibikin function baru di file baru, terus di import ke main.py, biar rapih ajaa hehee

from fitur.login import siapkanDataLogin, login
from fitur.buatLaporan import buatLaporan, dataLaporan
from fitur.lacakStatus import lacakStatus
from fitur.adminAkses import adminAkses
from fitur.verifikasiEskalasi import verifikasiEskalasi
from fitur.arsip import menuArsip

def menuUtama(pengguna):
    # wargaAktif sekarang diambil dari hasil login (bukan "asep" lagi)
    # pakai nama_pengguna karena unik, jadi lacakStatus gak ketuker antar warga
    wargaAktif = pengguna["nama_pengguna"]
    
    # pembagian hak akses: menu 1-2 buat Pelapor, menu 3-4 buat Admin/Pengelola dan Superadmin
    adalahPelapor = pengguna["peran"] == "Pelapor"
    
    while True:
        print("\nWargiPantau 0.1")
        print(f"Login sebagai: {pengguna['nama_lengkap']} ({pengguna['peran']})")
        print("1. Buat Laporan Baru")
        print("2. Lacak Status Laporan Saya")
        print("3. [ADMIN] Update Status Laporan")
        print("4. [ADMIN] Verifikasi & Eskalasi Laporan")
        print("5. Arsip dan Riwayat")
        print("6. Logout")
        
        pilihanMenu = input("Pilih menu (1-6): ")
        
        if pilihanMenu == '1':
            if adalahPelapor:
                buatLaporan(wargaAktif)
            else:
                print("\n[DITOLAK] Menu ini hanya untuk Pelapor (warga).")
        elif pilihanMenu == '2':
            if adalahPelapor:
                lacakStatus(wargaAktif, dataLaporan)
            else:
                print("\n[DITOLAK] Menu ini hanya untuk Pelapor (warga).")
        elif pilihanMenu == '3':
            if not adalahPelapor:
                adminAkses()
            else:
                print("\n[DITOLAK] Menu ini hanya untuk Admin/Pengelola dan Superadmin.")
        elif pilihanMenu == '4':
            if not adalahPelapor:
                verifikasiEskalasi()
            else:
                print("\n[DITOLAK] Menu ini hanya untuk Admin/Pengelola dan Superadmin.")
        elif pilihanMenu == '5':
            menuArsip(pengguna)
        elif pilihanMenu == '6':
            print("\nAnda telah logout.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            
def main():
    siapkanDataLogin()
    
    while True:
        print("\nWargiPantau 0.1")
        print("1. Login")
        print("0. Keluar")
        
        pilihanAwal = input("Pilih menu (0-1): ")
        
        if pilihanAwal == '1':
            pengguna = login()
            if pengguna:
                menuUtama(pengguna)
        elif pilihanAwal == '0':
            print("\nTerima kasih telah menggunakan WargiPantau. Hatur nuhun sadayanaa!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()
