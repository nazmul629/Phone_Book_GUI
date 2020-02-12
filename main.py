from tkinter import *
from view_people import MyPeople
import datetime


class Application(object):
    def __init__(self,master):
        self.master = master

        self.top = Frame(master,height = 150, bg='white') # For Top Bar 
        self.top.pack(fill = X)                                                                     

        self.bottom = Frame(master,heigh=650,bg='#34baeb') # For Butto m bar
        self.bottom.pack(fill = X)
        

        # top frame Image 
        self.top_image = PhotoImage(file="icon/logo.png")
        
        self.top_image_label = Label(self.top, image = self.top_image,bg='white')
        self.top_image_label.place(x=70,y=25)

        # Heading
        self.top_heading = Label(self.top,text="My PhoneBook App",font="arial 20 bold",bg = 'white', fg="#ebb434")
        self.top_heading.place(x=150,y=30)

        # Date 
        date = datetime.datetime.now().date()
        date = str(date)
       
       # Showing Top manu
        self.date_label = Label(self.top, text="Today's Date:\n"+date,font="arial 15 bold",fg="#ebb434",bg="white")
        self.date_label.place(x=480,y=20)

      # View Button
        self.ViewButton = Button(self.bottom, text = "View People",font="arial 15 bold",bg='white',fg='#42bcf5',bd=4, command = self.my_people)
        self.ViewButton.place(x=250,y=70)


      #  Add Button
        self.AddButton = Button(self.bottom, text = " Add People",font="arial 15 bold",bd=4,bg='white',fg='#42bcf5')
        self.AddButton.place(x=250,y=130)
    
         # About us
        self.AddButton = Button(self.bottom, text = "   About us  ",font="arial 15 bold",bd=3,bg='white',fg='#42bcf5')
        self.AddButton.place(x=250,y=190)


    def my_people(self):
        people = MyPeople()





def main():
    root = Tk()
    app = Application(root)
    root.title("PhoneBook App")
    root.geometry('650x550+350+250')
    root.resizable(False,False)
    # root.configure(bg = 'white')
    root.mainloop()

if __name__ == '__main__':
    main()