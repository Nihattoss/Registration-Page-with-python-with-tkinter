from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.geometry("600x400")
L1 = Label(root, text = "Nihattoss Registration Page", font = "arial 15 bold")
L1.grid(row = 0, column = 3)
    
name_and_surname = Label(root, width = 20, height = 3, text = "Your Name And Surname",font = " 15")
name_and_surname.grid(row = 1, column = 2)

e_mail = Label(root, width = 20, height = 3, text="Your e-mail",font = " 15")
e_mail.grid(row = 2, column = 2)

password = Label(root, width = 20, height = 3, text = "Your Password", font ="15")
password.grid(row = 3, column = 2)

Phone = Label(root, width = 20, height = 3, text = "Your phone number", font = "15")
Phone.grid(row = 4, column = 2)

#**********************************************************************************
NameSurname_value = StringVar
Email_value = StringVar
Password_value = StringVar
Phone_value = StringVar

#**************************************************************************************
NameSurname_entry = Entry(root, textvariable = NameSurname_value)
Email_entry = Entry(root, textvariable = Email_value)
Password_entry = Entry(root, textvariable = Password_value)
Phone_entry = Entry(root, textvariable = Phone_value)

#*************************************************************************************
NameSurname_entry.grid(row = 1, column = 3)
Email_entry.grid(row = 2, column = 3)
Password_entry.grid(row = 3, column = 3)
Phone_entry.grid(row = 4, column = 3)

#*****************************************************************************************
Send = Button(root, width=10, height = 2, command = lambda:define_sign(1))
Send.grid(row = 5, column = 3)
Send.config(text = "Send")

hatirla = Button(root, width = 15, height = 2, command = lambda:define_sign(2))
hatirla.grid(row = 5, column = 2)
hatirla.config(text = "Remember Me")

def define_sign(number):
    if number == 1:
        send()
    if number == 2:
        remember()
def remember():
    hatirla.config(bg = "light green")
    showinfo("Status","Your informations saved.")
    hatirla.config(bg= "white")

def send():
    Send.config(bg = "light green")
    showinfo("Status","Your registration sent successfully.")
    Send.config(bg = "white")
    
root.mainloop()
