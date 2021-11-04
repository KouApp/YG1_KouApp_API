from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen.canvas import Canvas
import io
from reportlab.lib.pagesizes import letter
import base64
import os

def inYatayKayitlimi(TCno):
    dir_list = os.getcwd()
    with os.scandir(dir_list+"/YatayGecisBasvurulari/") as tarama:
        for belge in tarama:
            if belge.name.startswith(str(TCno)):
                return True
            else:
                return False

def inYatayGecisBasvurusu(KurumYG,KurumArasıYG,MerYerPuanYG,YurtDisiYG,
                            AdSoyad,TCno,DogumTarihi,Eposta,GsmTel,EvTel,TebligatAdres,KayitliUniversite,KayitliFakulte,
                            KayitliBolum,birinciOgretim,ikinciOgretim,SınıfYarıyıl,DisiplinCezası,NotOrt,OgrenciNo,
                            KayitliYil,KayitliPuan,YabancıDilPuan,BasvurFakulte,BasvurBolum,BasvurBirinciOgr,BasvurikinciOgr,BasvurPuan,Tarih):
                dir_list = os.getcwd()
                deg = inYatayKayitlimi(TCno)
                if deg :
                    return "Kayitli"
                else:
                    packet = io.BytesIO()
                    can = Canvas(packet, pagesize=letter)
                    can.drawString(280, 720, KurumYG)
                    can.drawString(280, 740, KurumArasıYG)
                    can.drawString(485, 720, MerYerPuanYG)
                    can.drawString(485, 740, YurtDisiYG)
                    can.drawString(150, 670, AdSoyad)
                    can.drawString(150, 652, TCno)
                    can.drawString(367, 652, DogumTarihi)
                    can.drawString(150, 634, Eposta)
                    can.drawString(150, 615, GsmTel)
                    can.drawString(355, 615, EvTel)
                    can.drawString(150, 597, TebligatAdres)
                    can.drawString(330, 550, KayitliUniversite)
                    can.drawString(330, 532, KayitliFakulte)
                    can.drawString(330, 514, KayitliBolum)
                    can.drawString(220, 495, birinciOgretim)
                    can.drawString(327, 495, ikinciOgretim)
                    can.drawString(430, 495, SınıfYarıyıl)
                    can.drawString(330, 472, DisiplinCezası)
                    can.drawString(330, 454, NotOrt)
                    can.drawString(360, 435, OgrenciNo)
                    can.drawString(430, 417, KayitliYil)
                    can.drawString(430, 398, KayitliPuan)
                    can.drawString(120, 365, YabancıDilPuan)
                    can.drawString(230, 322, BasvurFakulte)
                    can.drawString(230, 305, BasvurBolum)
                    can.drawString(220, 288, BasvurBirinciOgr)
                    can.drawString(318, 288, BasvurikinciOgr)
                    can.drawString(120, 255, BasvurPuan)
                    can.drawString(100, 190, Tarih)
                    can.drawString(410, 190, AdSoyad)
                    can.save()
                    packet.seek(0)
                    new_pdf = PdfFileReader(packet)
                    existing_pdf = PdfFileReader(open(dir_list+"/DefaultFile/yatayGecis.pdf", "rb"))
                    output = PdfFileWriter()
                    page = existing_pdf.getPage(0)
                    page.mergePage(new_pdf.getPage(0))
                    output.addPage(page)
                    outputStream = open(dir_list+"/YatayGecisBasvurulari/"+str(TCno)+".pdf", "wb")
                    output.write(outputStream)
                    outputStream.close()
                    with open(dir_list+"/YatayGecisBasvurulari/"+str(TCno)+".pdf", "rb") as fileOpen:
                        decode64 = base64.b64encode(fileOpen.read())
                        dcode = decode64.decode()
                        dict ={"base64":dcode}
                        return dict

def inYazKayitlimi(OgrNo):
    dir_list = os.getcwd()
    with os.scandir(dir_list+"/YazOkuluBasvurulari/") as tarama:
        for belge in tarama:
            if belge.name.startswith(str(OgrNo)):
                return True
            else:
                return False

def inYazOkuluBasvurusu(BolumBaskalik,Fakulte,Bolumu,OgrNo,AdSoyad,YazUnı,YazFakulte,BolumSınıf,GsmTel,email,Adres):
                dir_list = os.getcwd()
                deg = inYazKayitlimi(OgrNo)
                if deg :
                    return "Kayitli"
                else:
                    packet = io.BytesIO()
                    can = Canvas(packet, pagesize=letter)
                    can.drawString(220, 690, BolumBaskalik)
                    can.drawString(190, 640, Fakulte)
                    can.drawString(330, 640, Bolumu)
                    can.drawString(150, 622, OgrNo)
                    can.drawString(330, 622, AdSoyad)
                    can.drawString(195, 567, YazUnı)
                    can.drawString(395, 567, YazFakulte)
                    can.drawString(170, 500, AdSoyad)
                    can.drawString(170, 482, OgrNo)
                    can.drawString(170, 465, BolumSınıf)
                    can.drawString(170, 450, GsmTel)
                    can.drawString(170, 433, email)
                    can.drawString(170, 417, Adres)
                    can.save()
                    packet.seek(0)
                    new_pdf = PdfFileReader(packet)
                    existing_pdf = PdfFileReader(open(dir_list+"/DefaultFile/YazOkuluDilekcesi.pdf", "rb"))
                    output = PdfFileWriter()
                    page = existing_pdf.getPage(0)
                    page.mergePage(new_pdf.getPage(0))
                    output.addPage(page)
                    outputStream = open(dir_list+"/YazOkuluBasvurulari/"+str(OgrNo)+".pdf", "wb")
                    output.write(outputStream)
                    outputStream.close()
                    with open(dir_list+"/YazOkuluBasvurulari/"+str(OgrNo)+".pdf", "rb") as fileOpen:
                        decode64 = base64.b64encode(fileOpen.read())
                        dcode = decode64.decode()
                        dict ={"base64":dcode}
                        return dict

def inMuafiyetKayitlimi(OgrNo):
    dir_list = os.getcwd()
    with os.scandir(dir_list+"/MuafiyetBasvurulari/") as tarama:
        for belge in tarama:
            if belge.name.startswith(str(OgrNo)):
                return True
            else:
                return False

def inMuafiyetBasvurusu(Bolum,Fakulte,yil,AdSoyad,GecisYolu,yarıyıl,OgrNo,intibakYariyil):
                dir_list = os.getcwd()
                deg = inMuafiyetKayitlimi(OgrNo)
                if deg:
                    return "Kayitli"
                else:
                    yyil = int(yil)+1
                    packet = io.BytesIO()
                    can = Canvas(packet, pagesize=letter)
                    can.drawString(200, 750, Bolum)
                    can.drawString(40, 680, "Kocaeli Üniversitesi")
                    can.drawString(210, 680, Fakulte)
                    can.drawString(380, 680, Bolum)
                    can.drawString(180, 662, yil)
                    can.drawString(210, 662, str(yyil))
                    can.drawString(320, 662, GecisYolu)
                    can.drawString(100, 645, Bolum)
                    can.drawString(270, 645, AdSoyad)
                    can.drawString(142, 628, yarıyıl)
                    can.drawString(142, 510, OgrNo)
                    can.drawString(142, 493, AdSoyad)
                    can.drawString(142, 476, GecisYolu)
                    can.drawString(460, 510, intibakYariyil)
                    can.save()
                    packet.seek(0)
                    new_pdf = PdfFileReader(packet)
                    existing_pdf = PdfFileReader(open(dir_list+"/DefaultFile/muafiyet.pdf", "rb"))
                    output = PdfFileWriter()
                    page = existing_pdf.getPage(0)
                    page.mergePage(new_pdf.getPage(0))
                    output.addPage(page)
                    outputStream = open(dir_list+"/MuafiyetBasvurulari/"+str(OgrNo)+".pdf", "wb")
                    output.write(outputStream)
                    outputStream.close()
                    with open(dir_list+"/MuafiyetBasvurulari/"+str(OgrNo)+".pdf", "rb") as fileOpen:
                        decode64 = base64.b64encode(fileOpen.read())
                        dcode = decode64.decode()
                        dict ={"base64":dcode}
                        return dict

def inCapKayitlimi(OgrNo):
    dir_list = os.getcwd()
    with os.scandir(dir_list+"/CapBasvurulari/") as tarama:
        for belge in tarama:
            if belge.name.startswith(str(OgrNo)):
                return True
            else:
                return False

def inCapBasvurusu(BolumBaskalik,Fakulte,Bolumu,program,Ogretim,OgrNo,AdSoyad,Bolumune,Sınıf,GsmTel,email,Adres):
                dir_list = os.getcwd()
                deg = inCapKayitlimi(OgrNo)
                if deg :
                    return "Kayitli"
                else:
                    packet = io.BytesIO()
                    can = Canvas(packet, pagesize=letter)
                    can.drawString(200, 720, BolumBaskalik)
                    can.drawString(50, 665, Fakulte)
                    can.drawString(150, 665, Bolumu)
                    can.drawString(350, 665, program)
                    can.drawString(150, 640, Ogretim)
                    can.drawString(320, 640, OgrNo)
                    can.drawString(180, 588, Bolumune)
                    can.drawString(170, 520, AdSoyad)
                    can.drawString(170, 503, OgrNo)
                    can.drawString(170, 487, Bolumu+ " "+Sınıf)
                    can.drawString(170, 472, GsmTel)
                    can.drawString(170, 455, email)
                    can.drawString(170, 433, Adres)
                    can.save()
                    packet.seek(0)
                    new_pdf = PdfFileReader(packet)
                    existing_pdf = PdfFileReader(open(dir_list+"/DefaultFile/CapBasvurusu.pdf", "rb"))
                    output = PdfFileWriter()
                    page = existing_pdf.getPage(0)
                    page.mergePage(new_pdf.getPage(0))
                    output.addPage(page)
                    outputStream = open(dir_list+"/CapBasvurulari/"+str(OgrNo)+".pdf", "wb")
                    output.write(outputStream)
                    outputStream.close()
                    with open(dir_list+"/CapBasvurulari/"+str(OgrNo)+".pdf", "rb") as fileOpen:
                        decode64 = base64.b64encode(fileOpen.read())
                        dcode = decode64.decode()
                        dict ={"base64":dcode}
                        return dict

