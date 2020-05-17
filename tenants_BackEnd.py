import sqlite3
from tkinter import messagebox

# BackEnd
def tenantsData():
    con = sqlite3.connect("Tenants.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Tenantx(id INTEGER PRIMARY KEY, AptNo text,firstName1 text, lastName1 text,firstName2 text, lastName2 text,\
     phoneNo text, workPhoneNo text, parkingStallNo text, canopyStallNo text, Description text )")
    con.commit()
    con.close()

def addTenantRcd(AptNo, firstName1, lastName1, firstName2 , lastName2 ,phoneNo, workPhoneNo, parkingStallNo,
                 canopyStallNo, Description):
    con = sqlite3.connect("Tenants.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Tenantx VALUES (NULL,?,?,?,?,?,?,?,?,?,?)", (AptNo, firstName1, lastName1, firstName2, lastName2 ,phoneNo, workPhoneNo, parkingStallNo, canopyStallNo, Description))
    con.commit()
    con.close()


def viewData():
    con = sqlite3.connect("Tenants.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Tenantx")
    row = cur.fetchall()
    con.close()
    return row


def deleteRec(AptNo):
    con = sqlite3.connect("Tenants.db")

    cur = con.cursor()
    cur.execute("DELETE  FROM Tenantx WHERE id=?", (AptNo,))
    con.commit()
    con.close()




def searchData(AptNo="", firstName1="", lastName1="", firstName2="",lastName2="",phoneNo="", workPhoneNo="",
               parkingStallNo="", canopyStallNo="", Description=""):
    con = sqlite3.connect("Tenants.db")
    cur = con.cursor()
    cur.execute( "SELECT * FROM Tenantx WHERE AptNo=? COLLATE NOCASE OR firstName1=? COLLATE NOCASE OR lastName1=? COLLATE NOCASE OR firstName2=? COLLATE NOCASE OR lastName2=? COLLATE NOCASE",
        (AptNo, firstName1, lastName1, firstName2, lastName2))
    rows = cur.fetchall()
    con.close()
    return rows




def dataUpdate(AptNo="", firstName1="", lastName1="", firstName2="",lastName2="",phoneNo="", workPhoneNo="",
               parkingStallNo="", canopyStallNo="", Description=""):
    con = sqlite3.connect("Tenants.db")

    cur = con.cursor()
    cur.execute(
        "UPDATE Tenantx SET AptNo=?, firstName1=? , lastName1=? , firstName2=? , lastName2=?, phoneNo=? ,workPhoneNo=? , parkingStallNo=? , canopyStallNo=? , email=? , Description=?, WHERE id=? ",
        (
        AptNo, firstName1, lastName1, firstName2,lastName2,phoneNo, workPhoneNo, parkingStallNo, canopyStallNo,
        Description, AptNo)) #AptNo was id
    con.commit()
    con.close()



tenantsData()





