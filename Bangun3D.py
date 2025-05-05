import math

def volume_kubus():
    sisi = float(input("Masukkan panjang sisi kubus: "))
    volume = sisi ** 3
    print(f"Volume kubus adalah {volume:.2f}")

def volume_balok():
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))
    volume = panjang * lebar * tinggi
    print(f"Volume balok adalah {volume:.2f}")

def volume_silinder():
    jari_jari = float(input("Masukkan jari-jari alas silinder: "))
    tinggi = float(input("Masukkan tinggi silinder: "))
    volume = math.pi * jari_jari ** 2 * tinggi
    print(f"Volume silinder adalah {volume:.2f}")

def volume_bola():
    jari_jari = float(input("Masukkan jari-jari bola: "))
    volume = (4/3) * math.pi * jari_jari ** 3
    print(f"Volume bola adalah {volume:.2f}")

def main():
    while True:
        print("Pilih bangun tiga dimensi yang ingin dihitung volumenya bre:")
        print("1. Kubus")
        print("2. Balok")
        print("3. Silinder")
        print("4. Bola")
        print("5. Udhan bng")
        print("(DALAM SATUAN CM!!)")

        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == '1':
            volume_kubus()
        elif pilihan == '2':
            volume_balok()
        elif pilihan == '3':
            volume_silinder()
        elif pilihan == '4':
            volume_bola()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, masukin pilihan yng bener bjir.")

if __name__ == "__main__":
    main()
