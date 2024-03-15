from tkinter import *
from PIL import Image,ImageTk #install pillow
from tkinter import ttk,messagebox
#from salle import salleClass
import mysql.connector




class equipementClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole - Equipement')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # -------Variable-------
        self.var_Code_equipement = StringVar()
        self.var_n_salle = StringVar()
        self.var_typr_equip = StringVar()
        self.var_quantite_equip = StringVar()

        # --------title--------
        title = Label(self.root, text='Les équipements', font=('goudy old style', 20, 'bold'), bg='#52B4C7', fg='white').place(x=10, y=15, width=1180, height=35)
        # ------widgets------
        lbl_code_equipement = Label(self.root, text='Code équip :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10, y=120)
        lbl_n_salle = Label(self.root, text='N°salle :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10,y=160)
        lbl_type_equip = Label(self.root, text='Type équip :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10,y=200)
        lbl_quantite_equip = Label(self.root, text='Quantité :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10,y=240)

        txt_code_equipement = Entry(self.root,textvariable=self.var_Code_equipement,font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=200, y=120)
        txt_n_salle = Entry(self.root,textvariable=self.var_n_salle,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=200,y=160)
        txt_type_equip = Entry(self.root,textvariable=self.var_typr_equip,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=200, y=200)
        txt_quantite_equip = Entry(self.root,textvariable=self.var_quantite_equip,font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=200, y=240)

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
        combo_search['value'] = ('code_equipement', 'N°salle','type_equipm','quantite_equipm')
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
        self.equipementTable = ttk.Treeview(self.C_Frame, columns=('Code equipement', 'N°salle','Type equipm','quantité_equipm'), yscrollcommand=scrolly.set)
        self.equipementTable.heading('Code equipement', text='Code equipement')
        self.equipementTable.heading('N°salle', text='N°salle')
        self.equipementTable.heading('Type equipm', text='Type equipm')
        self.equipementTable.heading('quantité_equipm', text='quantité_équipm')
        self.equipementTable['show'] = 'headings'
        self.equipementTable.column('Code equipement',width=50)
        self.equipementTable.column('N°salle',width=50)
        self.equipementTable.column('Type equipm',width=50)
        self.equipementTable.column('quantité_equipm',width=50)
        self.equipementTable.bind("<ButtonRelease-1>", self.get_cursor)
        self.equipementTable.pack(fill=BOTH, expand=1)
        self.show()
    def show(self):
        con = mysql.connector.connect(host='localhost', user='root', password='Ahsat0ut@', database='gestion_des_salles')
        cur = con.cursor()
        try:
            cur.execute("select * from equipements")
            rows = cur.fetchall()
            self.equipementTable.delete(*self.equipementTable.get_children())
            for row in rows:
                self.equipementTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")
    def add(self):
        v1 =self.var_Code_equipement.get()
        v2 = self.var_n_salle.get()
        v3=self.var_typr_equip.get()
        v4= self.var_quantite_equip.get()
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"

        )
        curser = con.cursor()
        sql = "INSERT INTO equipements(code_equipement,N°salle,type_equipm,quantite_equipm) VALUES (%s,%s,%s,%s)"
        val = (v1,v2,v3,v4)
        curser.execute(sql, val)
        con.commit()
        self.show()
        self.clear()
    def clear(self):
        self.var_Code_equipement.set('')
        self.var_n_salle.set('')
        self.var_typr_equip.set('')
        self.var_quantite_equip.set('')
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
        if x == "code_equipement":
            sql = "SELECT * FROM equipements WHERE code_equipement = %s"
        elif x == "N°salle" :
            sql = "SELECT * FROM equipements WHERE N°salle = %s"
        elif x == "type_equipm" :
            sql = "SELECT * FROM equipements WHERE type_equipm = %s"
        elif x == "quantite_equipm" :
            sql = "SELECT * FROM equipements WHERE quantite_equipm = %s"


        val = (y,)
        curser.execute(sql,val)
        rows = curser.fetchall()
        if len(rows) == 0:
            messagebox.showerror("Error", "Ta makinsh hadshy")
        if len(rows) != 0 :
            self.equipementTable.delete(*self.equipementTable.get_children())
            for row in rows :
                self.equipementTable.insert("", END, values=row)
            con.commit()
            con.close()

    def get_cursor(self, ev):
        cursor_row = self.equipementTable.focus()
        contents = self.equipementTable.item(cursor_row)
        row = contents['values']
        self.var_Code_equipement.set(row[0])
        self.var_n_salle.set(row[1])
        self.var_typr_equip.set(row[2])
        self.var_quantite_equip.set(row[3])
    def update(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        v1 = self.var_Code_equipement.get()
        v2 = self.var_n_salle.get()
        v3 = self.var_typr_equip.get()
        v4 = self.var_quantite_equip.get()
        curser = con.cursor()
        sql = "update equipements set N°salle=%s , type_equipm=%s,quantite_equipm=%s where code_equipement=%s"
        val = (v2,v3,v4,v1)
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
        decis = messagebox.askquestion("Alert", "Surement vous voulez supprimer cette donnée ?")
        if decis != 'yes':
            return
        else:
            sql1 = "SET FOREIGN_KEY_CHECKS = 0"
            sql = "delete from equipements where code_equipement = %s"
            sql3 = "SET FOREIGN_KEY_CHECKS = 1"
            val = (self.var_Code_equipement.get(),)
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
            sql2= "DELETE FROM equipements"
            sql3= "SET FOREIGN_KEY_CHECKS = 1"
            curser.execute(sql1)
            curser.execute(sql2)
            curser.execute(sql3)
            con.commit()
            self.show()
            con.close()
if __name__=="__main__":
    root=Tk()
    obj=equipementClass(root)
    root.mainloop()