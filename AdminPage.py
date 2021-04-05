from tkinter import *
from tkinter import Button
from tkinter import ttk
from HelperPage.Center import CenterPage
from AdminAddPeople import AddPeople
from AdminAddHospital import AddHospital
from AdminAddDoctor import AddDoctor
from AdminAddPharmacyShop import AddPharmacyShop
from AdminAddPharmacist import AddPharmacist

class AdminPage:

    def __init__(self):
        y = 30
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        Label(self.root, text="Admin Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=40)


        Button(self.root, text="Add People", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
               activebackground="#2D2C2C", activeforeground="#FFFDFC",
               command=self.AddPeoplePage
               ).place(x=40, y=y + 70)

        Button(self.root, text="Add Hospital", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
               activebackground="#2D2C2C", activeforeground="#FFFDFC",
               command=self.AddHospitalPage
               ).place(x=240, y=y + 70)

        Button(self.root, text="Add Doctor", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
               activebackground="#2D2C2C", activeforeground="#FFFDFC",
               command=self.AddDoctorPage
               ).place(x=440, y=y + 70)

        Button(self.root, text="Add Pharmacy", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
               activebackground="#2D2C2C", activeforeground="#FFFDFC",
               command=self.AddPharmacyShop
               ).place(x=40, y=y + 140)

        Button(self.root, text="Add Pharmacist", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
               activebackground="#2D2C2C", activeforeground="#FFFDFC",
               command=self.AddPharmacist
               ).place(x=240, y=y + 140)

        CenterPage(self.root)
        self.root.mainloop()

    def textInput(self, text, x1, x2, y, Name, show=""):
        Label(self.root, text=text, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x1, y=y)
        globals()[Name] = ttk.Entry(self.root, width=20, show=show)
        globals()[Name].place(x=x2, y=y)


    def AddPeoplePage(self):
        AddPeople()

    def AddHospitalPage(self):
        AddHospital()

    def AddDoctorPage(self):
        AddDoctor()

    def AddPharmacyShop(self):
        AddPharmacyShop()

    def AddPharmacist(self):
        AddPharmacist()

if __name__ == '__main__':
    AdminPage()