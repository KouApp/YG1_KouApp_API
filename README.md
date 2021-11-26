
***
# CouchDB Database 

  >http://172.104.152.183:5984/_utils  
  >Kullanıcı adı : admin  
  >Sifre : admin  
  
### Database Names :  
  
   >users  
   >admins  
   >doc  
   >pdf  
   >jpeg    
   >xls  
   >faculty  
   >section  
   >university  
   >cap
   >university  
   >faculty  
   >section  


***
# Jenkins 

   >Adres : http://172.104.152.183:8080/  
   >Kullanıcı adı : admin  
   >Şifre : 979a43efd3d5498284a7bc8d4f459dc4  
   
# CouchDB APİ

User Registry : [Documentation](https://github.com/KouApp/KouAppAPI/blob/main/doc/userregistry.md)  
Login : [Documentation](https://github.com/KouApp/KouAppAPI/blob/main/doc/login.md)
User Profile : [Documentation](https://github.com/KouApp/KouAppAPI/blob/main/doc/userprofile.md)
Faculty Name Get Page : [Documentation](https://github.com/KouApp/KouAppAPI/blob/main/doc/facnamegetpage.md)
Section Name Get Page : [Documentation](https://github.com/KouApp/KouAppAPI/blob/main/doc/sectionnameget.md)
Reset Password : [Documentation](https://github.com/KouApp/KouAppAPI/blob/main/doc/resetpass.md)




## File Upload Page 

##### POST   
>**Adres :** http://172.104.152.183:5000/DatabaseSaveFile     
>**Metod :** POST   
>**payload :**  
>1. {'TCNo': '18181',    
>2. 'fileType': 'pdf',    
>3. 'Base64': 'basdadad3',  
>4. 'fileName' : 'transkript',  
>5. 'Purpose': 'DGS'}   
  
**Purpose :**  
>> 1. Yaz okulu : "YO"  
>> 2. Çap Başvurusu : "CAP"  
>> 3. Dikey geçiş Başvurusu : "DGS"   
>> 4. Yatay geçiş Başvurusu : "YG"   
>> 5. İntibak Başvurusu : "DI"  
##### Return

> **Kayıt Başarılı :** True  
> **Kayıt Başarısız :** CountLimited  
> **Hata varsa :** exp  
`Bir kullanıcı en fazla dört (4) dosya ekleyebilir.`

## File Find Page

##### POST  
>**Adres :** http://172.104.152.183:5000/DatabaseGetinfo     
>**Metod :** POST    
>**payload :** {'TCNo': '121215'}    
##### Return  
>**Kayıt yoksa :** False   
>**Kayıt varsa :** Dict = {1:{TCNo,Base64,Control,fileName},2:{TCNo,Base64,...}}    
>**Hata varsa  :** exp   

# Admin
## Admin Update Page
##### Post   
>**Adres :** http://172.104.152.183:5000/DatabaseAdminUpdatefile    
>**Metod :** POST  
>**Payload :**  
>{'TCNo': '121215',  
>'Purpose': 'ygb',  
>'control' :'ONAYLI'}  
##### Return  
>**Başarılı :** True   
>**Başarısız :** False   
> `True Dönerse kayıt onaylanmış olur`  
## Get Application Page
##### Post   
>**Adres :** http://172.104.152.183:5000/DatabaseGetApplication   
>**Metod :** POST    
>**payload :**  
>{'TCNo': '1515',  
> 'Password': '1515',  
> 'Abbreviation':'DGS',  
> 'UserTC' : '10'}  
> ` NOT : Sadece admin tcno ve pass dönüş verir! UserTC gönderilmezse bütün kayıtları getirir.`    
>> 1. Yaz okulu : "YO"  
>> 2. Çap Başvurusu : "CAP"  
>> 3. Dikey geçiş Başvurusu : "DGS"   
>> 4. Yatay geçiş Başvurusu : "YG"    
>> 5. İntibak Başvurusu : "DI"    
##### Return    
>**Kayıt yoksa :** False   
>**Kayıt varsa :** Dict = {"1":[liste] ,"2":[liste],...}  
>**Hata varsa  :** exp   

# Başvurular

## Yatay Geçiş Başvurusu Sayfası

#### Post
>**Adres :** http://172.104.152.183:5000/YatayGecisBasvurusu   
>**Metod :** POST     
>**payload :**   
>>payload={'KurumYG': 'X',  
>>'KurumArasıYG': 'O',  
>>'MerYerPuanYG': 'O',  
>>'YurtDisiYG': 'O',  
>>'AdSoyad': 'Yasin Sahin',  
>>'TCno': '55588822213',  
>>'DogumTarihi': '14.09.1990',  
>>'Eposta': 'example@gmail.com',  
>>'GsmTel': '0 555 222 21 21',  
>>'EvTel': '0 216 222 33 33',  
>>'TebligatAdres': 'Exammple Adress ',  
>>'KayitliUniversite': 'Kocaeli Universitesi',  
>>'KayitliFakulte': 'Teknoloji Fakultesi',  
>>'KayitliBolum': 'Bilisim Sistemleri muh',  
>>'birinciOgretim': 'X',  
>>'ikinciOgretim': 'O',  
>>'SınıfYarıyıl': '3-6',  
>>'DisiplinCezası': 'Yok',  
>>'NotOrt': '4.11',  
>>'OgrenciNo': '188188188',  
>>'KayitliYil': '2020',  
>>'KayitliPuan': '355',  
>>'YabancıDilPuan': 'Yok',  
>>'BasvurFakulte': 'Muhendiislik',  
>>'BasvurBolum': 'Bilgisayar muh',  
>>'BasvurBirinciOgr': 'X',  
>>'BasvurikinciOgr': 'O',  
>>'BasvurPuan': '380',  
>>'Tarih': '15.12.2021'}  
##### Return  
>>{"base64":"base64base64base64base64base64"}  



## Çap Başvurusu

##### Post
>**Adres :** http://172.104.152.183:5000/CapBasvurusu  
>**Metod :** POST     
>**payload :**   
>>{'BolumBaskanlik': 'Baskanlik',  
>>'Fakulte': 'Fakulte',  
>>'Bolumu': 'Bolumu',  
>>'Program': 'Program',  
>>'Ogretim': 'I Ogretim',  
>>'OgrNo': '18111115',  
>>'AdSoyad': 'Yasin Sahin',  
>>'Bolumune': 'Bilisim Sistemleri',  
>>'Sinif': '3',  
>>'GsmTel': '544554447',  
>>'Email': 'example@gmail.com',  
>>'Adres': 'Adres Adres'}  

###### Return  
>**Kayıt Varsa :** Kayitli  
>**Kayıt Yoksa :** Base64  

## Muafiyet Başvurusu Sayfası

##### Post
>**Adres :** http://172.104.152.183:5000/MuafiyetBasvurusu  
>**Metod :** POST     
>**payload :**   
>>{'Bolum': 'Bolumu',  
>>'Fakulte': 'Fakultesi',  
>>'Yil': '21',  
>>'AdSoyad': 'Yasin Sahin',  
>>'GecisYolu': 'Yatay Gecis',  
>>'Yariyil': '5',  
>>'OgrNo': '18118111',  
>>'intibakYariyil': '6'}  

##### Return  
>**Kayıt Varsa :** Kayitli  
>**Kayıt Yoksa :** Base64


## Yaz Okulu Başvurusu Sayfası
##### Post
>**Adres :** http://172.104.152.183:5000/YazOkuluBasvurusu  
>**Metod :** POST     
>**payload :**   
>>{'Baskanlik': 'Baskanlık',  
>>'Fakulte': 'Fakulte',  
>>'Bolum': 'Bolum',  
>>'OgrNo': '18118181',  
>>'AdSoyad': 'Yasin Sahin',  
>>'YazUni': 'Yaz Universite',  
>>'YazFakulte': 'Yaz Fakulte',  
>>'BolumSinif': 'BolumSınıf',  
>>'GsmTel': '545454545',  
>>'Email': 'example@ggmailc.om',  
>>'TebligatAdres': 'adres adress'}   

##### Return  
>**Kayıt Varsa :** Kayitli  
>**Kayıt Yoksa :** Base64  

## Çap Başvurusu Bölümleri

##### Post
>**Adres :** http://172.104.152.183:5000/DatabaseGetCap   
>**Metod :** POST     
>**payload :**   
>>payload={'SectionName': 'Bilgisayar Mühendisliği'}  

##### Return  
>>    {"a": "Elektronik ve Haberleşme Mühendisliği",  
>>    "b": "Bilgisayar Mühendisliği",  
>>    "c": "Mekatronik Mühendisliği"}  

##### Abbreviation  
> Bilgisayar Mühendisliği : BilgMuh  
> Elektrik Mühendisliği : ElekMuh  
> Elektronik ve Haberleşme Mühendisliği : ElohabMuh  
> Endüstri Mühendisliği : EndMuh  
> Mekatronik Mühendisliği : MekMuh  
  
> Fen bilgisi Öğretmenliği : FenOgr  
> İngilizce Öğretmenliği : ingOgr  
> Okul Öncesi Öğretmenliği : OkulOgr  
> Rehberlik ve Psikolojisi Öğretmenliği : RehPsiOgr  
> Sınıf Öğretmenliği : SinifOgr  
  
> Arkeoloji Bölümü : ArkeolojiBol  
> Fizik Bölümü : FizikBol  
> Kimya Bölümü : KimyaBol  
> Matematik Bölümü : MatBol  
> Tarih Bölümü : TarihBol  
  
> Calısma Ekonomisi : CalEko  
> İktisat Bölümü : iktisatBol  
> İşletme Bölümü : isletmeBol  
> Siyaset Bölümü : SiyasetBol  
> Uluslar arası İlişkiler : UluslarArası  
  
> Halkla İlişkiler : Halkla   
> Radyo Televizyon : Radyo  
> Görsel İletişim : Gorsel  
> Reklamcılık : Reklam  
> Gazetecilik : Gazete  
## Git repo
>>TOKEN : https://yasinsahin0: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@github.com/KouApp/Couchdb_py_api.git  
>> Kou Mobil App : git clone https://yasinsahin0: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@github.com/yasinsahin0/kou-mobil-app.git  
>> Kou Mobil App Organizasyon: git clone https://yasinsahin0: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@github.com/KouApp/KouMobilApp-Java-Android.git