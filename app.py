from flask import Flask,jsonify,request
import database as db
import pdf
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = 'development'


@app.route('/test',methods=['POST'])
def test():
	print('[INFO]--[test]--[FUNCTION]')
	name = request.form['name']
	return jsonify({'names':name})

@app.route('/DatabaseRegistry', methods=['POST'])
def DatabaseRegistry():
    studentNo = request.form[db.dbStudentNo]
    tcNo = request.form[db.dbTCno]
    name = request.form[db.dbName]
    surname = request.form[db.dbSurName]
    email = request.form[db.dbEmail]
    phoneNo = request.form[db.dbPhoneNo]
    homeAddress = request.form[db.dbHomeAddress]
    businessAddress = request.form[db.dbBusinessAddress]
    dateofbrith = request.form[db.dbDateBrith]
    universityName = request.form[db.dbUniversityName]
    facultyName = request.form[db.dbDepartmanName]
    sectionName = request.form[db.dbSectionName]
    classNumber = request.form[db.dbRate]
    password = request.form[db.dbPassword]
    result = db.DBWriteDocument(studentNo,
                                    tcNo,name,surname,
                                    email,phoneNo,homeAddress,
                                    businessAddress,dateofbrith,
                                    universityName,facultyName,
                                    sectionName,classNumber,password)

    return result

@app.route('/DatabaseLogin', methods=['POST'])
def DatabaseLogin():
    TCNo = request.form[db.dbTCno]
    password = request.form[db.dbPassword]
    result = db.DBLogininfo(TCNo,password)
    return result

@app.route('/DatabasePasswordReset', methods=['POST'])
def DatabasePasswordReset():
    studentNo = request.form[db.dbStudentNo]
    tcNo = request.form[db.dbTCno]
    phoneNo = request.form[db.dbPhoneNo]
    result = db.DBPasswordReset(tcNo,phoneNo,studentNo)
    return result

@app.route('/DatabaseSaveFile', methods=['POST'])
def DatabaseSaveFile():
    TCNo = request.form[db.dbTCno]
    getType = request.form[db.getType]
    getBase64 = request.form[db.getBase64]
    getFileName = request.form[db.getFileName]
    getPurpose = request.form[db.dbPurpose]
    result = db.DBSaveFile(TCNo,getBase64,getType,getFileName,getPurpose)
    return result

@app.route('/DatabaseGetinfo', methods=['POST'])
def DatabaseGetinfo():
    tcNo = request.form[db.dbTCno]
    result = db.DBFileinfo(tcNo)
    return result

@app.route('/DatabaseGetApplication', methods=['POST'])
def DatabaseGetApplication():
    tcNo = request.form[db.dbTCno]
    passwd = request.form[db.dbPassword]
    abbr = request.form[db.dbAbbreviation]
    usertc = request.form[db.dbuserTCno]
    DGSdict = db.DBFindApplication(tcNo,passwd,abbr,usertc)
    return DGSdict

@app.route('/DatabaseAdminUpdatefile', methods=['POST'])
def DatabaseAdminUpdatefile():
    TCNo = request.form[db.dbTCno]
    purpose = request.form[db.dbPurpose]
    control = request.form[db.dbControl]
    result = db.DBAdminUpdateApp(TCNo,purpose,control)
    return result

@app.route('/DatabaseGetFacultyName', methods=['POST'])
def DatabaseGetFacultyName():
    abbr = request.form[db.dbAbbreviation]
    result = db.DBgetUniversityfaculty(abbr)
    return result

@app.route('/DatabaseGetSectionName', methods=['POST'])
def DatabaseGetSectionName():
    abbr = request.form[db.dbAbbreviation]
    result = db.DBgetUniversitySection(abbr)
    return result

@app.route('/YatayGecisBasvurusu', methods=['POST'])
def YatayGecisBasvurusu():
    KurumYG=request.form["KurumYG"]
    KurumArasıYG=request.form["KurumArasıYG"]
    MerYerPuanYG=request.form["MerYerPuanYG"]
    YurtDisiYG=request.form["YurtDisiYG"]
    AdSoyad = request.form["AdSoyad"]
    TCno = request.form["TCno"]
    DogumTarihi = request.form["DogumTarihi"]
    Eposta = request.form["Eposta"]
    GsmTel = request.form["GsmTel"]
    EvTel = request.form["EvTel"]
    TebligatAdres = request.form["TebligatAdres"]
    KayitliUniversite = request.form["KayitliUniversite"]
    KayitliFakulte =request.form["KayitliFakulte"]
    KayitliBolum = request.form["KayitliBolum"]
    birinciOgretim =request.form["birinciOgretim"]
    ikinciOgretim =request.form["ikinciOgretim"]
    SınıfYarıyıl =request.form["SınıfYarıyıl"]
    DisiplinCezası = request.form["DisiplinCezası"]
    NotOrt =request.form["NotOrt"]
    OgrenciNo =request.form["OgrenciNo"]
    KayitliYil =request.form["KayitliYil"]
    KayitliPuan =request.form["KayitliPuan"]
    YabancıDilPuan =request.form["YabancıDilPuan"]
    BasvurFakulte =request.form["BasvurFakulte"]
    BasvurBolum =request.form["BasvurBolum"]
    BasvurBirinciOgr = request.form["BasvurBirinciOgr"]
    BasvurikinciOgr =request.form["BasvurikinciOgr"]
    BasvurPuan =request.form["BasvurPuan"]
    Tarih =request.form["Tarih"]
    result = pdf.inYatayGecisBasvurusu(KurumYG,KurumArasıYG,MerYerPuanYG,YurtDisiYG,
                            AdSoyad,TCno,DogumTarihi,Eposta,GsmTel,EvTel,TebligatAdres,KayitliUniversite,KayitliFakulte,
                            KayitliBolum,birinciOgretim,ikinciOgretim,SınıfYarıyıl,DisiplinCezası,NotOrt,OgrenciNo,
                            KayitliYil,KayitliPuan,YabancıDilPuan,BasvurFakulte,BasvurBolum,BasvurBirinciOgr,BasvurikinciOgr,BasvurPuan,Tarih)
    return result

if __name__ == '__main__':
    app.run()
