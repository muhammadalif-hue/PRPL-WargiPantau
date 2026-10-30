##NOTEESSSSSSS! 
# ini jadi file utama, nanti di run nya dari sini, biar bisa nyambungin semua file yang ada di src
# kalo misalnya mau bikin fitur, dibikin function baru di file baru, terus di import ke main.py, biar rapih ajaa hehee

from buatLaporan import buatLaporan, dataLaporan
from lacakStatus import lacakStatus
from adminAkses import adminAkses

def main():
    wargaAktif = "asep" ##ges ini warga aktif, nanti bisa diganti sesuai login user nyak, jujur masih bingung nyambunginnya sama data user ketika login
    
    while True:
        print("\nWargiPantau")
        print("1. Buat Laporan Baru")
        print("2. Lacak Status Laporan Saya")
        print("3. [ADMIN] Update Status Laporan")
        print("4. Keluar")
        
        pilihanMenu = input("Pilih menu (1-4): ")
        
        if pilihanMenu == '1':
            buatLaporan(wargaAktif)
        elif pilihanMenu == '2':
            lacakStatus(wargaAktif, dataLaporan)
        elif pilihanMenu == '3':
            adminAkses()
        elif pilihanMenu == '4':
            print("\nTerima kasih telah menggunakan WargiPantau. Hatur nuhun sadayanaa!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()