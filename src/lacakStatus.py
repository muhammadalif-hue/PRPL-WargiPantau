def lacakStatus(namaPelapor, dataLaporan):
    print("\nDaftar Laporan Anda:")
    laporanDitemukan = False
    for laporan in dataLaporan:
        if laporan["pelapor"] == namaPelapor:
            laporanDitemukan = True
            print(f"\n- ID Laporan: {laporan['id']}")
            print(f"- Judul: {laporan['judul']}")
            print(f"- Lokasi: {laporan['lokasi']}")
            print(f"- Deskripsi: {laporan['deskripsi']}")
            print(f"- Lampiran Foto: {laporan['foto']}")
            print(f"- Status: {laporan['status']}")
            print(f"- Tanggal: {laporan['tanggal']}\n")
    
    if not laporanDitemukan:
        print("Anda belum mengirimkan laporan apapun.")
        
    laporanSaya = [x for x in dataLaporan if x['pelapor'] == namaPelapor]
    
    if not laporanSaya:
        print("\nBelum ada laporan yang dikirimkan.")
        return
    
    print(f"{'ID':<8} | {'Judul Laporan':<20} | {'Tanggal':<16} | {'Status':<18}") #ini gimana nya gais biar kaya rapih gitu biar jadi tabel
    for laporan in laporanSaya:
        print(f"{laporan['id']:<8} | {laporan['judul']:<20} | {laporan['tanggal']:<16} | {laporan['status']:<18}")
        
    idCari = input("\nMasukkan ID Laporan untuk detail lengkap (atau tekan Enter untuk kembali): ").strip()
    if idCari:
        detail = next((x for x in laporanSaya if x['id'].lower() == idCari.lower()), None)
        if detail:
        #ini aku bikin jadi tabel biar lebih rapi
            print("\nDETAIL LAPORAN")
            print(f"\nID Laporan : {detail['id']}")
            print(f"Tanggal    : {detail['tanggal']}")
            print(f"Judul      : {detail['judul']}")
            print(f"Lokasi     : {detail['lokasi']}")
            print(f"Deskripsi  : {detail['deskripsi']}")
            print(f"Foto       : {detail['foto']}")
            print(f"STATUS     : [{detail['status']}]")
        else:
            print("\n[ERROR] ID Laporan tidak ketemu")