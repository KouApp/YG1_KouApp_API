import database as db
import couchdb 
import CapRecordsDict as dc


couch = couchdb.Server("http://admin:admin@172.104.152.183:5984/")

def CreateDatabases():
    couch.create('users') 
    couch.create('admins') 
    couch.create('doc') 
    couch.create('pdf') 
    couch.create('jpeg') 
    couch.create('xls') 
    couch.create('university') 
    couch.create('faculty') 
    couch.create('section') 
    couch.create('cap')
    return print("Finish")

def CreateUsers():
    db.DBWriteDocument("1","1","yasin","şahin","example@gmail.com","05417895541",
                            "Ev adresim burası","İş Adresim yok","12.10.1995","Kocaeli Üniversitesi",
                            "Teknoloji fakültesi","Bilişim Sistemleri müh","3","12345",dc.yasinBase64)
    db.DBWriteDocument("2","2","abdullah ali","gün","example@gmail.com","05555554444",
                            "Ev adresim burası","İş Adresim yok","12.5.2000","Kocaeli Üniversitesi",
                            "Teknoloji fakültesi","Bilişim Sistemleri müh","3","12345",dc.abdullahBase64)
    db.DBWriteDocument("3","3","sıraç","arapoğlu","example@gmail.com","05555554444",
                            "Ev adresim burası","İş Adresim yok","10.1.1998","Kocaeli Üniversitesi",
                            "Teknoloji fakültesi","Bilişim Sistemleri müh","4","12345",dc.siracBase64)
    return print("Finish")
#CreateUsers()
def CreateFiles():
    db.DBSaveFile("1","Base64Base64Base64","application/pdf","transkript","DGS")
    db.DBSaveFile("2","Base64Base64Base64","application/msword","belge","YG")
    db.DBSaveFile("3","Base64Base64Base64","application/pdf","belge1","DI")
    db.DBSaveFile("4","Base64Base64Base64","application/pdf","belge1","DGS")
    return print("Finish")

#CreateFiles()
def CreateUniSecFac():
    db.inRegistiryUniversity("Kocaeli Universitesi","KOU")
    db.inRegistiryUniversity("Diger","Dig")
    db.inRegistiryUniversityFaculty("Mühendislik Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Bilgisayar Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Elektronik ve Haberleşme Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Mekatronik Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Elektrik Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Endüstri Mühendisliği","Mühendislik Fakültesi","MF")
    #
    db.inRegistiryUniversityFaculty("İletişim Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Gazetecilik","İletişim Fakültesi","IF")
    db.inRegistiryUniversitySection("Halkla İlişkiler ve Tanıtım","İletişim Fakültesi","IF")
    db.inRegistiryUniversitySection("Radyo Televizyon ve Sinema","İletişim Fakültesi","IF")
    db.inRegistiryUniversitySection("Görsel İletişim Tasarımı","İletişim Fakültesi","IF")
    db.inRegistiryUniversitySection("Reklamcılık","İletişim Fakültesi","IF")

    db.inRegistiryUniversityFaculty("Fen-Edebiyat Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Matematik ","Fen-Edebiyat Fakültesi","FEF")
    db.inRegistiryUniversitySection("Fizik ","Fen-Edebiyat Fakültesi","FEF")
    db.inRegistiryUniversitySection("Kimya ","Fen-Edebiyat Fakültesi","FEF")
    db.inRegistiryUniversitySection("Tarih ","Fen-Edebiyat Fakültesi","FEF")
    db.inRegistiryUniversitySection("Arkeoloji","Fen-Edebiyat Fakültesi","FEF")

    db.inRegistiryUniversityFaculty("Eğitim Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Fen bilgisi öğretmenliği","Eğitim Fakültesi","EF")
    db.inRegistiryUniversitySection("İngilizce öğretmenliği","Eğitim Fakültesi","EF")
    db.inRegistiryUniversitySection("Okul öncesi öğretmenliği","Eğitim Fakültesi","EF")
    db.inRegistiryUniversitySection("Rehberlik ve psikolojik danışmanlık","Eğitim Fakültesi","EF")
    db.inRegistiryUniversitySection("Sınıf öğretmenliği","Eğitim Fakültesi","EF")

    db.inRegistiryUniversityFaculty("İktisadi ve İdari Bilimler Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Uluslararası İlişkiler","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("Çalışma Ekonomisi ve Endüstri İlişkileri","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("İktisat","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("İşletme","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("Siyaset Bilimi ve Kamu Yönetimi","İktisadi ve İdari Bilimler Fakültesi","IIF")
#CreateUniSecFac()
def CreateCap():
    database = couch['cap']
    mekatdoc ={"bolum":"Mekatronik Mühendisliği",
                "cap":dc.mekatronikMuh,
                "abbr":"MekMuh"}
    database.save(mekatdoc)

    endustridoc ={"bolum":"Endüstri Mühendisliği",
                "cap":dc.endustriMuh,
                "abbr":"EndustriMuh"}
    database.save(endustridoc)

    elohabdoc ={"bolum":"Elektronik ve Haberleşme Mühendisliği",
                "cap":dc.elohabMuh,
                "abbr":"ElohabMuh"}
    database.save(elohabdoc)

    elekdoc ={"bolum":"Elektrik Mühendisliği",
                "cap":dc.elektrikMuh,
                "abbr":"ElekMuh"}
    database.save(elekdoc)
    bilgdoc ={"bolum":"Bilgisayar Mühendisliği",
                "cap":dc.bilgisayarMuh,
                "abbr":"BilgMuh"}
    database.save(bilgdoc)
    fenndoc ={"bolum":"Fen bilgisi öğretmenliği",
                "cap":dc.fenBilgisiOgretmenligi,
                "abbr":"FenOgr"}
    database.save(fenndoc)
    ingdoc ={"bolum":"İngilizce öğretmenliği",
                "cap":dc.ingilizceOgretmenligi,
                "abbr":"ingOgr"}
    database.save(ingdoc)

    okuloncdoc ={"bolum":"Okul Öncesi öğretmenliği",
                "cap":dc.okuloncesiOgretmenligi,
                "abbr":"OkulOgr"}
    database.save(okuloncdoc)

    rehpsidoc ={"bolum":"Rehberlik ve psikolojik danışmanlık",
                "cap":dc.rehberlikvepsikoOgretmenligi,
                "abbr":"RehPsiOgr"}
    database.save(rehpsidoc)

    sinifdoc ={"bolum":"Sınıf öğretmenliği",
                "cap": dc.sinifOgretmenligi,
                "abbr":"SinifOgr"}
    database.save(sinifdoc)

    arkeolojidoc ={"bolum":"Arkeoloji",
                "cap": dc.arkeoljibol,
                "abbr":"ArkeolojiBol"}
    database.save(arkeolojidoc)

    fizikdoc ={"bolum":"Fizik",
                "cap": dc.fizikbolum,
                "abbr":"FizikBol"}
    database.save(fizikdoc)

    kimyadoc ={"bolum":"Kimya",
                "cap": dc.kimyabolum,
                "abbr":"KimyaBol"}
    database.save(kimyadoc)

    matematikdoc ={"bolum":"Matematik",
                "cap": dc.matematikbolum,
                "abbr":"MatBol"}
    database.save(matematikdoc)

    tarihdoc ={"bolum":"Tarih",
                "cap": dc.tarihbolumu,
                "abbr":"TarihBol"}
    database.save(tarihdoc)

    calekodoc ={"bolum":"Çalışma Ekonomisi ve Endüstri İlişkileri",
                "cap": dc.calismaekonomisi,
                "abbr":"CalEko"}
    database.save(calekodoc)

    iktisatdoc ={"bolum":"İktisat",
                "cap": dc.iktisatbolumu,
                "abbr":"iktisatBol"}
    database.save(iktisatdoc)

    isletmedoc ={"bolum":"İşletme",
                "cap": dc.isletmebolum,
                "abbr":"isletmeBol"}
    database.save(isletmedoc)

    siyasetdoc ={"bolum":"Siyaset Bilimi ve Kamu Yönetimi",
                "cap": dc.siyasetbolumu,
                "abbr":"SiyasetBol"}
    database.save(siyasetdoc)

    uluslardoc ={"bolum":"Uluslararası İlişkiler",
                "cap": dc.uluslararasıılıskıler,
                "abbr":"UluslarArası"}
    database.save(uluslardoc)

    halklardoc ={"bolum":"Halkla İlişkiler ve Tanıtım",
                "cap": dc.halklailiskiler,
                "abbr":"Halkla"}
    database.save(halklardoc)

    radyodoc ={"bolum":"Radyo Televizyon ve Sinema",
                "cap": dc.radyontelevizyon,
                "abbr":"Radyo"}
    database.save(radyodoc)

    gorseldoc ={"bolum":"Görsel İletişim Tasarımı",
                "cap": dc.gorseliletisim,
                "abbr":"Gorsel"}
    database.save(gorseldoc)

    reklamdoc ={"bolum":"Reklamcılık",
                "cap": dc.reklamcilik,
                "abbr":"Reklam"}
    database.save(reklamdoc)

    gazetedoc ={"bolum":"Gazetecilik",
                "cap": dc.gazetecilik,
                "abbr":"Gazete"}
    database.save(gazetedoc)
    
CreateCap()


