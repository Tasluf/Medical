from tkinter import *
from tkinter import ttk
from HelperPage.Center import CenterPage
import sqlite3


conn = sqlite3.connect("Medical.db")
cursor = conn.cursor()
cursor.execute(""" select ID, Name from People """)
PatinetName = cursor.fetchall()
conn.commit()
conn.close()

class Prerecord:
    def __init__(self, id):
        self.id = id
        self.patienName = ""
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.resizable(width=False, height=False)
        self.root.config(bg="white")
        self.y = 20
        self.item()
        CenterPage(self.root)
        self.root.mainloop()

    def item(self):
        conn = sqlite3.connect("Medical.db")
        cursor = conn.cursor()
        cursor.execute(f""" Select CheckUp.ProblemType, CheckUp.Medicine, CheckUp.Note,
        CheckUp.Date, People.Name, Hospital.Name
        from CheckUp, Hospital, Doctor, People where CheckUp.PeopleID={int(self.id)} and 
        CheckUp.HospitalID = Hospital.ID  and CheckUp.DoctorID = Doctor.ID and Doctor.PeopleID = People.ID
      """)
        PreRecordList = cursor.fetchall()
        conn.commit()
        conn.close()

        if len(PreRecordList) == 0:
            Label(self.root, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").place(x=250,
                                                                                                            y=self.y)
            Label(self.root, text="This patient has no record", font=("Ubuntu", 12), fg="#707070", bg="white").place(
                x=220, y=self.y + 50)
        else:
            for i in PatinetName:
                if str(i[0]) == self.id:
                    self.patienName = i[1]

            frame = Frame(self.root, bg="white")
            frame.pack()

            Label(frame, text="Patient Page", font=("Ubuntu Bold", 16), fg="#707070", bg="white").pack(pady=10)
            Label(frame, text=self.patienName, font=("Ubuntu", 12), fg="#707070", bg="white").pack()

            main_frame = Frame(self.root, bg="white")
            main_frame.pack(fill=BOTH, expand=True, pady=15)
            second_frame = self.canva(main_frame)

            for i in PreRecordList:
                Label(second_frame, text=i[0], font=("Ubuntu Bold", 12), fg="#707070", bg="white").pack(
                    side=TOP, padx=30, pady=5, anchor=NW)
                Label(second_frame, text="Last Check Up date: " + i[3], font=("Ubuntu", 12), fg="#707070",
                      bg="white").pack(side=TOP, padx=30, pady=3,
                                       anchor=NW)
                Label(second_frame, text="Doctor Name: " + i[4], font=("Ubuntu", 12), fg="#707070",
                      bg="white").pack(side=TOP, padx=30, pady=3,
                                       anchor=NW)
                Label(second_frame, text="Hospital Name: " + i[5], font=("Ubuntu", 12), fg="#707070",
                      bg="white").pack(side=TOP, padx=30, pady=3,
                                       anchor=NW)
                Label(second_frame, text="Medicine: " + "\n" + i[1], font=("Ubuntu", 12), fg="#707070",
                      bg="white", justify=LEFT).pack(side=TOP, padx=30, pady=3, anchor=NW)
                Label(second_frame, text="Note: " + "\n" + i[2], font=("Ubuntu", 12), fg="#707070", bg="white",
                      justify=LEFT, wraplength=550).pack(side=TOP, padx=30, anchor=NW)

    def canva(self, main_frame):
        my_canvas = Canvas(main_frame, bg="white")
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = Frame(my_canvas, bg="white")
        my_canvas.create_window((0, 0), window=second_frame, anchor='nw')
        return second_frame


if __name__ == '__main__':
    Prerecord("1910003")
