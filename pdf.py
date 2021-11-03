from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen.canvas import Canvas
import io
from reportlab.lib.pagesizes import letter
import base64
import os

def inKayitlimi(TCno):
    with os.scandir("YatayGecisBasvurulari/") as tarama:
        for belge in tarama:
            if belge.name.startswith(str(TCno)):
                return True
            else:
                return False

def inYatayGecisBasvurusu(KurumYG,KurumArasıYG,MerYerPuanYG,YurtDisiYG,
                            AdSoyad,TCno,DogumTarihi,Eposta,GsmTel,EvTel,TebligatAdres,KayitliUniversite,KayitliFakulte,
                            KayitliBolum,birinciOgretim,ikinciOgretim,SınıfYarıyıl,DisiplinCezası,NotOrt,OgrenciNo,
                            KayitliYil,KayitliPuan,YabancıDilPuan,BasvurFakulte,BasvurBolum,BasvurBirinciOgr,BasvurikinciOgr,BasvurPuan,Tarih):
                deg = inKayitlimi(TCno)
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
                    existing_pdf = PdfFileReader(open("DefaultFile/yatayGecis.pdf", "rb"))
                    output = PdfFileWriter()
                    page = existing_pdf.getPage(0)
                    page.mergePage(new_pdf.getPage(0))
                    output.addPage(page)
                    outputStream = open("YatayGecisBasvurulari/"+str(TCno)+".pdf", "wb")
                    output.write(outputStream)
                    outputStream.close()
                    with open("YatayGecisBasvurulari/"+str(TCno)+".pdf", "rb") as fileOpen:
                        decode64 = base64.b64encode(fileOpen.read())
                        dcode = decode64.decode()
                        dict ={"base64":dcode}
                        return dict
    

