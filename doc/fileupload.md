# File Upload Page 
 
>**Adres :** http://172.104.152.183:5000/DatabaseSaveFile     
>**Metod :** POST   
>**payload :**  
>1. {'TCNo': '18181',    
>2. 'fileType': 'pdf',    
>3. 'Base64': 'basdadad3',  
>4. 'fileName' : 'transkript',  
>5. 'Purpose': 'DGS'}   
  
### Purpose   
>> 1. Yaz okulu : "YO"  
>> 2. Çap Başvurusu : "CAP"  
>> 3. Dikey geçiş Başvurusu : "DGS"   
>> 4. Yatay geçiş Başvurusu : "YG"   
>> 5. İntibak Başvurusu : "DI"  
# Return

> **Kayıt Başarılı :** True  
> **Kayıt Başarısız :** CountLimited  
> **Hata varsa :** exp  
`Bir kullanıcı en fazla dört (4) dosya ekleyebilir.`