from tkinter import *
from PIL import Image,ImageTk #install pillow
from tkinter import ttk
import mysql.connector
from tkinter import ttk,messagebox




class reservationClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole - Reservation ')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()

        # -------Variable-------
        self.var_code_reservation = StringVar()
        self.var_n_salle = StringVar()
        self.var_id_reservataire = StringVar()
        self.var_code_admin = StringVar()
        self.var_nbr_hr_utilis = StringVar()
        self.var_date_heure_reserv = StringVar()


        # --------title--------
        title = Label(self.root, text='Les Réservations', font=('goudy old style', 20, 'bold'), bg='#52B4C7',fg='white').place(x=10, y=15, width=1180, height=35)

        # ------widgets------
        lbl_code_reservation = Label(self.root, text='Code Réservation :', font=('goudy old style', 15, 'bold'),bg='white').place(x=10, y=80)
        lbl_n_salle = Label(self.root, text='N°salle :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10,y=120)
        lbl_id_reservataire = Label(self.root, text='id reserv :', font=('goudy old style', 15, 'bold'), bg='white').place(x=10, y=160)
        lbl_code_admin = Label(self.root, text='Code admin :', font=('goudy old style', 15, 'bold'),bg='white').place(x=10, y=200)
        lbl_nbr_hr_utilis = Label(self.root, text='nbr hr d\'utilisation :', font=('goudy old style', 15, 'bold'),bg='white').place(x=10, y=240)

        lbl_date_heure_reserv = Label(self.root, text='La Date et l\'Heure :', font=('goudy old style', 15, 'bold'),bg='white').place(x=10, y=280)

        txt_code_reservation = Entry(self.root,textvariable=self.var_code_reservation,font=('goudy old style', 15, 'bold'),bg='lightyellow').place(x=200, y=80)
        txt_n_salle = Entry(self.root,textvariable=self.var_n_salle, font=('goudy old style', 15, 'bold'), bg='lightyellow').place(x=200,y=120)
        txt_id_reservataire = Entry(self.root,textvariable=self.var_id_reservataire, font=('goudy old style', 15, 'bold'),bg='lightyellow').place(x=200, y=160)
        txt_code_admin = Entry(self.root,textvariable=self.var_code_admin , font=('goudy old style', 15, 'bold'), bg='lightyellow').place( x=200, y=200)
        txt_nbr_hr_utilis = Entry(self.root,textvariable=self.var_nbr_hr_utilis, font=('goudy old style', 15, 'bold'),bg='lightyellow').place(x=200, y=240)
        txt_date_heure_reserv = Entry(self.root,textvariable=self.var_date_heure_reserv, font=('goudy old style', 15, 'bold'), bg='lightyellow').place(x=200, y=280)

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
        combo_search['value'] = ('code_reservation','N°salle','id_reservataire','code_admin','date_et_heure_de_reservation')
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
        scrollx = Scrollbar(self.C_Frame,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM, fill=X)
        #scrollx.config(command=self.reservationTable.xview)
        #scrolly.config(command=self.equipementTable.yview)---------
        self.reservationTable = ttk.Treeview(self.C_Frame,
                            columns=('Code Réservation', 'N°salle', 'id reserv', 'Code admin','nbr hr d\'utilisation','La Date et l\'Heure'),
                            yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.reservationTable.heading('Code Réservation', text='Code Réservation')
        self.reservationTable.heading('N°salle', text='N°salle')
        self.reservationTable.heading('id reserv', text='id reserv')
        self.reservationTable.heading('Code admin', text='Code admin')
        self.reservationTable.heading('nbr hr d\'utilisation', text='nbr hr d\'utilisation')
        self.reservationTable.heading('La Date et l\'Heure', text='La Date et l\'Heure')
        self.reservationTable['show'] = 'headings'
        self.reservationTable.column('Code Réservation', width=30)
        self.reservationTable.column('N°salle', width=30)
        self.reservationTable.column('id reserv', width=30)
        self.reservationTable.column('Code admin', width=30)
        self.reservationTable.column('nbr hr d\'utilisation', width=30)
        self.reservationTable.column('La Date et l\'Heure', width=30)
        self.reservationTable.bind("<ButtonRelease-1>", self.get_cursor)
        self.reservationTable.pack(fill=BOTH, expand=1)
        self.show()
    def show(self):
        con = mysql.connector.connect(host='localhost', user='root', password='Ahsat0ut@', database='gestion_des_salles')
        cur = con.cursor()
        try:
            cur.execute("select * from reservation")
            rows = cur.fetchall()
            self.reservationTable.delete(*self.reservationTable.get_children())
            for row in rows:
                self.reservationTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")


    def add(self):
        v1 =self.var_code_reservation.get()
        v2 =self.var_n_salle.get()
        v3 =self.var_id_reservataire.get()
        v4 =self.var_code_admin.get()
        v5 =self.var_nbr_hr_utilis.get()
        v6 =self.var_date_heure_reserv.get()
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"

        )
        curser = con.cursor()
        sql = "INSERT INTO reservation(code_reservation,N°salle,id_reservataire,code_admin,nombre_d_heure_d_utilisation,date_et_heure_de_reservation) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (v1,v2,v3,v4,v5,v6)
        curser.execute(sql, val)
        con.commit()
        self.show()
        messagebox.showinfo("Succes", "vous avez bien reservé")
        self.clear()
    def clear(self):
        self.var_code_reservation.set('')
        self.var_n_salle.set('')
        self.var_nbr_hr_utilis.set('')
        self.var_code_admin.set('')
        self.var_id_reservataire.set('')
        self.var_date_heure_reserv.set('')
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
        if x == "code_reservation":
            sql = "SELECT * FROM reservation WHERE code_reservation = %s"
        elif x == "id_reservataire" :
            sql = "SELECT * FROM reservation WHERE id_reservataire = %s"
        elif x == "code_admin" :
            sql = "SELECT * FROM reservation WHERE code_admin = %s"
        elif x == "N°salle" :
            sql = "SELECT * FROM reservation WHERE N°salle = %s"
        else :
            sql = "SELECT * FROM reservation WHERE date_et_heure_de_reservation = %s"


        val = (y,)
        curser.execute(sql,val)
        rows = curser.fetchall()
        if len(rows) == 0:
            messagebox.showerror("Error", "Il n'existe pas")
        if len(rows) != 0 :
            self.reservationTable.delete(*self.reservationTable.get_children())
            for row in rows :
                self.reservationTable.insert("", END, values=row)
            con.commit()
            con.close()
    def get_cursor(self, ev):
        cursor_row = self.reservationTable.focus()
        contents = self.reservationTable.item(cursor_row)
        row = contents['values']
        self.var_code_reservation.set(row[0])
        self.var_n_salle.set(row[1])
        self.var_id_reservataire.set(row[2])
        self.var_code_admin.set(row[3])
        self.var_nbr_hr_utilis.set(row[4])
        self.var_date_heure_reserv.set(row[5])
    def update(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        v1 = self.var_code_reservation.get()
        v2 = self.var_n_salle.get()
        v3 = self.var_id_reservataire.get()
        v4 = self.var_code_admin.get()
        v5 = self.var_nbr_hr_utilis.get()
        v6 = self.var_date_heure_reserv.get()
        curser = con.cursor()
        sql = "update reservation set N°salle=%s,id_reservataire=%s,code_admin=%s,nombre_d_heure_d_utilisation=%s,date_et_heure_de_reservation=%s where code_reservation=%s"
        val = (v2,v3,v4,v5,v6,v1)
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
            sql = "delete from reservation where code_reservation = %s"
            sql3 = "SET FOREIGN_KEY_CHECKS = 1"
            val = (self.var_code_reservation.get(),)
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
            sql2= "DELETE FROM reservation"
            sql3= "SET FOREIGN_KEY_CHECKS = 1"
            curser.execute(sql1)
            curser.execute(sql2)
            curser.execute(sql3)
            con.commit()
            self.show()
            con.close()

if __name__=="__main__":
    root=Tk()
    obj=reservationClass(root)
    root.mainloop()