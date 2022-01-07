sayi =int(input("İki basamaklı bir sayı giriniz :\n"))


def sayiAtama(sayi):
    if sayi > 9 and sayi<100:
        sayiOkunusu(sayi)
    else:
        print("İki basamaklı sayı girmediniz !")

def sayiOkunusu(sayi):
    birler = sayi % 10
    onlar = sayi // 10
    okunus = ondalikOkunus(onlar) + " " + birlikOkunus(birler)

    print(okunus)

def ondalikOkunus(x):
    match x:
        case 1:
            return "On"
        case 2:
            return "Yirmi"
        case 3:
            return "Otuz"
        case 4:
            return "Kırk"
        case 5:
            return "Elli"
        case 6:
            return "Altmış"
        case 7:
            return "Yetmiş"
        case 8:
            return "Seksen"
        case _:
            return "Doksan"


def birlikOkunus(x):
    match x:
        case 1:
            return "bir"
        case 2:
            return "iki"
        case 3:
            return "üç"
        case 4:
            return "dört"
        case 5:
            return "beş"
        case 6:
            return "altı"
        case 7:
            return "yedi"
        case 8:
            return "sekiz"
        case 9:
            return "dokuz"
        case _:
            return ""

sayiAtama(sayi)
