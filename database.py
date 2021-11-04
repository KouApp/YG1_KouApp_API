import couchdb
import datetime
from couchdb.json import use

couch = couchdb.Server("http://admin:admin@172.104.152.183:5984/")

fileList =["pdf","doc","jpeg","xls"]

userdbName = 'users'
admindbName = 'admins'
UniversitydbName = 'university'
FacultydbName ='faculty'
SectiondbName ='section'

##dbcreatename
dbTCno = "TCNo"
dbStudentNo ="StudentNo"
dbName = "Name"
dbSurName ="Surname"
dbEmail = "Email"
dbPhoneNo ="PhoneNo"
dbHomeAddress = "HomeAddress"
dbBusinessAddress = "BusinessAddress"
dbDateBrith ="DateOfBrith"
dbUniversityName ="UniversityName"
dbDepartmanName ="DepartmanName"
dbSectionName ="SectionName"
dbRate = "Rate"
dbPassword ="Password"
dbControl ="control"
dbPurpose ="Purpose"
dbAbbreviation = "Abbreviation"
dbFaculty='Faculty'
dbuserTCno = "UserTC"
##POST
getType ="fileType"
getBase64 ="Base64"
getFileName ="fileName"

##
cUnSuccess = "ONAYSIZ"
cSuccess ="ONAYLI"
uploadCount=4
MIMHashDict={
    "image/jpeg":"jpg",
    "application/pdf":"pdf",
    "application/msword":"doc",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document":"docx"}

def inLocalUserinfo(TCNo):
    a = 0
    try:
        database = couch["users"]
        for doc in database.find({'selector': {dbTCno: TCNo}}):
            a = 1
            return True
        if a == 0:
            return False
      
    except:
        return "exp"   
#print(findUserR("5"))
def inGetFile(tcNO):
    try:
        a =0
        for typelist in fileList:
            database = couch[typelist]
            for doc in database.find({'selector': {dbTCno: tcNO}}):
                a += 1
        return a      
    except:
        return  "exp"
#print(inGetFile("1"))
def inRegistiryUniversity(UniName,Abbrev):
    database = couch[UniversitydbName]
    doc ={dbUniversityName:UniName,
            dbAbbreviation:Abbrev}
    database.save(doc)
    return True
#print(inRegistiryUniversity("Kocaeli Universitesi","KOU"))
def inRegistiryUniversityFaculty(Faculty,abbr,UnivName):
    database = couch[FacultydbName]
    doc ={dbFaculty:Faculty,dbAbbreviation:abbr,dbUniversityName:UnivName}
    database.save(doc)
    return True
#print(inRegistiryUniversityFaculty("İktisadi ve İdari Bilimler Fakültesi","KOU","Kocaeli Universitesi"))
def inRegistiryUniversitySection(Section,Faculty,abbr):
    database = couch[SectiondbName]
    doc ={dbFaculty:Faculty,
            dbSectionName:Section,
            dbAbbreviation:abbr}
    database.save(doc)
    return True
#print(inRegistiryUniversitySection("Uluslararası İlişkiler","İktisadi ve İdari Bilimler Fakültesi","IIF"))



def DBWriteDocument(studentNo,tcNo,name,surname,email,phoneNo,
                    homeAddress,businessAddress,dateofbrith,universityName,
                    facultyName,sectionName,classNumber,password):
    findUser = inLocalUserinfo(tcNo)
    if findUser == True:
        return "False"
    else:
        date = datetime.datetime.now()
        database = couch["users"]
        doc ={  'date' :str(date),
                dbStudentNo:studentNo,
                dbTCno:tcNo,
                dbName:name,
                dbSurName:surname,
                dbEmail:email,
                dbPhoneNo:phoneNo,
                dbHomeAddress:homeAddress,
                dbBusinessAddress:businessAddress,
                dbDateBrith:dateofbrith,
                dbUniversityName:universityName,
                dbDepartmanName:facultyName,
                dbSectionName:sectionName,
                dbRate:classNumber,
                dbPassword:password}
        database.save(doc)
        return "True"
#print(DBWriteDocument("1","1","adwad","aw3da","awda","awda","aga","faf","awdw","awaaa","agag","adadaw","23","aaaa"))
def DBPasswordReset(TCNo,phoneNo,studentNo):
    a = 0
    database = couch['users']
    for doc in database.find({'selector': {dbTCno: TCNo,
                                            dbPhoneNo:phoneNo,
                                            dbStudentNo:studentNo}}):
        a=1
        doc[dbPassword] = studentNo
        database.save(doc)
        return "True"
    if a==0:
        return "False"
#rint(resetPassword("5","awda","4"))
def DBLogininfo(TCNo,passwd):
    a = 0
    try:
        database = couch[userdbName]
        for doc in database.find({'selector': {dbTCno: TCNo, dbPassword: passwd}}):
            a =1
            return userdbName
        database1 = couch[admindbName]
        for doc1 in database1.find({'selector': {dbTCno: TCNo, dbPassword: passwd}}):
            a=1
            return admindbName
        if a ==0:
            return "False"
    except:
        return "exp"
#print(usersLogin("1515","1515"))
def DBRegistryAdmin(TCNo,password):
    date = datetime.datetime.now()
    database = couch["admins"]
    doc ={  'date' :str(date),
            dbTCno:TCNo,
            dbPassword:password}
    database.save(doc)
    return "True"
#print(DBRegistryAdmin("1515","1515"))
def DBSaveFile(tcNO,Base64,typeinfo,fileName,purpose):
    res = MIMHashDict[typeinfo]
    date = datetime.datetime.now()
    fileCount= inGetFile(tcNO)
    if uploadCount >fileCount:
        database = couch[res]
        doc ={  'date' :str(date),
                    getFileName:fileName,
                    getType : res,
                    dbTCno:tcNO,
                    getBase64:Base64,
                    dbControl:cUnSuccess,
                    dbPurpose:purpose}
        database.save(doc)
        return "True"
    elif inGetFile== "exp":
        return "exp"
    else:
        return "CountLimited"
#print(DBSaveFile("2","base64","application/pdf","trans","YG"))
def DBFileinfo(tcNO):
    try:
        getinfoDict={}
        count = 0
        for i in fileList:
            database = couch[i]
            for doc in database.find({'selector': {dbTCno: tcNO}}):    
                count +=1
                Gbase64 =doc[getBase64]
                Gcontrol =doc[dbControl]
                fileName = doc[getFileName]
                postdict = {
                         dbTCno :tcNO,
                         getBase64: Gbase64,
                         dbControl: Gcontrol,
                         getFileName: fileName}
                getinfoDict.update({count:postdict})
        return getinfoDict
    except:
        return "exp"
#print(DBFileinfo("10"))
def DBFindApplication(adminTC,adminPass,abbr,userTC):
    try:
        logresult = DBLogininfo(adminTC,adminPass)
        dgsDict={}
        if userTC == "":
            if logresult == "admins":
                count = 0
                for i in fileList:
                    database = couch[i]
                    for doc in database.find({'selector': {dbPurpose: abbr}}):
                        count +=1
                        doct = {}
                        Gbase64 =doc[getBase64]
                        Gcontrol =doc[dbControl]
                        fileName = doc[getFileName]
                        tcNo = doc[dbTCno]
                        doct.update({"TC no":tcNo})
                        doct.update({"Base64":Gbase64})
                        doct.update({"Kontrol":Gcontrol})
                        doct.update({"Dosya ismi":fileName})
                        dgsDict.update({count:doct})
                return dgsDict
        elif len(userTC) > 1:
            count = 0
            for i in fileList:
                database = couch[i]
                for doc in database.find({'selector': {dbTCno: userTC}}):
                    count +=1
                    doct = {}
                    Gbase64 =doc[getBase64]
                    Gcontrol =doc[dbControl]
                    fileName = doc[getFileName]
                    purpos = doc[dbPurpose]
                    doct.update({"Purpose":purpos})
                    doct.update({"Base64":Gbase64})
                    doct.update({"Kontrol":Gcontrol})
                    doct.update({"Dosya ismi":fileName})
                    dgsDict.update({count:doct})
            return dgsDict
        else:
            return "False"
    except:
        return "exp"
#print(DBFindApplication("1515","1515","YG",""))
def DBAdminUpdateApp(TCNo,purpose,cntrol):
    for i in fileList:
        database = couch[i]
        for doc in database.find({'selector': {dbTCno: TCNo,dbPurpose:purpose}}):
            doc[dbControl] = cntrol
            database.save(doc)
            return "True"
    return "False"
#print(DBAdminUpdateApp("15","dgs"))
def DBgetUserFile(TCNo,purpose):#Onaylımı onaysız mı
    for i in fileList:
        database = couch[i]
        for doc in database.find({'selector': {dbTCno: TCNo,dbPurpose:purpose}}):
            rescontrol = doc[dbControl]
            return rescontrol
    return False
#print(DBgetUserFile("10","dgs"))
def DBgetUniversityfaculty(abbr):
    database = couch[FacultydbName]
    mydict={}
    listem = []
    a=0
    for doc in database.find({'selector': {dbAbbreviation: abbr}}):
        a+=1
        mydict.update({a:doc[dbFaculty]})
    return mydict
#print(DBgetUniversityfaculty("KOU"))
def DBgetUniversitySection(facName):
    database = couch[SectiondbName]
    mydict={}
    a=0
    for doc in database.find({'selector': {dbAbbreviation: facName}}):
        a+=1
        mydict.update({a:doc[dbSectionName]})
    return mydict      
#print(DBgetUniversitySection("IF"))
def DBgetCap(abbr):
    capdict ={}
    database = couch['cap']
    for doc in database.find({'selector': {"abbr": abbr}}):
        capdict =doc["cap"]
    return capdict

        