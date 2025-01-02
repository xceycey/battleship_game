import random

karar = 1
while karar == 1:
    satirsay = 10
    sutunsay = 10
    kontrol1 = 0
    kontrol2 = 0
    kontrol3 = 0
    kontrol4 = 0
    atis = 0
    oyun= []
    oyunson =[]
    while 1:
        oyunboyutu= int(input("Oyun alani kaca kaclik olsun? (En az 10) "))
        if oyunboyutu<10:
            print("10 veya daha buyuk boyut giriniz.")
            continue
        oyun = ["?"] * oyunboyutu
        oyunson = ["?"] * oyunboyutu
        for i in range(oyunboyutu):
            oyun[i] = ["?"] * oyunboyutu
            oyunson[i] = ["?"] * oyunboyutu
        break
    hak = (oyunboyutu*oyunboyutu) // 3
    # 1lik gemiyi yerleştir
    satir1 = random.randint(1, satirsay)
    sutun1 = random.randint(1, sutunsay)
    oyun[satir1 - 1][sutun1 - 1] = "/"

    # 2lik gemiyi yerleştir
    while 1:
        satir2 = random.randint(1, satirsay)
        sutun2 = random.randint(1, sutunsay)
        if oyun[satir2 - 1][sutun2 - 1] == "?":
            while 1:
                yon2 = random.choice(["left", "right", "up", "down"])
                oyun[satir2 - 1][sutun2 - 1] = "/"
                if yon2 == "left":
                    if sutun2 != 1 and oyun[satir2 - 1][sutun2 - 2] == "?":
                        oyun[satir2 - 1][sutun2 - 2] = "/"
                        break
                    else:
                        continue
                elif yon2 == "right":
                    if sutun2 != oyunboyutu and oyun[satir2 - 1][sutun2] == "?":
                        oyun[satir2 - 1][sutun2] = "/"
                        break
                    else:
                        continue
                elif yon2 == "up":
                    if satir2 != 1 and oyun[satir2 - 2][sutun2 - 1] == "?":
                        oyun[satir2 - 2][sutun2 - 1] = "/"
                        break
                    else:
                        continue
                elif yon2 == "down":
                    if satir2 != oyunboyutu and oyun[satir2][sutun2 - 1] == "?":
                        oyun[satir2][sutun2 - 1] = "/"
                        break
                    else:
                        continue
                break
            break
        else:
            continue
    # 3lük gemiyi yerleştir
    while 1:
        satir3 = random.randint(1, satirsay)
        sutun3 = random.randint(1, sutunsay)
        if oyun[satir3 - 1][sutun3 - 1] == "?":
            while 1:
                yon3 = random.choice(["left", "right", "up", "down"])
                oyun[satir3 - 1][sutun3 - 1] = "/"
                if yon3 == "left":
                    if sutun3 != 1 and sutun3 != 2 and oyun[satir3 - 1][sutun3 - 2]=="?" and oyun[satir3 - 1][sutun3 - 3]=="?":
                        oyun[satir3 - 1][sutun3 - 2] = "/"
                        oyun[satir3 - 1][sutun3 - 3] = "/"
                        break
                    else:
                        continue
                elif yon3 == "right":
                    if sutun3 != oyunboyutu and sutun3 != oyunboyutu-1 and oyun[satir3 - 1][sutun3]=="?" and oyun[satir3 - 1][sutun3 + 1]=="?":
                        oyun[satir3 - 1][sutun3] = "/"
                        oyun[satir3 - 1][sutun3 + 1] = "/"
                        break
                    else:
                        continue
                elif yon3 == "up":
                    if satir3 != 1 and satir3 != 2 and oyun[satir3 - 2][sutun3 - 1]=="?" and oyun[satir3 - 3][sutun3 - 1]=="?":
                        oyun[satir3 - 2][sutun3 - 1] = "/"
                        oyun[satir3 - 3][sutun3 - 1] = "/"
                        break
                    else:
                        continue
                elif yon3 == "down":
                    if satir3!=oyunboyutu and satir3!=oyunboyutu-1 and oyun[satir3][sutun3 - 1]== "?" and oyun[satir3 + 1][sutun3 - 1]== "?":
                        oyun[satir3][sutun3 - 1] = "/"
                        oyun[satir3 + 1][sutun3 - 1] = "/"
                        break
                    else:
                        continue
                break
            break
        else:
            continue
    # 4lük gemiyi yerleştir
    while 1:
        satir4 = random.randint(1, satirsay)
        sutun4 = random.randint(1, sutunsay)
        if oyun[satir4 - 1][sutun4 - 1] == "?":
            while 1:
                yon4 = random.choice(["left", "right", "up", "down"])
                oyun[satir4 - 1][sutun4 - 1] = "/"
                if yon4 == "left":
                    if sutun4 != 1 and sutun4 != 2 and sutun4 != 3 and oyun[satir4 - 1][sutun4 - 2]=="?" and  oyun[satir4 - 1][sutun4 - 3]=="*" and oyun[satir4 - 1][sutun4 - 4]== "?":
                        oyun[satir4 - 1][sutun4 - 2] = "/"
                        oyun[satir4 - 1][sutun4 - 3] = "/"
                        oyun[satir4 - 1][sutun4 - 4] = "/"
                        break
                    else:
                        continue
                elif yon4 == "right":
                    if sutun4!=oyunboyutu and sutun4!=oyunboyutu-1 and sutun4!=oyunboyutu-2 and oyun[satir4 - 1][sutun4]=="?" and oyun[satir4 - 1][sutun4 + 1]=="?" and oyun[satir4 - 1][sutun4 + 2]=="?":
                        oyun[satir4 - 1][sutun4] = "/"
                        oyun[satir4 - 1][sutun4 + 1] = "/"
                        oyun[satir4 - 1][sutun4 + 2] = "/"
                        break
                    else:
                        continue
                elif yon4 == "up":
                    if satir4!=1 and satir4!=2 and satir4!=3 and oyun[satir4-2][sutun4-1]=="?" and oyun[satir4-3][sutun4-1]=="?" and oyun[satir4-4][sutun4-1]=="?":
                        oyun[satir4 - 2][sutun4 - 1] = "/"
                        oyun[satir4 - 3][sutun4 - 1] = "/"
                        oyun[satir4 - 4][sutun4 - 1] = "/"
                        break
                    else:
                        continue
                elif yon4 == "down":
                    if satir4!=oyunboyutu and satir4!=oyunboyutu-1 and satir4!=oyunboyutu-2 and oyun[satir4][sutun4-1]=="?" and oyun[satir4+1][sutun4-1]=="?" and oyun[satir4+2][sutun4-1]=="?":
                        oyun[satir4][sutun4 - 1] = "/"
                        oyun[satir4 + 1][sutun4 - 1] = "/"
                        oyun[satir4 + 2][sutun4 - 1] = "/"
                        break
                    else:
                        continue
                break
            break
        else:
            continue

    # gizli mod ve açık mod seç
    while 1:
        modsec= int(input("Gizli Mod icin 1 Acik Mod icin 2 giriniz: "))
        if modsec==1:
            for i in oyunson:
                print(*i)
            break
        if modsec==2:
            for i in oyun:
                print(*i)
            break
        else:
            print("Lutfen modu duzgun secin.")

    while hak != 0:
        girilensatir = int(input("Satir sayisi giriniz:"))
        girilensutun = int(input("Sutun sayisi giriniz:"))
        if oyunson[girilensatir - 1][girilensutun - 1] == "*" or oyunson[girilensatir - 1][girilensutun - 1] == "X":
            print("Lutfen daha once sectiginiz yeri tekrar secmeyin.")
            continue

        if oyun[girilensatir - 1][girilensutun - 1] == "/":
            print("Tebrikler bir gemi vurdunuz.")
            hak -= 1
            atis += 1
            oyunson[girilensatir - 1][girilensutun - 1] = "X"
        elif oyun[girilensatir - 1][girilensutun - 1] == "?":
            print("Maalesef isabet ettiremediniz.")
            hak -= 1
            atis += 1
            oyunson[girilensatir - 1][girilensutun - 1] = "*"
        # tüm gemiyi vurunca 'tebrikler bir gemi batırdınız' mesajı ver
        if kontrol1 == 0:
            if oyunson[satir1 - 1][sutun1 - 1] == "X":
                print("Tebrikler bir gemi batirdiniz.")
                kontrol1 = 1
        if kontrol2 == 0:
            if oyunson[satir2 - 1][sutun2 - 1] == "X":
                if yon2 == "left":
                    if oyunson[satir2 - 1][sutun2 - 2] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol2 = 1
                if yon2 == "right":
                    if oyunson[satir2 - 1][sutun2] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol2 = 1
                if yon2 == "up":
                    if oyunson[satir2 - 2][sutun2 - 1] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol2 = 1
                if yon2 == "down":
                    if oyunson[satir2][sutun2 - 1] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol2 = 1
        if kontrol3 == 0:
            if oyunson[satir3 - 1][sutun3 - 1] == "X":
                if yon3 == "left":
                    if oyunson[satir3 - 1][sutun3 - 2] == "X" and oyunson[satir3 - 1][sutun3 - 3] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol3 = 1
                if yon3 == "right":
                    if oyunson[satir3 - 1][sutun3] == "X" and oyunson[satir3 - 1][sutun3 + 1] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol3 = 1
                if yon3 == "up":
                    if oyunson[satir3 - 2][sutun3 - 1] == "X" and oyunson[satir3 - 3][sutun3 - 1] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol3 = 1
                if yon3 == "down":
                    if oyunson[satir3][sutun3 - 1] == "X" and oyunson[satir3 + 1][sutun3 - 1] == "X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol3 = 1
        if kontrol4 == 0:
            if oyunson[satir4 - 1][sutun4 - 1] == "X":
                if yon4 == "left":
                    if oyunson[satir4-1][sutun4-2]=="X" and oyunson[satir4-1][sutun4-3]=="X" and oyunson[satir4-1][sutun4-4]=="X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol4 = 1
                if yon4 == "right":
                    if oyunson[satir4-1][sutun4]=="X" and oyunson[satir4-1][sutun4+1]=="X" and oyunson[satir4-1][sutun4+2]=="X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol4 = 1
                if yon4 == "up":
                    if oyunson[satir4-2][sutun4-1]=="X" and oyunson[satir4-3][sutun4-1]=="X" and oyunson[satir4-4][sutun4-1]=="X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol4 = 1
                if yon4 == "down":
                    if oyunson[satir4][sutun4-1]=="X" and oyunson[satir4+1][sutun4-1]=="X" and oyunson[satir4+2][sutun4-1]=="X":
                        print("Tebrikler bir gemi batirdiniz.")
                        kontrol4 = 1

        for i in oyunson:
            print(*i)
        # oyunu kazanma şartı
        if kontrol1 == 1 and kontrol2 == 1 and kontrol3 == 1 and kontrol4 == 1:
            print("Tebrikler tum gemileri batirdiniz. {} puan ile kazandiniz.".format(hak - atis))
            break

    if hak == 0:
        print("Oyunu kaybettiniz. Hakkiniz kalmadi.")
    karar = int(input("Tekrar oynamak icin 1 Cikmak icin 0 giriniz: "))
    if karar == 1:
        continue
    if karar == 0:
        break
print("Cikis yapildi.")
