import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()

# cursor.execute("""
#     create table doctor (
#         id text,
#         name text,
#         password text
#         )""")

# cursor.execute("""
#     create table patient (
#         id text,
#         name text,
#         password text
#         )""")

# cursor.execute("""
#     insert into doctor values ("191-45042", "karim", "admin")
# """)

# cursor.execute("""
#     insert into patient values ("192-65443", "Roni", "admin")
# """)

# cursor.execute("""
#     create table patientDetails (
#         ID text,
#         Name text,
#         BloodGroup text,
#         Phone text,
#         Height text,
#         Weight int,
#         CurrentAdd text,
#         PermanentAdd text
#         )""")

# cursor.execute("""
#     insert into patientDetails values ("192-65442", "Bijoy", "O+", "01954323232", "5'02", 50, "Mirkadim Munshiganj Dhaka","Mirkadim Munshiganj Dhaka")
# """)

# cursor.execute("""
#     create table pharmacy (
#         id text,
#         name text,
#         password text
#         )""")

# cursor.execute("""
#     insert into pharmacy values ("193-48828", "Liton", "admin")
# """)
# cursor.execute("""
#     DELETE FROM doctor WHERE name = "Sakib";
# """)
#Password = admin

# cursor.execute("""
#     UPDATE patient
#     SET name = 'Bijoy'
#     WHERE id = "192-65442";
# """
# )

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


cursor.execute("""
    Select * from Doctor;
""")
print(cursor.fetchall())



conn.commit()
conn.close()

#Patient
#[('192-65441', 'Zakaria', 'admin'), ('192-65442', 'Bijoy', 'admin'), ('192-65443', 'Roni', 'admin')]
#Doctor
#[('191-45041', 'Jasmin', 'admin'), ('191-45042', 'karim', 'admin')]
#pharmacy
#[('193-48829', 'Sakib', 'admin'), ('193-48828', 'Liton', 'admin')]
