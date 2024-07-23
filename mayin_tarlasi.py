#RUKİYE UÇAR
#2110011057

import random

hata = 0

# Bu fonksiyon, kullanıcının kazanıp kazanmadığını belirler..
def kazandin_mi():
    for r in range(satir):
        for c in range(satir):
            if board[c][r] == "?":
                return False
    return True

while True:
    while True:
        satir = int(input("\n\nBoyut Girin (en az : 10): "))
        if satir < 10:
            print("\nMaalesef" + " :(" + "\nGeçersiz Boyut\n")
            continue
        else:
            break

    board = [["?" for c in range(satir)] for r in range(satir)]

    mod = input("\nMod Girin: (Gizli: 'gizli' or açık: 'açık') ")

    mayin_numarasi = int(((satir ** 2) * 30) / 100)

    mDizi = []
    sayac = 0
    kontrol = 0
    while sayac < mayin_numarasi:
        kontrol += 1
        msatir = random.randint(0, satir - 1)
        msutun = random.randint(0, satir - 1)
        if board[msutun][msatir] != 'X':
            board[msutun][msatir] = 'X'
            mList = [msutun, msatir]
            mDizi.append(mList)
            sayac += 1
    
    puan = 0

    # ----------------------------------------------------------------
    kontrol2 = True
    while   kontrol2:
        if mod == "gizli":
            print("\n----------------------MAYIN TARLASI----------------------\n")
            print("\t(Mayın Numarası:{})".format(mayin_numarasi), "\n\n")
            print("\t", *range(satir))
            print("   ", "_ " * (satir + 1))

            for r in range(satir):
                oyun_alani = []
                for c in range(satir):
                    if mod == "gizli" and board[c][r] == "X":
                        oyun_alani.append("?")
                    else:
                        oyun_alani.append(board[c][r])
                print(r, " |", *oyun_alani, "|")

            print("   ", "_ " * (satir + 1))
        elif mod == "açık":
            print("\n----------------------MAYIN TARLASI----------------------\n")
            print("\t(Mayın Numarası:{})".format(mayin_numarasi), "\n\n")
            print("\t", *range(satir))
            print("   ", "_ " * (satir + 1))

            for r in range(satir):
                oyun_alani = []
                for c in range(satir):
                    if mod == "gizli" and board[c][r] == "X":
                        oyun_alani.append("?")
                    else:
                        oyun_alani.append(board[c][r])
                print(r, " |", *oyun_alani, "|")

            print("   ", "_ " * (satir + 1))
            mod = input("\nOyuna Geri Dönmek İçin 'gizli' Yaz ")
            continue
        else:
            mod = input("\nBöyle Bir Mod Yok. Lütfen Tekrar kontrol: (gizli mod: 'gizli' or açık mod: 'açık') ")
            continue
        m_satir = int(input("\nsatir: "))
        m_sutun = int(input("\nsütun: "))
        print("\n")
        if m_satir >= satir or m_sutun >= satir:
            print("rakam çok büyük")
            hata = 1
        elif board[m_sutun][m_satir] != "?" and board[m_sutun][m_satir] != "X":
            print("başka bir konum seçin")
            hata = 1
        else:
            hata = 0
            puan += 1

            numara = 0
            gizli = 0

            # karoya bomba yerleştirilmişse, işleve geri döner
            if board[m_sutun][m_satir] == "X":
                numara = 9
                karo_sayisi = numara
            else:
                # kod mevcut kutucuğun etrafına yerleştirilmiş bombaları arar
                for i in range(m_sutun - 1, m_sutun + 2):
                    for j in range(m_satir - 1, m_satir + 2):
                        if i < 0 or j < 0 or i == satir or j == satir:
                            pass
                        elif m_sutun == i and m_satir == j and board[i][j] == "X":
                            pass
                        elif board[i][j] == 'X':
                            numara += 1
                        elif board[i][j] == '?':
                            gizli += 1
                        else:
                            pass

                karo_sayisi = numara


            # eğer bambaysa
            if karo_sayisi == 9:
                kontrol2 = False

            # karo 0-8 arasındaysa karoyu aç
            elif 0 <= karo_sayisi <= 8:
                board[m_sutun][m_satir] = chr(48 + karo_sayisi)
                kontrol2 = True

        if hata != 1:
            if not  kontrol2:
                print("BOOOM!!!!\nKAYBETTİN\nPUANIN:", (puan - 1) * 10)
                print("\n----------------------MAYIN TARLASI----------------------\n")
                print("\t(Mayın Numarası:{})".format(mayin_numarasi), "\n\n")
                print("\t", *range(satir))
                print("   ", "_ " * (satir + 1))

                for r in range(satir):
                    oyun_alani = []
                    for c in range(satir):
                        oyun_alani.append(board[c][r])
                    print(r, " |", *oyun_alani, "|")

                print("   ", "_ " * (satir + 1))
                break
            elif kazandin_mi():
                print("TEBRİKLER!\nKAZANDIN\nPUANIN:", puan * 10)
                print("\n----------------------MAYIN TARLASI----------------------\n")
                print("\t(MAYIN NUMARASI:{})".format(mayin_numarasi), "\n\n")
                print("\t", *range(satir))
                print("   ", "_ " * (satir + 1))

                for r in range(satir):
                    oyun_alani = []
                    for c in range(satir):
                        oyun_alani.append(board[c][r])
                    print(r, " |", *oyun_alani, "|")

                print("   ", "_ " * (satir + 1))
                break
    end = input("\nyeni oyun için 'n', çıkış için 'e' tıklayın: ")
    if end == "n":
        continue
    elif end == "e":
        break
