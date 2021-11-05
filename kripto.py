import hashlib
sifre="4cef278fa51df71b9ddb8c82178a77d2"
sifrele=hashlib.md5()
sifrele.update(sifre.encode("utf-8"))
cikti=sifrele.hexdigest()
print(cikti.digest())
print(cikti)