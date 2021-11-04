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
    db.DBWriteDocument("1","1","yasin","şahin","example@gmail.com","05555554444",
                            "Ev adresim burası","İş Adresim yok","25","Kocaeli Üniversitesi",
                            "Teknoloji fakültesi","Bilişim Sistemleri müh","3","12345")
    db.DBWriteDocument("2","2","ahmet","öz","example@gmail.com","05555554444",
                            "Ev adresim burası","İş Adresim yok","12.5.1555","Kocaeli Üniversitesi",
                            "Teknoloji fakültesi","Bilişim Sistemleri müh","4","12345")
    db.DBWriteDocument("3","3","ahmet","öz","example@gmail.com","05555554444",
                            "Ev adresim burası","İş Adresim yok","25","Kocaeli Üniversitesi",
                            "Teknoloji fakültesi","Bilişim Sistemleri müh","4","12345")
    db.DBWriteDocument("4","4","ahmet","öz","example@gmail.com","05555554444",
                            "Ev adresim burası","İş Adresim yok","25","Kocaeli Üniversitesi",
                            "Teknoloji fakültesi","Bilişim Sistemleri müh","4","12345")
    return print("Finish")

def CreateFiles():
    db.DBSaveFile("1","Base64Base64Base64","application/pdf","transkript","DGS")
    db.DBSaveFile("2","Base64Base64Base64","application/msword","belge","YG")
    db.DBSaveFile("3","Base64Base64Base64","application/pdf","belge1","DI")
    db.DBSaveFile("4","Base64Base64Base64","application/pdf","belge1","DGS")
    return print("Finish")

def CreateUniSecFac():
    db.inRegistiryUniversity("Kocaeli Universitesi","KOU")
    db.inRegistiryUniversityFaculty("Mühendislik Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Bilgisayar Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Elektronik ve Haberleşme Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Mekatronik Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Elektrik Mühendisliği","Mühendislik Fakültesi","MF")
    db.inRegistiryUniversitySection("Endüstri Mühendisliği","Mühendislik Fakültesi","MF")
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
    db.inRegistiryUniversitySection("Arkeoloj ","Fen-Edebiyat Fakültesi","FEF")
    db.inRegistiryUniversityFaculty("Eğitim Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Fen bilgisi öğretmenliği","Fen-Edebiyat Fakültesi","EF")
    db.inRegistiryUniversitySection("İngilizce öğretmenliği","Fen-Edebiyat Fakültesi","EF")
    db.inRegistiryUniversitySection("Okul öncesi öğretmenliği","Fen-Edebiyat Fakültesi","EF")
    db.inRegistiryUniversitySection("Rehberlik ve psikolojik danışmanlık","Fen-Edebiyat Fakültesi","EF")
    db.inRegistiryUniversitySection("Sınıf öğretmenliği","Fen-Edebiyat Fakültesi","EF")
    db.inRegistiryUniversityFaculty("İktisadi ve İdari Bilimler Fakültesi","KOU","Kocaeli Universitesi")
    db.inRegistiryUniversitySection("Uluslararası İlişkiler","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("Çalışma Ekonomisi ve Endüstri İlişkileri","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("İktisat","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("İşletme","İktisadi ve İdari Bilimler Fakültesi","IIF")
    db.inRegistiryUniversitySection("Siyaset Bilimi ve Kamu Yönetimi","İktisadi ve İdari Bilimler Fakültesi","IIF")

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
    fenndoc ={"bolum":"Fen bilgisi Öğretmenliği",
                "cap":dc.fenBilgisiOgretmenligi,
                "abbr":"FenOgr"}
    database.save(fenndoc)
    ingdoc ={"bolum":"İngilizce Öğretmenliği",
                "cap":dc.ingilizceOgretmenligi,
                "abbr":"ingOgr"}
    database.save(ingdoc)

    okuloncdoc ={"bolum":"Okul Öncesi Öğretmenliği",
                "cap":dc.okuloncesiOgretmenligi,
                "abbr":"OkulOgr"}
    database.save(okuloncdoc)

    rehpsidoc ={"bolum":"Rehberlik ve Psikolojisi Öğretmenliği",
                "cap":dc.rehberlikvepsikoOgretmenligi,
                "abbr":"RehPsiOgr"}
    database.save(rehpsidoc)

    sinifdoc ={"bolum":"Sınıf Öğretmenliği",
                "cap": dc.sinifOgretmenligi,
                "abbr":"SinifOgr"}
    database.save(sinifdoc)

    arkeolojidoc ={"bolum":"Arkeoloji Bölümü",
                "cap": dc.arkeoljibol,
                "abbr":"ArkeolojiBol"}
    database.save(arkeolojidoc)

    fizikdoc ={"bolum":"Fizik Bölümü",
                "cap": dc.fizikbolum,
                "abbr":"FizikBol"}
    database.save(fizikdoc)

    kimyadoc ={"bolum":"Kimya Bölümü",
                "cap": dc.kimyabolum,
                "abbr":"KimyaBol"}
    database.save(kimyadoc)

    matematikdoc ={"bolum":"Matematik Bölümü",
                "cap": dc.matematikbolum,
                "abbr":"MatBol"}
    database.save(matematikdoc)

    tarihdoc ={"bolum":"Tarih Bölümü",
                "cap": dc.tarihbolumu,
                "abbr":"TarihBol"}
    database.save(tarihdoc)

    calekodoc ={"bolum":"Calısma Ekonomisi",
                "cap": dc.calismaekonomisi,
                "abbr":"CalEko"}
    database.save(calekodoc)

    iktisatdoc ={"bolum":"İktisat Bölümü",
                "cap": dc.iktisatbolumu,
                "abbr":"iktisatBol"}
    database.save(iktisatdoc)

    isletmedoc ={"bolum":"İşletme Bölümü",
                "cap": dc.isletmebolum,
                "abbr":"isletmeBol"}
    database.save(isletmedoc)

    siyasetdoc ={"bolum":"Siyaset Bölümü",
                "cap": dc.siyasetbolumu,
                "abbr":"SiyasetBol"}
    database.save(siyasetdoc)

    uluslardoc ={"bolum":"Uluslar arası ilişkiler",
                "cap": dc.uluslararasıılıskıler,
                "abbr":"UluslarArası"}
    database.save(uluslardoc)

    halklardoc ={"bolum":"Halkla ilişkiler",
                "cap": dc.halklailiskiler,
                "abbr":"Halkla"}
    database.save(halklardoc)

    radyodoc ={"bolum":"Radyo Televizyon",
                "cap": dc.radyontelevizyon,
                "abbr":"Radyo"}
    database.save(radyodoc)

    gorseldoc ={"bolum":"Görsel İletisim",
                "cap": dc.gorseliletisim,
                "abbr":"Gorsel"}
    database.save(gorseldoc)

    reklamdoc ={"bolum":"Reklamcilik",
                "cap": dc.reklamcilik,
                "abbr":"Reklam"}
    database.save(reklamdoc)

    gazetedoc ={"bolum":"Gazetecilik",
                "cap": dc.gazetecilik,
                "abbr":"Gazete"}
    database.save(gazetedoc)
    



