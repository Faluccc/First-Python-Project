def konversi_suhu(nilai, dari, ke):
    # Konversi nilai suhu dari skala 'dari' ke Celsius terlebih dahulu
    if dari == 'C':
        celsius = nilai
    elif dari == 'F':
        celsius = (nilai - 32) * 5 / 9
    elif dari == 'K':
        celsius = nilai - 273.15
    elif dari == 'R':
        celsius = nilai * 5 / 4
    else:
        raise ValueError("Satuan asal salah bng")

    # Konversi dari Celsius ke skala tujuan
    if ke == 'C':
        return celsius
    elif ke == 'F':
        return (celsius * 9 / 5) + 32
    elif ke == 'K':
        return celsius + 273.15
    elif ke == 'R':
        return celsius * 4 / 5
    else:
        raise ValueError("Satuan tujuan salah bng")

def tampilkan_menu():
    print("Pilih satuan suhunya bre:")
    print("C - Celsius")
    print("F - Fahrenheit")
    print("K - Kelvin")
    print("R - Reamur")

def main():
    while True:
        print("Program Konversi Suhu")
        tampilkan_menu()
        dari = input("Masukkan satuan asal (C/F/K/R): ").upper()
        ke = input("Masukkan satuan tujuan (C/F/K/R): ").upper()

        if dari not in ['C', 'F', 'K', 'R'] or ke not in ['C', 'F', 'K', 'R']:
            print("Satuan tidak valid, coba lagi bng.")
            continue

        try:
            nilai = float(input("Masukkan nilai suhu: "))
        except ValueError:
            print("Input nilai suhu tidak valid, coba lagi bng.")
            continue

        try:
            hasil = konversi_suhu(nilai, dari, ke)
            print(f"{nilai} {dari} = {hasil:.2f} {ke}")
        except ValueError as e:
            print(e)

        lanjut = input("Apakah ingin melakukan konversi lagi? (mw/ga): ").lower()
        if lanjut != 'mw':
            print("Terima kasih bre telah menggunakan program konversi suhu ini!")
            break

if __name__ == "__main__":
    main()
