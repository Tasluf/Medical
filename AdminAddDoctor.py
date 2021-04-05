from tkinter import *
from tkinter import Button
from tkinter import ttk
from tkinter import messagebox
from Center import CenterPage
import sqlite3

class AddDoctor:
    entry_id = None
    entry_Password = None
    entry_PeopleID = None
    entry_HospitalID = None
    entry_DoctorType = None

    def __init__(self):
        y = 30
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")

        Label(self.root, text="Add Doctor", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=40)

        self.textInput("ID", 50, 130, y+60, 'entry_id')
        self.textInput("Password", 50, 130, y + 100, 'entry_Password')
        self.textInput("DoctorType", 200, 310, y + 160, 'entry_DoctorType')
        self.textInput("HospitalID", 330, 430, y + 100, 'entry_HospitalID')
        self.textInput("PeopleID", 330, 430, y + 60, 'entry_PeopleID')

        Button(self.root, text="Add Doctor", bg="#4B4B4B", fg="#FFFDFC", bd="0", padx='20', pady="3",
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
        Password = globals()['entry_Password'].get()
        DoctorType = globals()['entry_DoctorType'].get()
        HospitalID = globals()['entry_HospitalID'].get()
        PeopleID = globals()['entry_PeopleID'].get()

        try:
            conn = sqlite3.connect("Medical.db")
            cursor = conn.cursor()

            cursor.execute(f"""
                        insert into Doctor values ({id}, "{Password}", {PeopleID},
                        {HospitalID}, "{DoctorType}"
                        )
                    """)

            conn.commit()
            conn.close()
            messagebox.showinfo(title='information', message="Successfully Added")
            self.root.destroy()
        except:
            messagebox.showinfo(title='Error', message="Failed To Add")



if __name__ == '__main__':
    AddDoctor()