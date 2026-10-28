# PRPL-WargiPantau
# Platform Pelaporan dan Pemantauan Fasilitas Umum (Prototipe CLI)

Aplikasi baris perintah (CLI) untuk membantu warga RW 11 Desa Cibiru Wetan melaporkan kerusakan fasilitas umum dan memantau tindak lanjutnya, sehingga laporan tidak lagi terlupakan.

Proyek mata kuliah Pengantar Rekayasa Perangkat Lunak, Dasar Pemrograman, dan Literasi Teknologi Informasi dan Komunikasi, Kelompok 6 (1A).

## Latar belakang
Saat ini warga melapor langsung atau lewat grup WhatsApp tanpa pencatatan, sehingga banyak laporan terlupakan dan warga sulit memantau tindak lanjutnya. Proyek ini mencatat dan melacak laporan secara terpusat.

## Peran pengguna
- **Superadmin** (Ketua dan Sekretaris RW): mengelola data warga dan hak akses, mendelegasikan laporan, menetapkan tenggat.
- **Admin/Pengelola** (pengurus RT dan pemuda): memverifikasi, mengeskalasi, dan memperbarui status laporan.
- **Pelapor** (warga): mengirim laporan dan memantau statusnya.

## Fitur
- Penyiapan akun warga dan login
- Pelaporan dengan lampiran foto, serta draf otomatis jika pengiriman gagal
- Verifikasi dan eskalasi berjenjang (RT ke RW)
- Pelacakan status: Laporan Masuk, Diverifikasi, Proses Perbaikan, Selesai
- Notifikasi (disimulasikan di CLI)
- Hak akses bertingkat
- Chat per laporan antara warga dan petugas
- Riwayat perbaikan dan arsip digital

## Struktur folder
- `src/` kode program
- `docs/` dokumen SKPL dan flowmap
- `tests/` pengujian

## Catatan
Data warga bersifat pribadi, jadi file database tidak diunggah ke repo ini (lihat `.gitignore`).

## Anggota
Azril Muhammad Rizki, Fadia Azra Kadarisman, Muhammad Alif Al Fathir, Muhammad Farrel As Shafwan