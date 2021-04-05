from tkinter import *
from tkinter import ttk
from tkinter import Button
from tkinter import messagebox
from HelperPage.Center import CenterPage
import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from People """)
PatientList = cursor.fetchall()
cursor.execute(""" select Doctor.ID, People.Name from Doctor, People where Doctor.PeopleID = People.ID """)
DoctorList = cursor.fetchall()
cursor.execute(""" select * from Hospital """)
HospitaltList = cursor.fetchall()
conn.commit()
conn.close()

class Addrecord:
    entry_Problem = None
    entry_Date = None
    entry_Medicine = None
    entry_Note = None

    def __init__(self, id, doctorID, HospitalID):
        self.id = id
        self.HostipalID = HospitalID
        self.DoctorID = doctorID
        self.name = ""
        self.doctorName = ""
        self.hospitalName = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        x = 50
        y = 5
        Label(self.root, text="Add record", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=260, y=y+5)
        for i in PatientList:
            if str(i[0]) == self.id:
                self.name = i[5]

        for i in DoctorList:
            if i[0] == self.DoctorID:
                self.doctorName = i[1]

        for i in HospitaltList:
            if i[0] == self.HostipalID:
                self.hospitalName = i[1]

        Label(self.root, text="Patient Name: " + self.name, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=50, y=y + 40)
        Label(self.root, text="Doctor Name: "+self.doctorName, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=400, y=y + 40)
        Label(self.root, text="Hospital Name: "+self.hospitalName, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=180, y=y + 65)

        Label(self.root, text="Problem title", font=("Ubuntu", 10), fg="#707070", bg="white").place(x=x, y=y + 90)
        self.entry_Problem = ttk.Entry(self.root, width=30)
        self.entry_Problem.place(x=x+5, y=y + 120)
        Label(self.root, text="Date", font=("Ubuntu", 10), fg="#707070", bg="white").place(x=390, y=y + 90)
        self.entry_Date = ttk.Entry(self.root, width=30)
        self.entry_Date.place(x=x+345, y=y + 120)
        Label(self.root, text="Medicine", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=y + 170)
        self.entry_Medicine = Text(self.root, height=4, width=50, bd=2)
        self.entry_Medicine.place(x=x + 85, y=y + 170)
        Label(self.root, text="Note", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x, y=y + 260)
        self.entry_Note = Text(self.root, height=5, width=50, bd=2)
        self.entry_Note.place(x=x + 85, y=y + 270)
        Button(self.root, text="Add", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=self.add_details
                   ).place(x=290, y=y + 390)

    def add_details(self):
        Problem = self.entry_Problem.get()
        Date = self.entry_Date.get()
        Medicine = self.entry_Medicine.get("1.0", END)
        Note = self.entry_Note.get("1.0", END)
        if Problem == "":
            messagebox.showinfo(title='Error', message="Please Enter Diseases name")
        elif Date == "":
            messagebox.showinfo(title='Error', message="Please Enter Date")
        else:
            conn = sqlite3.connect("Medical.db")
            cursor = conn.cursor()

            cursor.execute(f"""insert into CheckUp values ({self.HostipalID},
                            {int(self.id)}, {self.DoctorID}, "{Problem}", "{Medicine}",
                            "{Note}", "{Date}"
                            )
                            """)

            conn.commit()
            conn.close()
            messagebox.showinfo(title='information', message="Successfull Added")
            self.root.destroy()


if __name__ == '__main__':
    Addrecord("1910001", 1930002, 1920001)