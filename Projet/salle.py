from tkinter import *
from PIL import Image,ImageTk #install pillow
from tkinter import ttk
from tkinter import ttk,messagebox
from Bloc import BlocClass
import mysql.connector


class salleClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole - Salle ')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # -------Variable-------
        self.var_N_salle = StringVar()
        self.var_capacite = StringVar()
        self.var_N_bloc = StringVar()

        # --------title--------
        title = Label(self.root, text='Salle', font=('goudy old style', 20, 'bold'), bg='#52B4C7', fg='white').place(x=10, y=15, width=1180, height=35)

        # ------widgets------
        lbl_Numero_salle = Label(self.root, text='N°Salle :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10, y=120)
        lbl_bloc = Label(self.root, text='N°bloc :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10,y=160)
        lbl_capacie = Label(self.root, text='Capacité :', font=('goudy old style', 17, 'bold'), bg='white').place(x=10,y=200)

        self.txt_Numero_salle = Entry(self.root, textvariable=self.var_N_salle, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=150, y=120)
        self.txt_N_bloc = Entry(self.root, textvariable=self.var_N_bloc, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=150, y=160)
        self.txt_capacite = Entry(self.root, textvariable=self.var_capacite, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=150, y=200)

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
        combo_search['value'] = ('N°salle', 'N°bloc', 'capacite')
        combo_search.place(x=660, y=60, width=130, height=31)
        combo_search.insert(0, 'choisissez')
        txt_search_salle = Entry(self.root, textvariable=self.var_search, font=('goudy old style', 17, 'bold'),bg='lightyellow').place(x=800, y=60, width=180)
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
        self.salleTable = ttk.Treeview(self.C_Frame, columns=('N°salle', 'N°bloc', 'capacite'),
                                       yscrollcommand=scrolly.set)
        self.salleTable.heading('N°salle', text='N°salle')
        self.salleTable.heading('N°bloc', text='N°bloc')
        self.salleTable.heading('capacite', text='Capacite')
        self.salleTable['show'] = 'headings'
        self.salleTable.column('N°salle', width=50)
        self.salleTable.column('N°bloc', width=50)
        self.salleTable.column('capacite', width=50)
        self.salleTable.bind("<ButtonRelease-1>", self.get_cursor)
        self.salleTable.pack(fill=BOTH, expand=1)
        self.show()

    def show(self):
        con = mysql.connector.connect(host='localhost', user='root', password='Ahsat0ut@', database='gestion_des_salles')
        cur=con.cursor()
        try :
            cur.execute("select * from salle")
            rows = cur.fetchall()
            self.salleTable.delete(*self.salleTable.get_children())
            for row in rows :
                self.salleTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    def add(self):
        Nsalle = self.var_N_salle.get()
        capacite = self.var_capacite.get()
        nbloc = self.var_N_bloc.get()
        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ahsat0ut@",
                database="gestion_des_salles"

            )
        curser = con.cursor()
        sql = "INSERT INTO salle (N°salle,N°bloc,capacite) VALUES (%s,%s,%s)"
        val = (Nsalle,nbloc,capacite)
        curser.execute(sql, val)
        con.commit()
        print(curser.rowcount, "record inserted.")
        self.show()
        self.clear()
    def clear(self):
        self.var_N_salle.set('')
        self.var_capacite.set('')
        self.var_N_bloc.set('')
    def search(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"

        )
        curser = con.cursor()
        curser.execute("select * from salle where " +
        str(self.var_searchBy.get())+" LIKE "+str(self.var_search.get()))
        rows=curser.fetchall()
        if len(rows) == 0 :
            messagebox.showerror("Error","Ta makinsh hadshy")
        if len(rows) != 0 :
            self.salleTable.delete(*self.salleTable.get_children())
            for row in rows :
                self.salleTable.insert("", END, values=row)
            con.commit()
            con.close()
    def get_cursor(self, ev):
        cursor_row = self.salleTable.focus()
        contents = self.salleTable.item(cursor_row)
        row = contents['values']
        self.var_N_salle.set(row[0])
        self.var_N_bloc.set(row[1])
        self.var_capacite.set(row[2])

    def update(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        Nsalle = self.var_N_salle.get()
        capacite = self.var_capacite.get()
        nbloc = self.var_N_bloc.get()
        curser = con.cursor()
        sql = "update salle set N°bloc=%s , capacite=%s where N°salle=%s"
        val = (nbloc,capacite,Nsalle)
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
            sql = "delete from salle where N°salle = %s"
            sql3 = "SET FOREIGN_KEY_CHECKS = 1"
            val = (self.var_N_salle.get(),)
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
            sql2= "DELETE FROM salle"
            sql3= "SET FOREIGN_KEY_CHECKS = 1"
            curser.execute(sql1)
            curser.execute(sql2)
            curser.execute(sql3)
            con.commit()
            self.show()
            con.close()


if __name__=="__main__":
    root=Tk()
    obj=salleClass(root)
    root.mainloop()

