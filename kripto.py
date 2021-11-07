import hashlib

def Cryptology(Password):
    Hash=hashlib.md5()
    Hash.update(Password.encode("utf-8"))
    resultHash=Hash.hexdigest()[::-1]
    return resultHash



def kontrol(deg,RegisterDatabasePass):
    b = Cryptology(deg)
    if b == RegisterDatabasePass:
        return True
    else:
        return False


#print(Cryptology("1515"))