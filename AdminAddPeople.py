from tkinter import *
from tkinter import Button
from tkinter import ttk
from tkinter import messagebox
from HelperPage.Center import CenterPage
import sqlite3

class AddPeople:
    entry_id = None
    entry_password = None
    entry_MotherID = None
    entry_FatherID = None
    entry_NID = None
    entry_Name = None
    entry_BOD = None
    entry_BloodGroup = None
    entry_Phone = None
    entry_Height = None
    entry_Weight = None
    entry_Email = None
    entry_Current_Address = None
    entry_Current_District = None
    entry_Current_Division = None
    entry_Permanent_Address = None

    def __init__(self):
        y = 30
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        Label(self.root, text="Add People", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=40)

        self.textInput("ID", 50, 130, y+60, 'entry_id')
        self.textInput("Password", 50, 130, y + 100, 'entry_password')
        self.textInput("MotherID", 50, 130, y + 140, 'entry_MotherID')
        self.textInput("FatherID", 50, 130, y + 180, 'entry_FatherID')
        self.textInput("NID", 50, 130, y + 220, 'entry_NID')
        self.textInput("Name", 50, 130, y + 260, 'entry_Name')
        self.textInput("BOD", 50, 130, y + 300, 'entry_BOD')
        self.textInput("Blood", 50, 130, y + 340, 'entry_BloodGroup')
        self.textInput("Phone", 330, 410, y + 60, 'entry_Phone')
        self.textInput("Height", 330, 410, y + 100, 'entry_Height')
        self.textInput("Weight", 330, 410, y + 140, 'entry_Weight')
        self.textInput("Email", 330, 410, y + 180, 'entry_Email')
        self.textInput("CAddress", 330, 410, y + 220, 'entry_Current_Address')
        self.textInput("CDistrict", 330, 410, y + 260, 'entry_Current_District')
        self.textInput("CDivision", 330, 410, y + 300, 'entry_Current_Division')
        self.textInput("PAddress", 330, 410, y + 340, 'entry_Permanent_Address')

        Button(self.root, text="Add People", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
               activebackground="#2D2C2C", activeforeground="#FFFDFC",
               command=self.show
               ).place(x=270, y=y + 380)

        CenterPage(self.root)
        self.root.mainloop()

    def textInput(self, text, x1, x2, y, Name, show=""):
        Label(self.root, text=text, font=("Ubuntu", 12), fg="#707070", bg="white").place(x=x1, y=y)
        globals()[Name] = ttk.Entry(self.root, width=20, show=show)
        globals()[Name].place(x=x2, y=y)

    def show(self):
        id = globals()['entry_id'].get()
        password = globals()['entry_password'].get()
        MotherID = globals()['entry_MotherID'].get()
        FatherID = globals()['entry_FatherID'].get()
        NID = globals()['entry_NID'].get()
        Name = globals()['entry_Name'].get()
        BOD = globals()['entry_BOD'].get()
        BloodGroup = globals()['entry_BloodGroup'].get()
        Phone = globals()['entry_Phone'].get()
        Height = globals()['entry_Height'].get()
        Weight = globals()['entry_Weight'].get()
        Email = globals()['entry_Email'].get()
        Current_Address = globals()['entry_Current_Address'].get()
        Current_District = globals()['entry_Current_District'].get()
        Current_Division = globals()['entry_Current_Division'].get()
        Permanent_Address = globals()['entry_Permanent_Address'].get()

        try:
            conn = sqlite3.connect("Medical.db")
            cursor = conn.cursor()

            cursor.execute(f"""
                        insert into People values ({id}, "{password}", {MotherID}, {FatherID},
                        "{NID}", "{Name}", "{BOD}", "{BloodGroup}", "{Phone}", "{Height}",
                        {Weight}, "{Current_Address}", "{Current_District}", "{Current_Division}",
                        "{Permanent_Address}", "{Email}"
                        )
                    """)

            conn.commit()
            conn.close()
            messagebox.showinfo(title='information', message="Successfully Added")
            self.root.destroy()
        except:
            messagebox.showinfo(title='Error', message="Failed To Add")



if __name__ == '__main__':
    AddPeople()