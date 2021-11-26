# Get Application Page   
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
# Return    
>**Kayıt yoksa :** False   
>**Kayıt varsa :** Dict = {"1":[liste] ,"2":[liste],...}  
>**Hata varsa  :** exp   