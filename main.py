from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice
import string

# Variables
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digits = string.digits
simbols = string.punctuation

# Colors
blackColor = "#050505"
whiteColor = "#feffff"
tealColor = "#008080"

# Functions


def passwordGenerate():
    password = ''
    values = ''
    passwordLength = int(spin.get())

    if upperCaseCheckIf.get() == upperCase:
        values += upperCase

    if lowerCaseCheckIf.get() == lowerCase:
        values += lowerCase

    if digitsCheckIf.get() == digits:
        values += digits

    if simbolsCheckIf.get() == simbols:
        values += simbols

    if values == '':
        messagebox.showinfo("Error", "Select any option")
    else:
        for i in range(passwordLength):
            password += choice(values)

        appPassword['text'] = password

        mainFrame.clipboard_clear()
        mainFrame.clipboard_append(password)

        messagebox.showinfo("Success", "The password was copied successfully")


# UI Configurations
root = Tk()
root.title('Password Generator')
root.geometry('300x360')
root.minsize(300, 360)
root.maxsize(300, 360)
root.configure(bg=whiteColor)

# Frames
style = ttk.Style(root)
style.theme_use("clam")

mainFrame = Frame(root, width=300, height=360, pady=0, padx=0, relief="flat")
mainFrame.grid(row=0, column=0)

appName = Label(mainFrame, text="Password Generator", width=50, height=1,
                padx=0, relief="flat", anchor="nw", font=('Ivy 16 bold'), fg=blackColor)
appName.place(x=45, y=2)

appDivision = Label(mainFrame, text="", width=300, height=1, padx=0,
                    relief="flat", anchor="nw", font=('Arial 1'), bg=tealColor, fg=whiteColor)
appDivision.place(x=0, y=35)

var = IntVar()
var.set(8)

appInfo = Label(mainFrame, text="Select at least one option", height=1,
                padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), fg=blackColor)
appInfo.place(x=60, y=50)

appPassword = Label(mainFrame, text="- - -", width=24, height=2, padx=0, relief="solid",
                    anchor="center", font=('Ivy 10 bold'), fg=blackColor, bg=whiteColor)
appPassword.place(x=50, y=80)

# Password Length
spin = Spinbox(mainFrame, from_=0, to=20, width=5, textvariable=var)
spin.place(x=30, y=140)

appInfo = Label(mainFrame, text="Password Length", height=1, padx=0, relief="flat",
                anchor="nw", justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.place(x=80, y=140)

# Uppercase Letters
upperCaseCheckIf = StringVar()
upperCaseCheckIf.set(False)

upperCaseCheckBox = Checkbutton(
    mainFrame, width=1, var=upperCaseCheckIf, onvalue=upperCase, offvalue='off')
upperCaseCheckBox.place(x=25, y=170)

appInfo = Label(mainFrame, text="Capital Letters", height=1, padx=0, relief="flat",
                anchor="nw", justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.place(x=65, y=170)

# Lowercase Letters
lowerCaseCheckIf = StringVar()
lowerCaseCheckIf.set(False)

lowerCaseCheckBox = Checkbutton(
    mainFrame, width=1, var=lowerCaseCheckIf, onvalue=lowerCase, offvalue='off')
lowerCaseCheckBox.place(x=25, y=200)

appInfo = Label(mainFrame, text="Small Letters", height=1, padx=0, relief="flat",
                anchor="nw", justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.place(x=65, y=200)

# Digits
digitsCheckIf = StringVar()
digitsCheckIf.set(False)

digitsCheckBox = Checkbutton(
    mainFrame, width=1, var=digitsCheckIf, onvalue=digits, offvalue='off')
digitsCheckBox.place(x=25, y=230)

appInfo = Label(mainFrame, text="Numbers", height=1, padx=0, relief="flat",
                anchor="nw", justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.place(x=65, y=230)

# Simbols
simbolsCheckIf = StringVar()
simbolsCheckIf.set(False)

simbolsCheckBox = Checkbutton(
    mainFrame, width=1, var=simbolsCheckIf, onvalue=simbols, offvalue='off')
simbolsCheckBox.place(x=25, y=260)

appInfo = Label(mainFrame, text="Special Characters", height=1, padx=0, relief="flat",
                anchor="nw", justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.place(x=65, y=260)

# Buttons
generatePasswordButton = Button(mainFrame, command=passwordGenerate, text="Generate Password", width=30,
                                height=1, overrelief=SOLID,  bg=tealColor, fg=whiteColor, font=('Ivy 10 bold'), anchor="center", relief=FLAT)
generatePasswordButton.place(x=28, y=310)

root.mainloop()
