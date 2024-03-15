from tkinter import *
from PIL import Image,ImageTk #install pillow
from tkinter import ttk,messagebox
import sqlite3
import mysql.connector
class BlocClass:
    def __init__(self,root):
        self.root=root
        self.root.title('Systeme De Management Des Salles D\'une Ecole ')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()
        # --------title--------
        title = Label(self.root, text='Bloc',font=('goudy old style', 20, 'bold'), bg='#52B4C7', fg='white').place(x=10, y=15,width=1180, height=35)


        #-------Variable-------
        self.var_N_bloc=StringVar()


        #------widgets------
        lbl_Numero_bloc=Label(self.root,text='N°Bloc :',font=('goudy old style',17,'bold'),bg='white').place(x=10,y=120)


        #------------Entry-------
        self.txt_Numero_bloc=Entry(self.root,textvariable=self.var_N_bloc,font=('goudy old style', 17, 'bold'), bg='lightyellow').place(x=110,y=120)

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


        #----Search Panel----------
        self.var_search=StringVar()
        lbl_search_bloc = Label(self.root, text='N°Bloc :', font=('goudy old style', 17, 'bold'), bg='white').place(x=720,y=60)
        txt_search_bloc = Entry(self.root,textvariable=self.var_search,font=('goudy old style', 17,'bold'),bg='lightyellow').place(x=800,y=60,width=180)
        self.bg_img = Image.open('icon.png')
        self.bg_img = self.bg_img.resize((20, 20), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.var_actualiser = StringVar()
        self.btn_search = Button(self.root, text='Refresh', font=('goudy old style', 17, 'bold'), bg='#19798C',
                                 image=self.bg_img, fg='white', cursor='hand2', command=self.show)
        self.btn_search.place(x=1140, y=60, width=40, height=32)
        self.btn_search = Button(self.root, text='Search', font=('goudy old style', 17, 'bold'), bg='#19798C', fg='white',cursor='hand2',command=self.search)
        self.btn_search.place(x=1000, y=60, width=130, height=31)

        #-----content------
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        self.blocTable=ttk.Treeview(self.C_Frame,columns=('N°bloc'),yscrollcommand=scrolly.set)
        self.blocTable.heading('N°bloc',text=('N°bloc'))
        self.blocTable.pack(fill=BOTH,expand=1)
        self.blocTable['show']='headings'
        self.blocTable.column('N°bloc',width=50)
        self.blocTable.bind("<ButtonRelease-1>", self.get_data)
        self.blocTable.bind("<ButtonRelease-1>", self.get_cursor)
        self.show()
    #=======================
    def get_data(self,ev):
        r=self.blocTable.focus()
        content=self.blocTable.item(r)
        row=content["values"]
        self.var_N_bloc.set(row[1])


    def add(self):
        nbloc = self.var_N_bloc.get()

        con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ahsat0ut@",
                database="gestion_des_salles"

            )
        curser = con.cursor()
        sql = "INSERT INTO bloc(N°bloc) VALUES (%s)"
        val = (nbloc,)
        curser.execute(sql, val)
        con.commit()
        print(curser.rowcount, "record inserted.")
        self.show()
        self.clear()




    def show(self):
        con = mysql.connector.connect(host='localhost', user='root', password='Ahsat0ut@', database='gestion_des_salles')
        cur=con.cursor()
        try :
            cur.execute("select * from bloc")
            rows = cur.fetchall()
            self.blocTable.delete(*self.blocTable.get_children())
            for row in rows :
                self.blocTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def clear(self):
        self.var_N_bloc.set('')
    def search(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"

        )
        curser = con.cursor()
        sql = "select * from bloc where N°bloc = %s"
        val = (self.var_search.get(),)
        curser.execute(sql,val)
        rows=curser.fetchall()
        if len(rows) != 0 :
            self.blocTable.delete(*self.blocTable.get_children())
            for row in rows :
                self.blocTable.insert("", END, values=row)
            con.commit()
            con.close()
    def get_cursor(self, ev):
        cursor_row = self.blocTable.focus()
        contents = self.blocTable.item(cursor_row)
        row = contents['values']
        self.var_N_bloc.set(row[0])
    def update(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ahsat0ut@",
            database="gestion_des_salles"
        )
        nbloc = self.var_N_bloc.get()
        curser = con.cursor()
        sql = "update salle set N°bloc=%s"
        val = (nbloc,)
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
        decis = messagebox.askquestion("Alert", "Surement vous voulez supprimer ce bloc ?")
        if decis != 'yes':
            return
        else:
            sql1 = "SET FOREIGN_KEY_CHECKS = 0"
            sql = "delete from bloc where N°bloc = %s"
            sql3 = "SET FOREIGN_KEY_CHECKS = 1"
            val = (self.var_N_bloc.get(),)
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
    obj=BlocClass(root)
    root.mainloop()