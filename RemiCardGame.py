import random

def draw_a_card():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10','Jack','Queen', 'King', 'Ace']
    suits = ['♠', '♥', '♦', '♣']
    
    rank = random.choice(ranks)
    suit = random.choice(suits)
    
    return (rank, suit)

def rank_value(rank, suit):
    order = {'2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9,'10':10,'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
    orders = {'♦':20,'♣':40,'♥':60,'♠':80}
    return order[rank] + orders[suit]

player_card = {
    1: draw_a_card(),
    2: draw_a_card(),
    3: draw_a_card()
}

pemain = input("Nama lu siapa: ")
print(f"=== Kartu Remi: {pemain} vs BOT ===")

def card_remaining():
    if not player_card:
        print("All cards have been selected. No more cards left.")
    else:
        print(f"===Kartu milik {pemain}===")
        for card_number, card in player_card.items():
            rankp, suitp = card
            print(f"{card_number}. {rankp} of {suitp}")

def main():
    pwin = 0
    swin = 0
    draw = 0
    while True:
            try:
                card_remaining()
                selection = int(input("Pilih kartu yang lu punya (1 - 3): "))
                if selection in player_card:
                    prank, psuit = player_card[selection]
                    system_card = draw_a_card()
                    syrank, sysuit = system_card
                    print(f"Lu milih: {prank} of {psuit}")
                    print(f"Kartu BOT: {syrank} of {sysuit}")
                    player_val = rank_value(prank, psuit)
                    system_val = rank_value(syrank, sysuit)
                    if player_val > system_val:
                        print(f"{pemain} menang!")
                        del player_card[selection]
                        pwin += 1
                    elif player_val < system_val:
                        print("BOT menang!")
                        del player_card[selection]
                        swin += 1
                    else:
                        print("SERI!!")
                        del player_card[selection]
                        draw += 1

                    if not player_card:
                        print("Semua kartu udh kepake. Kartu lu habis.")
                        print(f"{pemain} Menang: {pwin} kali, BOT Menang: {swin} kali, Seri: {draw} kali")
                        print("Terima Kasih Telah Bermain y bng")
                        break
                else:
                    print("Pilihan tidak valid. pilih yng bener mw 1, 2, atau 3.")
            except ValueError:
                print("Salah input, tolong masukkan angka yng bener bre (1-3).")

if __name__ == "__main__":
    main()
