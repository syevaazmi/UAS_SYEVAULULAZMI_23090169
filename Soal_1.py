def main():
    Mahasiswa = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        
        student = {"NIM": nim, "Nama": nama}
        Mahasiswa.append(student)
        
        Tambah_Lagi = input("Ingin Tambah Lagi? (ya/tidak): ").lower()
        if Tambah_Lagi != 'ya':
            break

    print("\nData Mahasiswa:")
    for student in Mahasiswa:
        print(f"NIM: {student['NIM']}, Nama: {student['Nama']}")

if __name__ == "__main__":
    main()
