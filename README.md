
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
   >image  
   >xls  

***
# Jenkins 

   >Adres : http://172.104.152.183:8080/  
   >Kullanıcı adı : admin  
   >Şifre : 979a43efd3d5498284a7bc8d4f459dc4  
   
# CouchDB APİ
### Registry Page
##### POST  

   >**Adres :** http://172.104.152.183:5000/DatabaseRegistry  
   >**Metod :** POST    
   >**Payload :**  
   >1. {'StudentNo': '181202203',   
   >2. 'TCNo': '555202203',  
   >3. 'Name': 'yasin',  
   >4. 'Surname': 'şahin',  
   >5. 'Email': 'ornek@gmail.com',  
   >6. 'PhoneNo': '555 444 33 22',  
   >7. 'HomeAddress': 'home adres burası',  
   >8. 'BusinessAddress': 'bussines adress',  
   >9. 'DateOfBrith': '18.11.2021',  
   >10. 'UniversityName': 'Kocaeli üniversitesi',  
   >11. 'DepartmanName': 'Teknoloji Fakültesi',  
   >12. 'SectionName': 'Bilişim Sistemleri Müh',  
   >13. 'Rate': '3',  
   >14. 'Password': 'deneme123.'}  

##### Return 
> 1. Başarısız kayıt : False      
> 2. Başarılı kayıt : True    

### Login Page
##### POST
  > **Adres :** http://172.104.152.183:5000/DatabaseLogin    
  > **Metod :** Post    
  > **Payload :**     
  > 1. {'TCNo': '5555',    
  > 2. 'Password': 'deneme123.'}  

##### Return 
>**Admin :** 'admins'  
>**User :** 'users'  
>**Başarısız :** False  

### Faculty Name  
##### Post  
  > **Adres :** http://172.104.152.183:5000/DatabaseGetFacultyName   
  > **Metod :** Post    
  > **Payload :** {'Abbreviation': 'KOU'}   

##### Return  
>{1: 'Mühendislik Fakültesi',   
>2: 'İletişim Fakültesi',   
>3: 'Fen-Edebiyat Fakültesi',  
>4: 'Eğitim Fakültesi',   
>5: 'İktisadi ve İdari Bilimler Fakültesi'}  

### Section Name  
`KISALTMALAR :  
1.İletişim Fakültesi = "IF"    
2.Mühendislik Fakültesi = "MF"  
3.Fen-Edebiyat Fakültesi = "FEF"  
4.İktisadi ve İdari Bilimler Fakültesi = "IIF"  
5.Eğitim Fakültesi = "EF"`
##### Post  
  > **Adres :** http://172.104.152.183:5000/DatabaseGetSectionName   
  > **Metod :** Post    
  > **Payload :** {'Abbreviation': 'IF'}   

##### Return   
>{1: 'Gazetecilik',  
>2: 'Halkla İlişkiler ve Tanıtım',   
>3: 'Radyo Televizyon ve Sinema',   
>4: 'Görsel İletişim Tasarımı',   
>5: 'Reklamcılık'}  

### Reset Password Page  
##### POST   
 >**Adres :** http://172.104.152.183:5000/DatabasePasswordReset  
 >**Metod :** Post  
 >**payload :**
 >1. {'StudentNo': '181202201',  
 >2. 'TCNo': '555202201',   
 >3. 'PhoneNo': '55554488'}  
			   
#####  Return 

  >**Başarılı :** True  
  >**Başarısız :** False  
  >`NOT : Başarılıysa yeni şifre Öğrenci no olur.`  
    

# FİLE
### File upload

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
> `Bir kullanıcı en fazla dört (4) dosya ekleyebilir.`

### File Find  

##### POST  
>**Adres :** http://172.104.152.183:5000/DatabaseGetinfo     
>**Metod :** POST    
>**payload :** {'TCNo': '121215'}    
##### Return  
>**Kayıt yoksa :** False   
>**Kayıt varsa :** Dict = {1:{TCNo,Base64,Control,fileName},2:{TCNo,Base64,...}}    
>**Hata varsa  :** exp   

# APPLİCATİON
### Admin Update  
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
### Get Application  
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
  
   


   >>TOKEN : https://yasinsahin0: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@github.com/KouApp/Couchdb_py_api.git

