from tkinter import *
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from HelperPage.Center import CenterPage
from PreRecord import Prerecord
from AddRecord import Addrecord

import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute("""Select Doctor.ID, People.Name, Doctor.HospitalID from Doctor, People where Doctor.PeopleID=People.ID;""")
DoctorList = cursor.fetchall()
cursor.execute(""" select ID, Password from People """)
PeopleList = cursor.fetchall()
conn.commit()
conn.close()

class Doctor:
    def __init__(self, id):
        self.entry_id = None
        self.entry_password = None

        self.id = id
        self.name = ""
        self.doctor = {}
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="White")
        self.y = 60
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        Label(self.root, text="Doctor Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=20)

        for i in DoctorList:
            if str(i[0]) == self.id:
                self.name = i[1]
                self.doctor = i
        Label(self.root, text="Name: " + self.name, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 40)
        Label(self.root, text="Doctor Id: " + str(self.id), font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 70)

        Label(self.root, text="Patient ID", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 110)
        self.entry_id = ttk.Entry(self.root, width=30)
        self.entry_id.place(x=250, y=self.y + 115)

        Label(self.root, text="Password", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=150, y=self.y + 160)
        self.entry_password = ttk.Entry(self.root, width=30, show="*")
        self.entry_password.place(x=250, y=self.y + 165)

        Button(self.root, text="Pre Record", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=lambda: self.getIdPassword("pre")
                   ).place(x=180, y=self.y + 240)

        Button(self.root, text="Add Record", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=lambda: self.getIdPassword("add")
                   ).place(x=330, y=self.y + 240)

    def getIdPassword(self, track):
        id = self.entry_id.get()
        password = self.entry_password.get()
        self.Authentication(id, password, track)

    def Authentication(self, id, password, track):
        id_first = id
        id_first = id_first[:3]
        if id_first == "191":
            for i in PeopleList:
                if str(i[0]) == id and i[1] == password:
                    if track == "pre":
                        self.root.destroy()
                        Prerecord(id)
                    elif track == "add":
                        Addrecord(id, self.doctor[0], self.doctor[2])
                    return
            else:
                messagebox.showinfo(title='Error', message="Id or Password is incorrect")
        else:
            messagebox.showinfo(title='Error', message="Id or Password is incorrect")

if __name__ == '__main__':
    Doctor('1930002')