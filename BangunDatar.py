import math

def hitung_luas_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = (alas * tinggi) / 2
    print(f"Luas segitiga adalah {luas:.2f}")

def hitung_luas_persegi_panjang():
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    print(f"Luas persegi panjang adalah {luas:.2f}")

def hitung_luas_lingkaran():
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = math.pi * jari_jari ** 2
    print(f"Luas lingkaran adalah {luas:.2f}")

def hitung_luas_persegi():
    sisi = float(input("Masukkan sisi persegi: "))
    luas = sisi * sisi
    print(f"Luas persegi adalah {luas:.2f}")

def main():
    while True:
        print("Pilih bangun datar yang ingin dihitung luasnya bre:")
        print("1. Segitiga")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Persegi")
        print("5. Wes udhan ah")
        print("(INI DALAM SATUAN CM YA)")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            hitung_luas_segitiga()
        elif pilihan == '2':
            hitung_luas_persegi_panjang()
        elif pilihan == '3':
            hitung_luas_lingkaran()
        elif pilihan == '4':
            hitung_luas_persegi()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, masukin pilihan yng bener bjir.")

if __name__ == "__main__":
    main()
