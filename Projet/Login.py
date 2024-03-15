from tkinter import *
from tkinter import messagebox
from subprocess import call

def interface() :
    root.destroy()
    call(["python", "main.py"])
def signin() :
    username = user.get()
    password = code.get()
    if username.lower() =='admin'  and password=="hassan" :
        interface()
    # new_window()
    else:
        messagebox.showerror('Error', 'Invalid username or password')
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.resizable(False,False)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Se connecter",fg='#57a1f8',bg='white',font=("Microsoft YaHei UI Light",23,'bold'))
heading.place(x=100,y=5)

########################
def on_enter(e):
    user.delete (0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0, 'Username')
user = Entry (frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

######################
def on_enter(e):
    code.delete (0, 'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0, 'Password')
code = Entry(frame,width=25,fg='black',show="*",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)


######################

Button(frame,width=39,pady=7,text="Connexion",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)









root.mainloop()