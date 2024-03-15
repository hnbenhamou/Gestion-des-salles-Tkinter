from tkinter import *
from PIL import Image,ImageTk #install pillow
from tkinter import ttk
import mysql.connector
from tkinter import ttk,messagebox


class evenementClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole - Evenement')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # -------Variable-------
        self.var_N_evenement = StringVar()
        self.var_Code_Admin = StringVar()
        self.var_Nom_evenement = StringVar()
        self.var_date_evenement = StringVar()
        self.var_delete_evenement=StringVar()

        # --------title--------
        title = Label(self.root, text='Les évenements', font=('goudy old style', 20, 'bold'), bg='#52B4C7',fg='white').place(x=10, y=15, width=1180, height=35)
        # ------widgets------
        lbl_N_even = Label(self.root, text='N°evenement :', font=('goudy old style', 15, 'bold'),bg='white').place(x=10, y=120)
        lbl_code_admin = Label(self.root, text='Code admin :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10, y=160)
        lbl_Nom_evenment= Label(self.root, text='Nom d\'évenement :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10, y=200)
        lbl_date_evenement= Label(self.root, text='Date d\'évenement :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10,y=240)


        txt_N_even  = Entry(self.root, textvariable=self.var_N_evenement,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=200, y=120)
        txt_code_admin = Entry(self.root, textvariable=self.var_Code_Admin, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=200, y=160)
        txt_Nom_evenment= Entry(self.root, textvariable=self.var_Nom_evenement, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=200, y=200)
        txt_date_evenement= Entry(self.root, textvariable=self.var_date_evenement,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=200, y=240)

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
        combo_search['value'] = (
        'N°evenement','Nom' , 'Code Admin', 'Date et Heure')
        combo_search.place(x=660, y=60, width=130, height=31)
        combo_search.insert(0, 'choisissez')

        txt_search_equip = Entry(self.root, textvariable=self.var_search, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=800, y=60, width=180)
        self.bg_img = Image.open('icon.png')
        self.bg_img = self.bg_img.resize((20, 20), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.var_actualiser = StringVar()
        self.btn_search = Button(self.root, text='Refresh', font=('goudy old style', 17, 'bold'), bg='#19798C',
                                 image=self.bg_img, fg='white', cursor='hand2',command=self.show)
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
        # scrollx.config(command=self.equipementTable.xview)---------
        # scrolly.config(command=self.equipementTable.yview)---------
        self.evenementTable = ttk.Treeview(self.C_Frame,columns=('N°evenement', 'Code admin', 'nom evenement', 'date evenement'),yscrollcommand=scrolly.set)
        self.evenementTable.heading('N°evenement', text='N°evenement')
        self.evenementTable.heading('Code admin', text='Code admin')
        self.evenementTable.heading('nom evenement', text='nom d\'evenement')
        self.evenementTable.heading('date evenement', text='date d\'évenement')
        self.evenementTable['show'] = 'headings'
        self.evenementTable.column('N°evenement', width=50)
        self.evenementTable.column('Code admin', width=50)
        self.evenementTable.column('nom evenement', width=50)
        self.evenementTable.column('date evenement', width=50)
        self.evenementTable.bind("<ButtonRelease-1>", self.get_cursor)
        self.evenementTable.pack(fill=BOTH, expand=1)
        self.show()
    def show(self):
        con = mysql.connector.connect(host='localhost', user='root', password='Ahsat0ut@', database='gestion_des_salles')
        cur=con.cursor()
        try :
            cur.execute("select * from evenement")
            rows = cur.fetchall()
            self.evenementTable.delete(*self.evenementTable.get_children())
            for row in rows :
                self.evenementTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        con.close()
    def add(self):
        v1 =self.var_N_evenement.get()
        v2 = self.var_Code_Admin.get()
        v3=self.var_Nom_evenement.get()
        v4= self.var_date_evenement.get()
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"

        )
        curser = con.cursor()
        sql = "INSERT INTO evenement(N°evenement,code_admin,nom_d_evenement,date_d_evenements) VALUES (%s,%s,%s,%s)"
        val = (v1,v2,v3,v4)
        curser.execute(sql, val)
        con.commit()
        self.show()
        self.clear()
    def clear(self):
        self.var_Code_Admin.set('')
        self.var_Nom_evenement.set('')
        self.var_date_evenement.set('')
        self.var_N_evenement.set('')
    def delete(self):
        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ahsat0ut@",
                database="gestion_des_salles"

            )
        cur = con.cursor()
        decis = messagebox.askquestion("Alert", "Surement vous voulez supprimer cet evenement ?")
        if decis != 'yes':
            return
        else:
            sql1 = "SET FOREIGN_KEY_CHECKS = 0"
            sql = "delete from evenement where N°evenement like %s"
            sql3 = "SET FOREIGN_KEY_CHECKS = 1"
            val = (self.var_N_evenement.get(),)
            cur.execute(sql1)
            cur.execute(sql, val)
            cur.execute(sql3)
            con.commit()
            self.show()
            con.close()
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
        if x == "N°evenement":
            sql = "SELECT * FROM evenement WHERE N°evenement = %s"
        elif x == "Code Admin":
            sql = "SELECT * FROM evenement WHERE code_admin = %s"
        elif x == "Nom":
            sql = "SELECT * FROM evenement WHERE nom_d_evenement = %s"
        elif x == "Date et Heure":
            sql = "SELECT * FROM evenement WHERE date_d_evenements = %s"


        val = (y,)
        curser.execute(sql, val)
        rows=curser.fetchall()
        if len(rows) == 0:
            messagebox.showerror("Error", "Desole , Il n'existe pas")
        if len(rows) != 0 :
            self.evenementTable.delete(*self.evenementTable.get_children())
            for row in rows :
                self.evenementTable.insert("", END, values=row)
            con.commit()
            con.close()


    def get_cursor(self, ev):
        cursor_row = self.evenementTable.focus()
        contents = self.evenementTable.item(cursor_row)
        row = contents['values']
        self.var_Code_Admin.set(row[1])
        self.var_Nom_evenement.set(row[2])
        self.var_date_evenement.set(row[3])
        self.var_N_evenement.set(row[0])

    def update(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        v1 =self.var_N_evenement.get()
        v2 = self.var_Code_Admin.get()
        v3=self.var_Nom_evenement.get()
        v4= self.var_date_evenement.get()
        curser = con.cursor()
        sql = "update evenement set code_admin=%s, nom_d_evenement=%s, date_d_evenements=%s where N°evenement=%s"
        val = (v2,v3,v4,v1)
        curser.execute(sql, val)
        con.commit()
        self.show()
        self.clear()
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
            sql2= "DELETE FROM evenement"
            sql3= "SET FOREIGN_KEY_CHECKS = 1"
            curser.execute(sql1)
            curser.execute(sql2)
            curser.execute(sql3)
            con.commit()
            self.show()
            con.close()

if __name__=="__main__":
    root=Tk()
    obj=evenementClass(root)
    root.mainloop()