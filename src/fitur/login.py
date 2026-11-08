# Fitur login WargiPantau (database dummy: data/pengguna.csv)
import csv
import hashlib
import os

folderData = "data"
berkasPengguna = os.path.join(folderData, "pengguna.csv")

kolomPengguna = ["id_pengguna", "nik", "nama_lengkap", "nama_pengguna", "kata_sandi",
                 "peran", "wilayah", "hak_akses", "nomor_whatsapp", "status_akun"]


def enkripsiSandi(sandi):
    return hashlib.sha256(sandi.encode("utf-8")).hexdigest()


def bacaCsv(berkas):
    with open(berkas, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def tulisCsv(berkas, kolom, daftarBaris):
    with open(berkas, "w", newline="", encoding="utf-8") as f:
        penulis = csv.DictWriter(f, fieldnames=kolom)
        penulis.writeheader()
        penulis.writerows(daftarBaris)


def siapkanDataLogin():
    """Membuat data awal jika berkas CSV belum ada (berkas yang sudah ada tidak ditimpa)."""
    os.makedirs(folderData, exist_ok=True)

    if not os.path.isfile(berkasPengguna):
        tulisCsv(berkasPengguna, kolomPengguna, [
            {"id_pengguna": "1", "nik": "3273011001700001", "nama_lengkap": "Hendra Wijaya",
             "nama_pengguna": "ketuarw", "kata_sandi": enkripsiSandi("rw12345"), "peran": "Superadmin",
             "wilayah": "", "hak_akses": "semua", "nomor_whatsapp": "081200000001", "status_akun": "Aktif"},
            {"id_pengguna": "2", "nik": "3273011505850002", "nama_lengkap": "Budi Santoso",
             "nama_pengguna": "admin_rt01", "kata_sandi": enkripsiSandi("rt12345"),
             "peran": "Admin/Pengelola", "wilayah": "1", "hak_akses": "verifikasi;eskalasi;update_status",
             "nomor_whatsapp": "081200000002", "status_akun": "Aktif"},
            {"id_pengguna": "3", "nik": "3273012002900003", "nama_lengkap": "Siti Aminah",
             "nama_pengguna": "siti", "kata_sandi": enkripsiSandi("siti123"), "peran": "Pelapor",
             "wilayah": "1", "hak_akses": "", "nomor_whatsapp": "081200000003", "status_akun": "Aktif"},
            {"id_pengguna": "4", "nik": "3273012503950004", "nama_lengkap": "Dewi Lestari",
             "nama_pengguna": "dewi", "kata_sandi": enkripsiSandi("dewi123"), "peran": "Pelapor",
             "wilayah": "2", "hak_akses": "", "nomor_whatsapp": "081200000004", "status_akun": "Aktif"},
        ])


def login():
    """Mengembalikan data pengguna (dict) jika login berhasil, atau None jika gagal."""
    print("\nLOGIN WARGIPANTAU")
    for percobaan in range(1, 4):
        namaPengguna = input("Nama pengguna : ").strip()
        sandi = input("Kata sandi    : ").strip()

        for p in bacaCsv(berkasPengguna):
            if p["nama_pengguna"] == namaPengguna and p["kata_sandi"] == enkripsiSandi(sandi):
                if p["status_akun"] != "Aktif":
                    print("\n[ERROR] Akun nonaktif. Hubungi Superadmin.")
                    return None
                print(f"\n[SUKSES] Login berhasil. Selamat datang, {p['nama_lengkap']} ({p['peran']}).")
                return p

        print(f"\n[ERROR] Nama pengguna atau kata sandi salah (percobaan {percobaan}/3).")

    print("Login gagal 3 kali. Kembali ke menu awal.")
    return None
