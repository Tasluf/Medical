from tkinter import *
from tkinter import Button
from tkinter import ttk
from tkinter import messagebox
from HelperPage.Center import CenterPage
import sqlite3

class AddPharmacyShop:
    entry_id = None
    entry_Name = None
    entry_Phone = None
    entry_Current_Address = None
    entry_Current_District = None
    entry_Current_Division = None

    def __init__(self):
        y = 30
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        Label(self.root, text="Add Pharmacy Shop", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=40)

        self.textInput("ID", 50, 130, y+60, 'entry_id')
        self.textInput("Name", 50, 130, y + 100, 'entry_Name')
        self.textInput("Phone", 50, 130, y + 140, 'entry_Phone')
        self.textInput("CAddress", 330, 410, y + 140, 'entry_Current_Address')
        self.textInput("CDistrict", 330, 410, y + 100, 'entry_Current_District')
        self.textInput("CDivision", 330, 410, y + 60, 'entry_Current_Division')

        Button(self.root, text="Add Parmacy Shop", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
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
        Name = globals()['entry_Name'].get()
        Phone = globals()['entry_Phone'].get()
        Current_Address = globals()['entry_Current_Address'].get()
        Current_District = globals()['entry_Current_District'].get()
        Current_Division = globals()['entry_Current_Division'].get()

        try:
            conn = sqlite3.connect("Medical.db")
            cursor = conn.cursor()

            cursor.execute(f"""
                        insert into PharmacyShop values ({id}, "{Name}", "{Current_Address}",
                        "{Current_District}", "{Current_Division}", "{Phone}"
                        )
                    """)

            conn.commit()
            conn.close()
            messagebox.showinfo(title='information', message="Successfully Added")
            self.root.destroy()
        except:
            messagebox.showinfo(title='Error', message="Failed To Add")



if __name__ == '__main__':
    AddPharmacyShop()