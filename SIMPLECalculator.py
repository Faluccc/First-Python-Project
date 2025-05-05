def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan!"
    return x / y

def kalkulator():
    while True:
        print("Kalkulator Sederhana")
        print("====================")
        print("Pilih operasi: ")
        print("1. Tambah (+)")
        print("2. Kurang (-)")
        print("3. Kali (*)")
        print("4. Bagi (/)")

        pilihan = input("Masukkan Nomor Pengoperasian (1/2/3/4): ")

        if pilihan in ['1', '2', '3', '4']:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Error: Masukkan angka yang valid!")
                return

            if pilihan == '1':
                hasil = tambah(angka1, angka2)
                print(f"Hasil: {angka1} + {angka2} = {hasil}")
            elif pilihan == '2':
                hasil = kurang(angka1, angka2)
                print(f"Hasil: {angka1} - {angka2} = {hasil}")
            elif pilihan == '3':
                hasil = kali(angka1, angka2)
                print(f"Hasil: {angka1} * {angka2} = {hasil}")
            elif pilihan == '4':
                hasil = bagi(angka1, angka2)
                print(f"Hasil: {angka1} / {angka2} = {hasil}")
        else:
            print("Pilihan tidak valid!")
        
        lanjut = input("Apakah ingin melanjutkan? (mw/ga): ").lower()
        if lanjut == "ga":
            print("Terima kasih telah menggunakan kalkulator!")
            break

if __name__ == "__main__":
    kalkulator()
