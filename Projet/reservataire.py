from tkinter import *
from PIL import Image,ImageTk #install pillow
from tkinter import ttk
#from salle import salleClass
import mysql.connector
from tkinter import ttk,messagebox


class reserverClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole - Reservataire')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # -------Variable-------
        self.var_Id_reserver = StringVar()
        self.var_role = StringVar()
        self.var_nom = StringVar()
        self.var_prenom = StringVar()
        self.var_email = StringVar()

        # --------title--------
        title = Label(self.root, text='Les Réservataire', font=('goudy old style', 20, 'bold'), bg='#52B4C7',fg='white').place(x=10, y=15, width=1180, height=35)
        # ------widgets------
        lbl_id_reservataire = Label(self.root, text='id reserv :', font=('goudy old style', 15, 'bold'),bg='white').place(x=10, y=120)
        lbl_role = Label(self.root, text='Role :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10,y=160)
        lbl_nom = Label(self.root, text='Nom :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10, y=200)
        lbl_Prénom = Label(self.root, text='Prénom :', font=('goudy old style', 15, 'bold'),bg='white').place(x=10, y=240)
        lbl_email = Label(self.root, text='email :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10,y=280)

        txt_id_reservataire = Entry(self.root, textvariable=self.var_Id_reserver,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=180, y=120)
        txt_role = Entry(self.root, textvariable=self.var_role, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=180, y=160)
        txt_nom = Entry(self.root, textvariable=self.var_nom, font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=180, y=200)
        txt_Prenom = Entry(self.root, textvariable=self.var_prenom,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=180, y=240)
        txt_email = Entry(self.root, textvariable=self.var_email, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=180, y=280)

        # -------Buttons----------
        self.btn_add = Button(self.root, text='Reset', font=('goudy old style', 15, 'bold'), bg='#185373', fg='white',cursor='hand2', command=self.clear)
        self.btn_add.place(x=30, y=400, width=110, height=40)

        self.btn_add = Button(self.root, text='Save', font=('goudy old style', 15, 'bold'), bg='#2196f3', fg='white',cursor='hand2',command=self.add)
        self.btn_add.place(x=160, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text='Update', font=('goudy old style', 15, 'bold'), bg='#4caf50',fg='white', cursor='hand2',command=self.update)
        self.btn_update.place(x=290, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text='Delete', font=('goudy old style', 15, 'bold'), bg='#f44336',fg='white', cursor='hand2',command=self.delete)
        self.btn_delete.place(x=420, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text='Clear', font=('goudy old style', 15, 'bold'), bg='#607d8b', fg='white', cursor='hand2',command=self.vider)
        self.btn_clear.place(x=550, y=400, width=110, height=40)

        # ----Search Panel----------
        self.var_search = StringVar()
        self.var_searchBy = StringVar()
        combo_search = ttk.Combobox(self.root, justify='right', font=('goudy old style', 12),
                                    textvariable=self.var_searchBy)
        combo_search['value'] = ('id_reservataire', 'nom', 'prenom', 'role', 'email')
        combo_search.place(x=660, y=60, width=130, height=31)
        combo_search.insert(0, 'choisissez')
        txt_search_equip = Entry(self.root, textvariable=self.var_search, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=800, y=60, width=180)
        self.bg_img = Image.open('icon.png')
        self.bg_img = self.bg_img.resize((20, 20), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.var_actualiser = StringVar()
        self.btn_search = Button(self.root, text='Refresh', font=('goudy old style', 17, 'bold'), bg='#19798C',
                                 image=self.bg_img, fg='white', cursor='hand2', command=self.show)
        self.btn_search.place(x=1140, y=60, width=40, height=32)
        self.btn_search = Button(self.root, text='Search', font=('goudy old style', 17, 'bold'), bg='#19798C',fg='white', cursor='hand2',command=self.search)
        self.btn_search.place(x=1000, y=60, width=130, height=31)

        # -----content------
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=720, y=100, width=470, height=340)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        #scrollx.config(command=self.equipementTable.xview)---------
        #scrolly.config(command=self.equipementTable.yview)---------
        self.reservataireTable = ttk.Treeview(self.C_Frame, columns=('ID reser', 'Role','Nom','Prenom','email'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        self.reservataireTable.heading('ID reser', text='id reservataire')
        self.reservataireTable.heading('Role', text='role')
        self.reservataireTable.heading('Nom', text='nom')
        self.reservataireTable.heading('Prenom', text='prenom')
        self.reservataireTable.heading('email', text='email')
        self.reservataireTable['show'] = 'headings'
        self.reservataireTable.column('ID reser',width=50)
        self.reservataireTable.column('Role',width=50)
        self.reservataireTable.column('Nom',width=50)
        self.reservataireTable.column('Prenom', width=50)
        self.reservataireTable.column('email', width=50)
        self.reservataireTable.bind("<ButtonRelease-1>",self.get_cursor)
        self.reservataireTable.pack(fill=BOTH, expand=1)
        self.show()
    def show(self):
        con = mysql.connector.connect(host='localhost', user='root', password='Ahsat0ut@', database='gestion_des_salles')
        cur=con.cursor()
        try :
            cur.execute("select * from reservataire")
            rows = cur.fetchall()
            self.reservataireTable.delete(*self.reservataireTable.get_children())
            for row in rows :
                self.reservataireTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def add(self):
        v1 = self.var_Id_reserver.get()
        v2 = self.var_role.get()
        v3 = self.var_nom.get()
        v4 = self.var_prenom.get()
        v5 = self.var_email.get()


        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ahsat0ut@",
                database="gestion_des_salles"

            )
        curser = con.cursor()
        sql = "INSERT INTO reservataire (id_reservataire,_role,nom,prenom,email) VALUES (%s,%s,%s,%s,%s)"
        val = (v1,v2,v3,v4,v5)
        curser.execute(sql, val)
        con.commit()
        print(curser.rowcount, "record inserted.")
        self.show()
        self.clear()

    def clear(self):
        self.var_Id_reserver.set('')
        self.var_nom.set('')
        self.var_prenom.set('')
        self.var_email.set('')
        self.var_role.set('')
    def search(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"

        )
        x = self.var_searchBy.get()
        y = self.var_search.get()
        curser = con.cursor()
        if x == "id_reservataire":
            sql = "SELECT * FROM reservataire WHERE id_reservataire = %s"
        elif x == "nom":
            sql = "SELECT * FROM reservataire WHERE nom like %s"
        elif x == "role" :
            sql = "SELECT * FROM reservataire WHERE _role like %s"
        elif x == "prenom":
            sql = "SELECT * FROM reservataire WHERE prenom like %s"
        elif x == "email" :
            sql = "SELECT * FROM reservataire WHERE email like %s"


        val = (y,)
        curser.execute(sql, val)
        rows=curser.fetchall()
        if len(rows) != 0 :
            self.reservataireTable.delete(*self.reservataireTable.get_children())
            for row in rows :
                self.reservataireTable.insert("", END, values=row)
            con.commit()
            con.close()

    def get_cursor(self, ev):
        cursor_row = self.reservataireTable.focus()
        contents = self.reservataireTable.item(cursor_row)
        row = contents['values']
        self.var_Id_reserver.set(row[0])
        self.var_nom.set(row[2])
        self.var_prenom.set(row[3])
        self.var_email.set(row[4])
        self.var_role.set(row[1])
    def update(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        v1 = self.var_Id_reserver.get()
        v2 = self.var_role.get()
        v3 = self.var_nom.get()
        v4 = self.var_prenom.get()
        v5 = self.var_email.get()
        curser = con.cursor()
        sql = "update reservataire set _role=%s,nom=%s,prenom=%s,email=%s where id_reservataire=%s"
        val = (v2,v3,v4,v5,v1)
        curser.execute(sql, val)
        con.commit()
        self.show()
        self.clear()
        con.close()
    def delete(self):
        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ahsat0ut@",
                database="gestion_des_salles"

            )
        cur = con.cursor()
        decis = messagebox.askquestion("Alert", "Surement vous voulez supprimer cette reservation ?")
        if decis != 'yes':
            return
        else:
            sql1 = "SET FOREIGN_KEY_CHECKS = 0"
            sql = "delete from reservataire where id_reservataire = %s"
            sql3 = "SET FOREIGN_KEY_CHECKS = 1"
            val = (self.var_Id_reserver.get(),)
            cur.execute(sql1)
            cur.execute(sql, val)
            cur.execute(sql3)
            con.commit()
            self.show()
            con.close()
    def vider(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        curser = con.cursor()
        decis = messagebox.askquestion("Alert","Surement vous voulez supprimer toutes les donnees ?")
        if decis != 'yes' :
            return
        else :
            sql1= "SET FOREIGN_KEY_CHECKS = 0"
            sql2= "DELETE FROM reservataire"
            sql3= "SET FOREIGN_KEY_CHECKS = 1"
            curser.execute(sql1)
            curser.execute(sql2)
            curser.execute(sql3)
            con.commit()
            self.show()
            con.close()
if __name__=="__main__":
    root=Tk()
    obj=reserverClass(root)
    root.mainloop()