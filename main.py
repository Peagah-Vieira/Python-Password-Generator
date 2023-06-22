from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice
import string

#Variables
lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digits = string.digits
simbols= string.punctuation	

#Colors
blackColor = "#444466"  
whiteColor = "#feffff"  
blueColor = "#6f9fbd"  
redColor = "#f05a43"  

#Functions
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
        messagebox.showinfo("Erro","Selecione alguma opção")
    else:
        for i in range(passwordLength):
            password += choice(values)
            
        appPassword['text'] = password
        
        boxFrame.clipboard_clear()
        boxFrame.clipboard_append(password)
        
        messagebox.showinfo("Sucesso","A senha foi copiada com sucesso") 

#UI Configurations
root = Tk()
root.title('Password Generator')
root.geometry('300x360')
root.configure(bg = whiteColor)

#Frames
style = ttk.Style(root)
style.theme_use("clam")

mainFrame = Frame(root, width= 300, height= 110, pady= 0, padx= 0, relief= "flat")
mainFrame.grid(row= 0, column= 0)

boxFrame = Frame(root, width= 300, height= 220, pady= 0, padx= 0, relief= "flat")
boxFrame.grid(row= 1, column= 0)

appName = Label(mainFrame, text= "Password Generator", width= 50, height= 1, padx= 0, relief= "flat", anchor= "nw", font= ('Ivy 16 bold'), fg= blackColor)
appName.place(x= 35, y= 2)

appDivision = Label(mainFrame, text="", width= 400, height= 1, padx= 0, relief= "flat", anchor= "nw", font=( 'Arial 1'), bg= redColor, fg= whiteColor)
appDivision.place(x=0, y=35)

var = IntVar()
var.set(8)

appInfo = Label(mainFrame, text="Número total de caracteres na senha", height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), fg=blackColor)
appInfo.place(x=15, y=60)

spin = Spinbox(mainFrame, from_=0, to=20, width=5, textvariable=var)
spin.place(x=20, y=90)

appPassword = Label(boxFrame , text="- - -", width=20, height=2, padx=0, relief="solid", anchor="center", font=('Ivy 10 bold'), fg=blackColor)
appPassword.grid(row=0, column=0, columnspan=2,  sticky=NSEW, pady=10, padx=2)

#Uppercase Letters
appInfo = Label(boxFrame, text="ABC Letras maiúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.grid(row=1, column=1,  sticky=NSEW, pady=5, padx=2)

upperCaseCheckIf = StringVar()
upperCaseCheckIf.set(False)

upperCaseCheckBox = Checkbutton(boxFrame,width=1, var=upperCaseCheckIf,onvalue=upperCase, offvalue='off')
upperCaseCheckBox.grid(row=1, column=0,  sticky=NSEW, pady=5, padx=2)

#Lowercase Letters
appInfo = Label(boxFrame, text="abc Letras minúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.grid(row=2, column=1,  sticky=NSEW, pady=5, padx=2)

lowerCaseCheckIf = StringVar()
lowerCaseCheckIf.set(False)  

lowerCaseCheckBox = Checkbutton(boxFrame,width=1, var=lowerCaseCheckIf,onvalue=lowerCase, offvalue='off')
lowerCaseCheckBox.grid(row=2, column=0,  sticky=NSEW, pady=5, padx=2)

#Digits
appInfo = Label(boxFrame, text="123 Números",height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.grid(row=3, column=1,  sticky=NSEW, pady=5, padx=2)

digitsCheckIf = StringVar()
digitsCheckIf.set(False) 

digitsCheckBox = Checkbutton(boxFrame, width=1, var=digitsCheckIf,onvalue=digits, offvalue='off')
digitsCheckBox.grid(row=3, column=0,  sticky=NSEW, pady=5, padx=2)

#Simbols
appInfo = Label(boxFrame, text="!@# Símbolos", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), fg=blackColor)
appInfo.grid(row=4, column=1,  sticky=NSEW, pady=1, padx=2)

simbolsCheckIf = StringVar()
simbolsCheckIf.set(False)  

simbolsCheckBox = Checkbutton(boxFrame, width=1, var=simbolsCheckIf, onvalue=simbols, offvalue='off')
simbolsCheckBox.grid(row=4, column=0,  sticky=NSEW, pady=1, padx=2)

#Buttons
generatePasswordButton = Button(boxFrame,command=passwordGenerate ,text="Gerar senha",width=32, height=1, overrelief=SOLID,  bg=redColor, fg="white", font=('Ivy 10 bold'), anchor="center", relief=FLAT )
generatePasswordButton.grid(row=5, column=0,  sticky=NSEW, pady=20, padx=0, columnspan=5)

root.mainloop()