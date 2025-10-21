# Struktur data siswa sebagai dictionary
data_lagu = []

# Fungsi input data siswa
def input_siswa():
    nama = input("Masukkan nama siswa: ")
    try:
        nilai = float(input("Masukkan nilai: "))
    except ValueError:
        print("Nilai harus berupa angka.")
        return

    status = "Lulus" if nilai >= 75 else "Tidak Lulus"
    data_siswa.append({
        "nama": nama,
        "nilai": nilai,
        "status": status
    })
    print("Data berhasil ditambahkan.")

# Fungsi edit data siswa
def edit_siswa():
    if not data_siswa:
        print("Tidak ada data untuk diedit.")
        return

    tampilkan_laporan()

    try:
        index = int(input(f"Masukkan nomor siswa yang akan diedit (1-{len(data_siswa)}): "))
        if index < 1 or index > len(data_siswa):
            print("Nomor siswa tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    nama = input("Masukkan nama baru: ")
    try:
        nilai = float(input("Masukkan nilai baru: "))
    except ValueError:
        print("Nilai harus berupa angka.")
        return

    status = "Lulus" if nilai >= 75 else "Tidak Lulus"
    data_siswa[index - 1] = {
        "nama": nama,
        "nilai": nilai,
        "status": status
    }
    print("Data siswa berhasil diedit.")

# Fungsi hapus data siswa
def hapus_siswa():
    if not data_siswa:
        print("Tidak ada data untuk dihapus.")
        return

    tampilkan_laporan()

    try:
        index = int(input(f"Masukkan nomor siswa yang akan dihapus (1-{len(data_siswa)}): "))
        if index < 1 or index > len(data_siswa):
            print("Nomor siswa tidak valid.")
            return
    except ValueError:
        print("Input harus berupa angka.")
        return

    del data_siswa[index - 1]
    print("Data siswa berhasil dihapus.")

# Fungsi tampilkan laporan
def tampilkan_laporan():
    if not data_siswa:
        print("Tidak ada data siswa yang tersedia.")
        return

    print("\n--- Laporan Data Siswa ---")
    print("{:<5} | {:<20} | {:<10} | {:<15}".format("No", "Nama", "Nilai", "Status"))
    print("-" * 60)

    for i, siswa in enumerate(data_siswa):
        print("{:<5} | {:<20} | {:<10.2f} | {:<15}".format(
            i + 1, siswa["nama"], siswa["nilai"], siswa["status"]
        ))

# Fungsi utama (menu)
def main():
    while True:
        print("\n=== Aplikasi Pendaftaran Siswa ===")
        print("1. Input Data Siswa")
        print("2. Edit Data Siswa")
        print("3. Hapus Data Siswa")
        print("4. Tampilkan Laporan")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            input_siswa()
        elif pilihan == "2":
            edit_siswa()
        elif pilihan == "3":
            hapus_siswa()
        elif pilihan == "4":
            tampilkan_laporan()
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.")

# Jalankan program
if _name_ == "_main_":
    main()