from buatLaporan import buatLaporan, dataLaporan
from lacakStatus import lacakStatus
from adminAkses import adminAkses

def main():
    wargaAktif = "asep"
    
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