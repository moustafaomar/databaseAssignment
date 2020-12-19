import mysql.connector
def output():
    print('''
            1.Add new doctor
            2.Add new patient
            3.Relate patient and doctor
            4.View list of doctors names
            5.View list of patients names
            6.View list of patient and corresponding doctor
            7.Terminate a patient doctor relationship
            8.View patients names supervised by selected doctor
            9.View doctors names supervises a selected patient
    ''')
def SQL_CONN():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="databaseSubmissions"
    )
    conn = mydb.cursor()
    return [conn,mydb]
def AddDoctor():
    DName = input("Please Enter Doctor Name:")
    DDep = input("Please Enter Doctor Department:")
    DID = input("Please Enter Doctor ID:")
    Query = "INSERT INTO Doctors (name,department,id) VALUES (%s,%s,%s)"
    Values = (DName,DDep,DID)
    conn.execute(Query,Values)
def AddPatient():
    PName = input("Please Enter Patient Name:")
    PID = input("Please Enter Patient ID:")
    Query = "INSERT INTO patients(name,id) VALUES (%s,%s)"
    Values = (PName,PID)
    conn.execute(Query,Values)
def relate():
    PID = input("Please Enter Patient ID:")
    DID = input("Please Enter Doctor ID:")
    Query = "INSERT INTO doc_pat(D_code,P_code) VALUES (%s,%s)"
    Values = (DID,PID)
    conn.execute(Query,Values)
def ViewDoctors():
    Query = "SELECT * FROM doctors"
    conn.execute(Query)
def ViewPatients():
    Query = "SELECT * FROM patients"
    conn.execute(Query)
def ViewPatientsAndDoctors():
    Query = "SELECT * FROM patients JOIN doc_pat ON patients.id = P_code JOIN doctors ON doctors.id = D_code"
    conn.execute(Query)
def TerminateRelation():
    PID = input("Please Enter Patient ID:")
    DID = input("Please Enter Doctor ID:")
    Query = "DELETE FROM doc_pat WHERE D_code = %s AND P_code = %s"
    Values = (DID,PID)
    conn.execute(Query,Values)
def PatientsOfDoctor():
    DID = input("Please Enter Doctor ID:")
    Query = "SELECT * FROM patients JOIN doc_pat ON patients.id = P_code JOIN doctors ON doctors.id = D_code WHERE D_code = %s"
    Values = (DID,)
    conn.execute(Query,Values)
def DoctorsOfPatient():
    PID = input("Please Enter Patient ID:")
    Query = "SELECT * FROM patients JOIN doc_pat ON patients.id = P_code JOIN doctors ON doctors.id = D_code WHERE P_code = %s"
    Values = (PID,)
    conn.execute(Query,Values)
def Main():
    output()
    selection = input()
    while selection!='EXIT':
        selection = int(selection)
        if selection not in range(0,10):
            return
        elif selection==1:
            AddDoctor()
        elif selection==2:
            AddPatient()
        elif selection==3:
            relate()
        elif selection==4:
            ViewDoctors()
        elif selection==5:
            ViewPatients()
        elif selection==6:
            ViewPatientsAndDoctors()
        elif selection==7:
            TerminateRelation()
        elif selection==8:
            PatientsOfDoctor()
        elif selection==9:
            DoctorsOfPatient()
        if selection == 4 or selection == 5 or selection == 6 or selection ==8 or selection==9:
            result = conn.fetchall()
            for x in result:
                print(x)
        else:
            db.commit()
        output()
        selection = input()
[conn,db] = SQL_CONN()
Main()