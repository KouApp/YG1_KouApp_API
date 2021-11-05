

def sifreleme(yazi):
    try:
        alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
        sifre = ""
        for i in yazi:
                sifre = sifre + alfabe[(alfabe.index(i)+3) % len(alfabe)]
        return sifre
    except:
        None

def cozucu():
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
    a =sifreleme("naBeR")
    print(a)
    cozucu = ""
    for a in a:
        cozucu = cozucu + alfabe[(alfabe.index(a)-3) % len(alfabe)]
    print("Yazinin sifresi cozulmus hali : " + cozucu)

cozucu()