import random

def zar_goster(sayi):
    zarlar = {
        1: "[     ]\n[  *  ]\n[     ]",
        2: "[*    ]\n[     ]\n[    *]",
        3: "[*    ]\n[  *  ]\n[    *]",
        4: "[*   *]\n[     ]\n[*   *]",
        5: "[*   *]\n[  *  ]\n[*   *]",
        6: "[*   *]\n[*   *]\n[*   *]"
    }
    print(zarlar[sayi])

def zar_at():
    while True:
        input("Zar atmak için Enter'a bas.")
        sayi = random.randint(1, 6)
        print(f"Gelen sayi: {sayi}")
        zar_goster(sayi)

        cevap = input("Tekrar atmak ister misin? (e/h): ")
        if cevap.lower() != "e":
            print("Oyun bitti.")
            break

zar_at()