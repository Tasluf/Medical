import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()


# cursor.execute("""
#     create table People (
#         ID int primary key,
#         Password text not null,
#         MotherID int,
#         FatherID int,
#         NID text not null,
#         Name text not null,
#         BOD timestamp not null,
#         BloodGroup text,
#         Phone text,
#         Height text,
#         Weight int,
#         CurrentAdd text not null,
#         CDistrict text not null,
#         CDivision text,
#         PermanentAdd text,
#         Email text,
#         )""")

# cursor.execute("""
#     create table Hospital (
#         ID int primary key,
#         Name text not null,
#         Address text not null,
#         District text not null,
#         Division text not null,
#         Phone text not null,
#         Email text not null
#         )""")

# cursor.execute("""
#     create table Doctor (
#         ID int primary key,
#         Password text not null,
#         PeopleID int not null,
#         HospitalID int not null,
#         DoctorType text not null
#         )""")

# cursor.execute("""
#     create table PharmacyShop (
#         ID int primary key,
#         Name text not null,
#         Address text not null,
#         District text not null,
#         Division text not null,
#         Phone text not null
#         )""")

# cursor.execute("""
#     create table Pharmacist (
#         ID int primary key,
#         Password text not null,
#         PharmacyShopID int not null,
#         PeopleID int not null
#         )""")

# cursor.execute("""
#     create table CheckUp (
#         HospitalID int not null,
#         PeopleID int not null,
#         DoctorID int not null,
#         ProblemType text not null,
#         Medicine text not null,
#         Note text not null,
#         Date timestamp not null
#         )""")

#select Pharmacist.ID, People.Name, PharmacyShop.Address, PharmacyShop.District, PharmacyShop.Division
    # from Pharmacist, People, PharmacyShop
    # where Pharmacist.PeopleID = People.ID and Pharmacist.PharmacyShopID = PharmacyShop.ID

cursor.execute("""
     Select * from Pharmacist
     """)
a = cursor.fetchall()
for i in a:
    print(i)
# print(cursor.fetchall())

conn.commit()
conn.close()

