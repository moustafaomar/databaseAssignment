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
            EXIT: exit application
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
def db_exec(query, params=None):
    if not params:
        result = conn.fetchall()
        for x in result:
            print(x)
        if(result):
            return True
    else:
        db.commit()
        if(conn.rowcount > 0):
            return True
    return False
def AddDoctor(DName,DDep,DID):
    Query = "INSERT INTO Doctors (name,department,id) VALUES (%s,%s,%s)"
    Values = (DName,DDep,DID)
    if(db_exec(conn.execute(Query,Values),Values)):
        return True
    else:
        return False
def AddPatient(PName,PID):
    Query = "INSERT INTO patients(name,id) VALUES (%s,%s)"
    Values = (PName,PID)
    if(db_exec(conn.execute(Query,Values),Values)):
        return True
    else:
        return False
def relate(DID,PID):
    Query = "INSERT INTO doc_pat(D_code,P_code) VALUES (%s,%s)"
    Values = (DID,PID)
    if(db_exec(conn.execute(Query,Values),Values)):
        return True
    else:
        return False
def ViewDoctors():
    Query = "SELECT name FROM doctors"
    if(db_exec(conn.execute(Query))):
        return True
    else:
        return False
def ViewPatients():
    Query = "SELECT name FROM patients"
    if(db_exec(conn.execute(Query))):
        return True
    else:
        return False
def ViewPatientsAndDoctors():
    Query = "SELECT patients.name,doctors.name FROM patients JOIN doc_pat ON patients.id = P_code JOIN doctors ON doctors.id = D_code"
    if(db_exec(conn.execute(Query))):
        return True
    else:
        return False
def TerminateRelation(DID,PID):
    Query = "DELETE FROM doc_pat WHERE D_code = %s AND P_code = %s"
    Values = (DID,PID)
    if(db_exec(conn.execute(Query,Values),Values)):
        return True
    else:
        return False
def PatientsOfDoctor(DID):
    Query = "SELECT patients.name FROM patients JOIN doc_pat ON patients.id = P_code JOIN doctors ON doctors.id = D_code WHERE D_code = %s"
    Values = (DID,)
    if(db_exec(conn.execute(Query,Values),Values)):
        return True
    else:
        return False
def DoctorsOfPatient(PID):
    Query = "SELECT doctors.name FROM patients JOIN doc_pat ON patients.id = P_code JOIN doctors ON doctors.id = D_code WHERE P_code = %s"
    Values = (PID,)
    if(db_exec(conn.execute(Query,Values),Values)):
        return True
    else:
        return False
def Main():
    output()
    selection = input()
    while selection!='EXIT':
        selection = int(selection)
        if selection not in range(0,10):
            return
        elif selection==1:
            DName = input("Please Enter Doctor Name:")
            DDep = input("Please Enter Doctor Department:")
            DID = input("Please Enter Doctor ID:")
            AddDoctor(DName,DDep,DID)
        elif selection==2:
            PName = input("Please Enter Patient Name:")
            PID = input("Please Enter Patient ID:")
            AddPatient(PName,PID)
        elif selection==3:
            PID = input("Please Enter Patient ID:")
            DID = input("Please Enter Doctor ID:")
            relate(DID,PID)
        elif selection==4:
            ViewDoctors()
        elif selection==5:
            ViewPatients()
        elif selection==6:
            ViewPatientsAndDoctors()
        elif selection==7:
            PID = input("Please Enter Patient ID:")
            DID = input("Please Enter Doctor ID:")
            TerminateRelation(DID,PID)
        elif selection==8:
            DID = input("Please Enter Doctor ID:")
            PatientsOfDoctor(DID)
        elif selection==9:
            PID = input("Please Enter Patient ID:")
            DoctorsOfPatient(PID)
        output()
        selection = input()
[conn,db] = SQL_CONN()
if __name__ == "__main__":
    Main()