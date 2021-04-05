from tkinter import *
from HelperPage.Center import CenterPage
import sqlite3


class MedicineClass:
    def __init__(self, id):
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
        conn = sqlite3.connect("Medical.db")
        cursor = conn.cursor()
        cursor.execute(f""" Select * from CheckUp where PeopleID = {int(self.id)} """)
        PreRecordList = cursor.fetchall()
        cursor.execute(f"""
        Select Name from People where ID = {int(self.id)} ;
        """)
        patientName = cursor.fetchone()
        conn.commit()
        conn.close()

        if len(PreRecordList) == 0:
            Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250,
                                                                                                            y=self.y)
            Label(self.root, text="This patient has no record", font=("Ubuntu", 12), fg="#707070",
                  bg="white").place(x=220, y=self.y + 50)
        else:
            medicien = PreRecordList[len(PreRecordList)-1]

            Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250, y=20)
            Label(self.root, text=patientName[0], font=("Ubuntu", 12), fg="#707070", bg="white").place(x=300,
                                                                                                       y=self.y + 50)
            Label(self.root, text="Current Medicine", font=("Ubuntu Bold", 12), fg="#707070", bg="white").place(x=30,
                                                                                                                y=self.y + 90)
            medicienList = medicien[4].split('\n')
            gap = 130
            for i in medicienList:
                Label(self.root, text=i, font=("Ubuntu", 12), fg="#707070", bg="white", justify=LEFT).place(x=30,
                                                                                             y=self.y + gap)
                gap += 30



if __name__ == '__main__':
    MedicineClass("1910001")