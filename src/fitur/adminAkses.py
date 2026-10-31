from fitur.buatLaporan import dataLaporan, statusOptions

def adminAkses():
    print("\n[ADMIN] Update Status Laporan")
    
    if not dataLaporan:
        print("\nBelum ada laporan masuk ges")
        return
    
    for x in dataLaporan:
        print(f"[{x['id']}] {x['judul']} - Status Saat Ini: {x['status']}")
        
    idTarget = input("\nMasukkan ID Laporan yang ingin diubah statusnya: ").strip()
    target = next((x for x in dataLaporan if x['id'].lower() == idTarget.lower()), None)
    
    if target:
        print("\nPilih Status Baru:")
        for idx, stat in enumerate(statusOptions, 1): ##idx = index dari statusOptions(di anuan buatLaporan.py), stat = status
            print(f"{idx}. {stat}")
        
        try:
            pilihanStatus = int(input("Masukkan nomor status baru: "))
            if 1 <= pilihanStatus <= len(statusOptions):
                target['status'] = statusOptions[pilihanStatus - 1]
                print(f"\n[SUKSES] Status laporan {target['id']} berhasil diubah menjadi '{target['status']}'")
            else:
                print("\n[ERROR] Pilihan status tidak valid.")
        except ValueError:
            print("\n[ERROR] Input harus berupa angka.")