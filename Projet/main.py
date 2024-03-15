from tkinter import *
from PIL import Image,ImageTk #install pillow
from Bloc import BlocClass
from salle import salleClass
from equipement import equipementClass
from administrateur import adminClass
from reservataire import reserverClass
from evenement import evenementClass
from reservation import reservationClass


class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole ')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')
        #--------icons-------



        #--------title--------
        title=Label(self.root,text='Systeme De Management Des Salles D\'une Ecole',font=('goudy old style',20,'bold'),bg='#52B4C7',fg='white').place(x=0,y=0,relwidth=1,height=50)
        #-------MENU---------
        M_Frame=LabelFrame(self.root,text='Menus',font=('times new roman',15),bg='white')
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_Bloc=Button(M_Frame,text='Blocs',font=('goudy old style',15,'bold'),bg="#52B4C7",fg='white',cursor='hand2',command=self.add_blocs).place(x=23,y=5,width=174,height=40)
        btn_Salle = Button(M_Frame, text='Salles', font=('goudy old style', 15, 'bold'), bg="#52B4C7", fg='white',cursor='hand2',command=self.add_salle).place(x=207, y=5, width=  174, height=40)
        btn_Administrateur = Button(M_Frame, text='Administrateur', font=('goudy old style', 15, 'bold'), bg="#52B4C7", fg='white',cursor='hand2',command=self.add_admin).place(x=391, y=5, width=174, height=40)
        btn_Reservataire = Button(M_Frame, text='Reservataire', font=('goudy old style', 15, 'bold'), bg="#52B4C7", fg='white',cursor='hand2',command=self.add_reservataire).place(x=576, y=5, width=174, height=40)
        btn_Reservation = Button(M_Frame, text='Reservation', font=('goudy old style', 15, 'bold'), bg="#52B4C7", fg='white',cursor='hand2',command=self.add_reservation).place(x=761,y=5, width=174, height=40)
        btn_Equipements = Button(M_Frame, text='Equipements', font=('goudy old style', 15, 'bold'), bg="#52B4C7",fg='white', cursor='hand2',command=self.add_equipement).place(x=946, y=5, width=174, height=40)
        btn_Evenements = Button(M_Frame, text='Evenements', font=('goudy old style', 15, 'bold'), bg="#52B4C7", fg='white',cursor='hand2',command=self.add_event).place(x=1132, y=5, width=174, height=40)

        #------content_window----
        self.bg_img=Image.open('gestion.png')
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=170,y=240,width=920,height=350)





        # --------footer--------
        footer = Label(self.root, text='Systeme De Management Des Salles D\'une Ecole :\nContact Us for any Technical Issue : 0649533692/0711191884',font=('goudy old style',12), bg='#225661', fg='white').pack(side=BOTTOM,fill=X)

    def add_blocs(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BlocClass(self.new_win)

    def add_salle(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salleClass(self.new_win)

    def add_equipement(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=equipementClass(self.new_win)

    def add_admin(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=adminClass(self.new_win)

    def add_reservataire(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reserverClass(self.new_win)

    def add_event(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=evenementClass(self.new_win)

    def add_reservation(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reservationClass(self.new_win)


if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()