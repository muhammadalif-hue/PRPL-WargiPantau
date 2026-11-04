from fitur.buatLaporan import dataLaporan, statusOptions

def verifikasiEskalasi():
    print("\n[VERIFIKASI & ESKALASI LAPORAN]")
    
    if not dataLaporan:
        print("\nBelum ada laporan masuk ges.")
        return
    
    for x in dataLaporan:
        if "tingkat" not in x:
            x["tingkat"] = 1
            
        print(f"[{x['id']}] {x['judul']} | Status: {x['status']} | Level Eskalasi: Level {x['tingkat']}")
        
    idTarget = input("\nMasukkan ID Laporan yang ingin diproses: ").strip()
    target = next((x for x in dataLaporan if x['id'].lower() == idTarget.lower()), None)
    
    if not target:
        print("\n[ERROR] Laporan dengan ID tersebut tidak ditemukan.")
        return

    print(f"\nMemproses Laporan: [{target['id']}] {target['judul']}")
    print("1. Verifikasi Status Laporan")
    print("2. Eskalasi Tingkat Laporan (Naikkan Kewenangan)")
    
    pilihanAksi = input("Pilih menu aksi (1/2): ").strip()
    
    if pilihanAksi == '1':
        print("\nPilih Status / Hasil Verifikasi Baru:")
        for idx, stat in enumerate(statusOptions, 1):
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
            
    elif pilihanAksi == '2':
        print(f"\nTingkat Eskalasi Saat Ini: Level {target.get('tingkat', 1)}")
        print("Pilih Level Tujuan Eskalasi:")
        print("1. Level 1 (Kecamatan / Kelurahan)")
        print("2. Level 2 (Dinas Terkait Kabupaten/Kota)")
        
        try:
            levelTujuan = int(input("Masukkan pilihan level eskalasi (1-2): "))
            if 1 <= levelTujuan <= 2:
                target['tingkat'] = levelTujuan
                target['status'] = f"Dieskalasi ke Level {levelTujuan}"
                print(f"\n[SUKSES] Laporan {target['id']} berhasil dieskalasi ke Level {levelTujuan}.")
            else:
                print("\n[ERROR] Level eskalasi tidak valid.")
        except ValueError:
            print("\n[ERROR] Input harus berupa angka.")
    else:
        print("\n[ERROR] Pilihan menu tidak valid.")