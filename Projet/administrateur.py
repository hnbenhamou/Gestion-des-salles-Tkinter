from tkinter import *
from PIL import Image,ImageTk #install pillow
from tkinter import ttk,messagebox
#from salle import salleClass
import mysql.connector



class adminClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole - Administrateur')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # -------Variable-------
        self.var_CodeAdmin = StringVar()
        self.var_nom = StringVar()
        self.var_prenom = StringVar()
        # --------title--------
        title = Label(self.root, text='Administrateur', font=('goudy old style', 20, 'bold'), bg='#52B4C7',fg='white').place(x=10, y=15, width=1180, height=35)

        # ------widgets------
        lbl_code_admin = Label(self.root, text='Code admin :', font=('goudy old style', 17, 'bold'),bg='white').place(x=10, y=120)
        lbl_nom = Label(self.root, text='Nom :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10,y=160)
        lbl_prenom = Label(self.root, text='Prénom :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10, y=200)

        txt_code_admin = Entry(self.root, textvariable=self.var_CodeAdmin,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=200, y=120)
        txt_nom = Entry(self.root, textvariable=self.var_nom, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=200, y=160)
        txt_prenom = Entry(self.root, textvariable=self.var_prenom, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=200, y=200)

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
        combo_search['value'] = ('code_admin', 'nom', 'prenom')
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
        self.adminTable = ttk.Treeview(self.C_Frame, columns=('Code Admin', 'Nom','Prenom'), yscrollcommand=scrolly.set)
        self.adminTable.heading('Code Admin', text='Code Admin')
        self.adminTable.heading('Nom', text='Nom')
        self.adminTable.heading('Prenom', text='Prenom')
        self.adminTable['show'] = 'headings'
        self.adminTable.column('Code Admin',width=50)
        self.adminTable.column('Nom',width=50)
        self.adminTable.column('Prenom',width=50)
        self.adminTable.bind("<ButtonRelease-1>", self.get_cursor)
        self.adminTable.pack(fill=BOTH, expand=1)
        self.show()

    def show(self):
        con = mysql.connector.connect(host='localhost', user='root', password='Ahsat0ut@', database='gestion_des_salles')
        cur = con.cursor()
        try:
            cur.execute("select * from administrateur")
            rows = cur.fetchall()
            self.adminTable.delete(*self.adminTable.get_children())
            for row in rows:
                self.adminTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
        con.close()
    def add(self):
        code_admin = self.var_CodeAdmin.get()
        nom = self.var_nom.get()
        prenom = self.var_prenom.get()

        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ahsat0ut@",
                database="gestion_des_salles"

            )
        curser = con.cursor()
        sql = "INSERT INTO administrateur (code_admin,nom,prenom) VALUES (%s,%s,%s)"
        val = (code_admin,nom,prenom)
        curser.execute(sql, val)
        con.commit()
        print(curser.rowcount, "record inserted.")
        self.show()
        self.clear()

    def clear(self):
        self.var_CodeAdmin.set('')
        self.var_nom.set('')
        self.var_prenom.set('')
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
        if x == "code_admin":
            sql = "SELECT * FROM administrateur WHERE code_admin = %s"
        elif x == "nom":
            sql = "SELECT * FROM administrateur WHERE nom = %s"
        elif x == "prenom":
            sql = "SELECT * FROM administrateur WHERE prenom = %s"


        val = (y,)
        curser.execute(sql, val)
        rows=curser.fetchall()
        if len(rows) != 0 :
            self.adminTable.delete(*self.adminTable.get_children())
            for row in rows :
                self.adminTable.insert("", END, values=row)
            con.commit()
            con.close()

    def get_cursor(self, ev):
        cursor_row = self.adminTable.focus()
        contents = self.adminTable.item(cursor_row)
        row = contents['values']
        self.var_CodeAdmin.set(row[0])
        self.var_nom.set(row[1])
        self.var_prenom.set(row[2])
    def update(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        code_admin = self.var_CodeAdmin.get()
        nom = self.var_nom.get()
        prenom = self.var_prenom.get()
        curser = con.cursor()
        sql = "update administrateur set nom=%s , prenom=%s where code_admin=%s"
        val = (nom,prenom,code_admin)
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
        decis = messagebox.askquestion("Alert", "Surement vous voulez supprimer cet admin ?")
        if decis != 'yes':
            return
        else:
            sql1 = "SET FOREIGN_KEY_CHECKS = 0"
            sql = "delete from administrateur where code_admin = %s"
            sql3 = "SET FOREIGN_KEY_CHECKS = 1"
            val = (self.var_CodeAdmin.get(),)
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
            sql2= "DELETE FROM administrateur"
            sql3= "SET FOREIGN_KEY_CHECKS = 1"
            curser.execute(sql1)
            curser.execute(sql2)
            curser.execute(sql3)
            con.commit()
            self.show()
            con.close()

if __name__=="__main__" :
    root=Tk()
    obj=adminClass(root)
    root.mainloop()