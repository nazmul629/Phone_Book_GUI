from tkinter import *
import sqlite3 

con = sqlite3.connect('database.db')
cur=  con.cursor()

class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        
        self.geometry("650x550+600+200")
        self.title("My People")
        self.resizable(False,False)


        self.top = Frame(self,height="150",bg="white")
        self.top.pack(fill=X)
        
        self.bottom = Frame(self,heigh='650',bg='powder blue')
        self.bottom.pack(fill = X)

        # image
        self.top_img = PhotoImage(file='icon/people.png')
        self.top_img_label = Label(self.top,image=self.top_img,bg='white')
        self.top_img_label.place(x=70,y=25)

        #  heading
        self.top_heading = Label(self.top,text="My People",font="arial 20 bold",bg = 'white', fg="#ebb434")
        self.top_heading.place(x=150,y=30)


