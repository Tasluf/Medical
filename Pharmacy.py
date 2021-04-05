from tkinter import *
from tkinter import Button
from tkinter import ttk
from tkinter import messagebox
from HelperPage.Center import CenterPage
from Medicien import MedicineClass
import sqlite3

conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select * from People """)
PatientList = cursor.fetchall()
cursor.execute("""
    select Pharmacist.ID, People.Name, PharmacyShop.Address, PharmacyShop.District, PharmacyShop.Division
    from Pharmacist, People, PharmacyShop 
    where Pharmacist.PeopleID = People.ID and Pharmacist.PharmacyShopID = PharmacyShop.ID
    ;
""")
PharmacyList = cursor.fetchall()
conn.commit()
conn.close()



class pharmacyPage:
    def __init__(self, id):
        self.entry_id = None
        self.id = id
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="White")
        self.y = 20
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        pharmacist = dict()
        for i in PharmacyList:
            if str(i[0]) == self.id:
                pharmacist = i

        Label(self.root, text="Pharmacy Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=260, y=self.y)
        Label(self.root, text="ID: " + self.id, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=100, y=self.y + 60)
        Label(self.root, text="Name: " + pharmacist[1], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=100, y=self.y + 90)
        Label(self.root, text="Shop Address: " + f"{pharmacist[2]}, {pharmacist[3]}, {pharmacist[4]}",
              font=("Ubuntu", 12), fg="#707070", bg="white").place(x=100,y=self.y + 120)
        Label(self.root, text="Patient ID: ", font=("Ubuntu", 12), fg="#707070", bg="white").place(x=130, y=self.y + 170)
        self.entry_id = ttk.Entry(self.root, width=30)
        self.entry_id.place(x=250, y=self.y + 170)

        Button(self.root, text="Login", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3", activebackground="#2D2C2C", activeforeground="#FFFDFC",
                   command=self.getIdPassword
                   ).place(x=280, y=self.y + 240)

    def getIdPassword(self):
        id = self.entry_id.get()
        match = False
        for i in PatientList:
            if str(i[0]) == id:
                match = True

        if match:
            self.root.destroy()
            MedicineClass(id)
        else:
            messagebox.showinfo(title='Error', message="Id is incorrect")


if __name__ == '__main__':
    pharmacyPage("1950001")
