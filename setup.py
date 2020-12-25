import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="databaseSubmissions"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE doctors (name VARCHAR(255),department VARCHAR(255), id INT, PRIMARY KEY(id))")
mycursor.execute("CREATE TABLE patients (name VARCHAR(255), id INT, PRIMARY KEY(id))")
mycursor.execute("CREATE TABLE doc_pat (D_code INT, P_code INT, FOREIGN KEY (P_code) REFERENCES patients(id),FOREIGN KEY (D_code) REFERENCES doctors(id))")
