from tkinter import *
from msilib.schema import ComboBox
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

import sqlite3
                                                                                                                                        

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.title('Prison Database')
        self.config(bg='gray26')

        self.iconbitmap('kk.ico')
        self.config(bg='#090A2E')
        self.resizable(False,False)
        fr2=Frame(self,width='495',height='499',bg='#0C1630')
        fr2.place(x=303,y=15)
        
        load = Image.open('pv.png')
        render = ImageTk.PhotoImage(load)
        img = Label(fr2, image=render,bg='#0C1630')
        img.image = render
        img.place(width=380,height=300)




        lbl44=Label(fr2,text='IUSR| Faculty of Informatics Engineering',fg='white',bg='#0C1630',font=('Bookman Old Style',7))
        lbl44.place(x=90,y=240)
        lbl_title=Label(self,text=' PRISON MANAGMENT SYSTEM ',fg='white',bg='black'
        ,font=('times new roman',20,'bold'))
        lbl_title.place(x=0,y=0,width=700,height=40)
        lbl_meun=Label(self,text=' MENU OF TABLES ',fg='white',bg='black'
        ,font=('times new roman',15,'bold'))
        lbl_meun.place(x=20,y=45,width=265,height=40)
        offense_btn=Button(self,text='Offense',font=('Courier',9),command=lambda :offense(),border=3,fg='white',bg='black',cursor='target',width='15'
        ,activebackground='white',activeforeground='black',padx=5,pady=5)
        offense_btn.place(x=20,y=100)

        convicts_btn=Button(self,text='Convicts',font=('Courier',9),command=lambda :convicts(),border=3,fg='white',bg='black',cursor='target',width='15'
        ,activebackground='white',activeforeground='black',padx=5,pady=5)
        convicts_btn.place(x=20,y=150)

        person_btn=Button(self,text='Person',font=('Courier',9),command=lambda:person(),border=3,fg='white',bg='black',cursor='target',width='15'
        ,activebackground='white',activeforeground='black',padx=5,pady=5)
        person_btn.place(x=160,y=100)

        visitng_btn=Button(self,text='Visitings',font=('Courier',9),command=lambda:visiting(),border=3,fg='white',bg='black',cursor='target',width='15'
        ,activebackground='white',activeforeground='black',padx=5,pady=5)
        visitng_btn.place(x=160,y=150)

        dungeon_btn=Button(self,text='Dungeon',font=('Courier',9),command=lambda:dungeon(),border=3,fg='white',bg='black',cursor='target',width='15'
        ,activebackground='white',activeforeground='black',padx=5,pady=5)
        dungeon_btn.place(x=20,y=200)

        dungeonMoves_btn=Button(self,text='DungeonMoves',font=('Courier',9),command=lambda:dungeonMoves(),border=3,fg='white',bg='black',cursor='target',width='15'
        ,activebackground='white',activeforeground='black',padx=5,pady=5)
        dungeonMoves_btn.place(x=160,y=200)
        def visiting():
            Visitings().mainloop()
        def dungeon():
            Dungeon().mainloop()
        def dungeonMoves():
            DungeonMoves().mainloop()
        def offense():
            Offense().mainloop()
        def person():
            Person().mainloop()
        def convicts():
            Convicts().mainloop()
class Dungeon(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False,False)
        self.geometry('700x400')
        lbl_frame=Frame(self,bg='#0C1630')
        lbl_frame.place(x=0,y=0,width=200,height=400)
        lbl_frame1=Frame(self,bg='#0C1630')
        lbl_frame1.place(x=201,y=0,width=500,height=60)
        self.title('الزنزانات')
        Label(self,text='ID',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=90,y=6)
        self.per_id=ttk.Entry(self).place(x=33,y=27,width=130,height=25)
        Label(self,text='NAME',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=80,y=55)
        self. per_name=ttk.Entry(self).place(x=33,y=77,width=130,height=25)
        Label(self,text='SIZE',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=82,y=105)
        self. per_size=ttk.Entry(self).place(x=33,y=130,width=130,height=25)
        # ================================= buttom =========================================================
        insert_btn=Button(self,text='ADD',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        insert_btn.place(x=35,y=180)
        update_btn=Button(self,text='UPDATE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        update_btn.place(x=35,y=220)
        clear_btn=Button(self,text='CLEAR',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        clear_btn.place(x=35,y=260)
        view_btn=Button(self,text='VIEW DATA',command=self.checkData,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        view_btn.place(x=560,y=10)
        delet_btn=Button(self,text='DELETE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        delet_btn.place(x=210,y=10)
        self. per_delet=ttk.Entry(self).place(x=346,y=10,width=130,height=35)


        scrol_y=ttk.Scrollbar(self,orient=VERTICAL)
        scrol_y.place(x=682,y=60,height=342)
  
        self.table5=ttk.Treeview(self,height=16,columns=('Id','name','size'),show='headings',yscrollcommand=scrol_y.activate)
        scrol_y.config(command=self.table5.yview()) 
        self.table5.heading('Id',text='Id')
        self.table5.heading('name',text='Name')
        self.table5.heading('size',text='Size')

        self.table5.column('Id',width=15)
        self.table5.column('name',width=25)
        self.table5.column('size',width=25)

        self.table5.place(x=200,y=60,width=482,height=340)
        
    def conn(self):
        con=sqlite3.connect('prison.db')
        print('connected sqlite3')
        return con 
    def checkData(self):
        connect=self.conn()
        c=connect.cursor()
        c.execute("""select * from Dungeon""")
        data = c.fetchall()
        self.table5.delete(*self.table5.get_children())
        for i in data:
            self.table5.insert('', END, values=i)
            connect.commit()
        connect.close()
        
        
class DungeonMoves(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        lbl_frame=Frame(self,bg='#0C1630')
        lbl_frame.place(x=0,y=0,width=270,height=400)
        lbl_frame1=Frame(self,bg='#0C1630')
        lbl_frame1.place(x=271,y=0,width=430,height=60)
        self.resizable(False,False)
        self.title('زنزانات الاحداث')
        Label(self,text='ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=30)
        self. per_id=Entry(self).place(x=110,y=27,width=130,height=25)
        Label(self,text='DUNGEON ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=70)
        self. per_dungeonId=Entry(self).place(x=110,y=68,width=130,height=25)
        Label(self,text='PERSON ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=110)
        self. per_personId=Entry(self).place(x=110,y=107,width=130,height=25)
        Label(self,text='FROM DATE :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=150)
        self. per_fromDate=Entry(self).place(x=110,y=147,width=130,height=25)
        # ========================================== buttom ==============================================
        insert_btn=Button(self,text='ADD',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        insert_btn.place(x=10,y=220)
        update_btn=Button(self,text='UPDATE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        update_btn.place(x=140,y=220)
        clear_btn=Button(self,text='CLEAR',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        clear_btn.place(x=80,y=260)
        view_btn=Button(self,text='VIEW DATA',command=self.checkData,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        view_btn.place(x=560,y=10)
        delet_btn=Button(self,text='DELETE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        delet_btn.place(x=274,y=10)
        self.per_delet=Entry(self).place(x=410,y=10,width=130,height=35)

        scrol_y=ttk.Scrollbar(self,orient=VERTICAL)
        scrol_y.place(x=682,y=60,height=342)
    
        self.table6=ttk.Treeview(self,height=16,columns=('Id','dungeonId','personId','fromDate'),show='headings',yscrollcommand=scrol_y.activate)
        scrol_y.config(command=self.table6.yview())     
        self.table6.heading('Id',text='Id')
        self.table6.heading('dungeonId',text='Doungeon Id')
        self.table6.heading('personId',text='Person Id')
        self.table6.heading('fromDate',text='From Date')   

        self.table6.column('Id',width=15)
        self.table6.column('dungeonId',width=25)
        self.table6.column('personId',width=25)
        self.table6.column('fromDate',width=25)

        self.table6.place(x=270,y=60,width=412,height=340)

    def conn(self):
        con=sqlite3.connect('prison.db')
        print('connected sqlite3')
        return con 
    def checkData(self):
        connect=self.conn()
        c=connect.cursor()
        c.execute("""select * from DungeonMoves""")
        data = c.fetchall()
        self.table6.delete(*self.table6.get_children())
        for i in data:
            self.table6.insert('', END, values=i)
            connect.commit()
        connect.close()

class Visitings(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False,False)
        self.geometry('790x400')
        lbl_frame=Frame(self,bg='#0C1630')
        lbl_frame.place(x=0,y=0,width=290,height=400)
        lbl_frame1=Frame(self,bg='#0C1630')
        lbl_frame1.place(x=291,y=0,width=520,height=60)
        self.title('الزيارات')
        Label(self,text='ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=30)
        self.per_id=Entry(self).place(x=140,y=27,width=130,height=25)
        Label(self,text='DATE VISIT :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=70)
        self.per_dateVisit=Entry(self).place(x=140,y=68,width=130,height=25)
        Label(self,text='PERSON ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=110)
        self.per_personId=Entry(self).place(x=140,y=107,width=130,height=25)
        Label(self,text='VISIT OR NAME :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=150)
        self.per_visitOrname=Entry(self).place(x=140,y=147,width=130,height=25)
        Label(self,text='MOUNT IN MIUNTS :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=190)
        self. per_mountInminute=Entry(self).place(x=140,y=187,width=130,height=25)
        # ========================================= buttom ==============================================
        insert_btn=Button(self,text='ADD',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        insert_btn.place(x=10,y=270)
        update_btn=Button(self,text='UPDATE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        update_btn.place(x=150,y=270)
        clear_btn=Button(self,text='CLEAR',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        clear_btn.place(x=80,y=310)
        view_btn=Button(self,text='VIEW DATA',border=3,command=self.checkData,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        view_btn.place(x=620,y=10)
        delet_btn=Button(self,text='DELETE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        delet_btn.place(x=300,y=10)
        self. per_delet=Entry(self).place(x=435,y=10,width=130,height=35)


        scrol_y=ttk.Scrollbar(self,orient=VERTICAL)
        scrol_y.place(x=773,y=60,height=342)
    
        self.table4=ttk.Treeview(self,height=16,columns=('Id','dateVist','personId','VisitOrName','MountInMiuntes')
        ,show='headings',yscrollcommand=scrol_y.activate)
        scrol_y.config(command=self.table4.yview())
        self.table4.heading('Id',text='Id')
        self.table4.heading('dateVist',text='Date Visit')
        self.table4.heading('personId',text='Person Id')
        self.table4.heading('VisitOrName',text='Visit OR Name')
        self.table4.heading('MountInMiuntes',text='Mount In Minutes')
    

        self.table4.column('Id',width=1)
        self.table4.column('dateVist',width=15)
        self.table4.column('personId',width=15)
        self.table4.column('VisitOrName',width=15)
        self.table4.column('MountInMiuntes',width=15)

        self.table4.place(x=290,y=60,width=482,height=340)
        
    def conn(self):
        con=sqlite3.connect('prison.db')
        print('connected sqlite3')
        return con 
    def checkData(self):
        connect=self.conn()
        c=connect.cursor()
        c.execute("""select * from Visitings""")
        data = c.fetchall()
        self.table4.delete(*self.table4.get_children())
        for i in data:
            self.table4.insert('', END, values=i)
            connect.commit()
        connect.close()


class Offense(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False,False)
        self.geometry('650x400')
        self.title('الجرائم')
        lbl_frame=Frame(self,bg='#0C1630')
        lbl_frame.place(x=0,y=0,width=200,height=400)
        lbl_frame1=Frame(self,bg='#0C1630')
        lbl_frame1.place(x=201,y=0,width=450,height=60)
        Label(self,text='ID',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=90,y=6)
        self.per_id=Entry(self).place(x=33,y=27,width=130,height=25)
        Label(self,text='NAME',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=80,y=55)
        self. per_name=Entry(self).place(x=33,y=79,width=130,height=25)
        # ========================================= butttom ===================================================
        insert_btn=Button(self,text='ADD',border=3,command=self.insertData,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        insert_btn.place(x=35,y=180)
        update_btn=Button(self,text='UPDATE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        update_btn.place(x=35,y=220)
        clear_btn=Button(self,text='CLEAR',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        clear_btn.place(x=35,y=260)
        view_btn=Button(self,text='VIEW DATA',command=self.checkData,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        view_btn.place(x=510,y=10)
        delet_btn=Button(self,text='DELETE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        delet_btn.place(x=205,y=10)
        self. per_delet=Entry(self).place(x=343,y=10,width=130,height=35)

        scrol_y=ttk.Scrollbar(self,orient=VERTICAL)
        scrol_y.place(x=631,y=60,height=342)
    
        self.table1=ttk.Treeview(self,height=16,columns=('Id','Name'),show='headings',yscrollcommand=scrol_y.activate)
        scrol_y.config(command=self.table1.yview())
        self.table1.heading('Id',text='Id')
        self.table1.heading('Name',text='Name')
        
        self.table1.column('Id',width=50)
        self.table1.column('Name',width=50)
        self.table1.place(x=200,y=60,width=430)
    def conn(self):
        con=sqlite3.connect('prison.db')
        print('connected sqlite3')
        return con  
    def insertData(self):
            connect=self.conn()
            c=connect.cursor()
            c.execute("insert into Offense values('%s','%s')",(self.per_id,self.per_name))
            print('dgvdbrh')
            connect.commit()
            connect.close()
    def checkData(self):
        connect=self.conn()
        c=connect.cursor()
        c.execute('select * from Offense')
        data = c.fetchall()
        self.table1.delete(*self.table1.get_children())
        for i in data:
            self.table1.insert('', END, values=i)
            connect.commit()
        connect.close()

class Person(Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False,False)
        self.geometry('800x450')
        lbl_frame=Frame(self,bg='#0C1630')
        lbl_frame.place(x=0,y=0,width=300,height=500)
        lbl_frame1=Frame(self,bg='#0C1630')
        lbl_frame1.place(x=301,y=0,width=500,height=60)
        Label(self,text='ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=30)
        self.per_id=Entry(self).place(x=100,y=27,width=130,height=25)
        Label(self,text='FIRST NAME :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=70)
        self.per_firstName=Entry(self).place(x=100,y=68,width=130,height=25)
        Label(self,text='FATHER :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=110)
        self.per_father=Entry(self).place(x=100,y=107,width=130,height=25)
        Label(self,text='LAST NAME :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=150)
        self.per_lastName=Entry(self).place(x=100,y=147,width=130,height=25)
        Label(self,text='GENDER :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=190)
        self.per_gender=ttk.Combobox(self,value=('male','female'),state='readonly').place(x=100,y=185,width=130,height=25)
        Label(self,text='BIRTH YEAR :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=230)
        self.per_birthyear=Entry(self).place(x=100,y=227,width=130,height=25)
        Label(self,text='ADDRESS :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=270)
        self.per_address=Entry(self).place(x=100,y=267,width=130,height=25)
        self.title('المساجين')
        #========================================== buttum ========================================================
        insert_btn=Button(self,text='ADD',command=self.insertData,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        insert_btn.place(x=10,y=320)
        update_btn=Button(self,text='UPDATE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        update_btn.place(x=150,y=320)
        clear_btn=Button(self,text='CLEAR',command=self.clear,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        clear_btn.place(x=80,y=360)
        view_btn=Button(self,text='VIEW DATA',command=self.checkData,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        view_btn.place(x=660,y=10)
        delet_btn=Button(self,text='DELETE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        delet_btn.place(x=310,y=10)
        self.per_delet=Entry(self).place(x=445,y=10,width=130,height=35)
        # ==================================== VIEW DATA TABLE =================================================

        scrol_y=ttk.Scrollbar(self,orient=VERTICAL)
        scrol_y.place(x=782,y=60,height=384)
        self.table2=ttk.Treeview(self,height=16,columns=('Id','firstName','father','lastName','gender','birthYear','address'),yscrollcommand=scrol_y.activate)
        scrol_y.config(command=self.table2.yview())
        self.table2.heading('Id',text='Id')
        self.table2.heading('firstName',text='First Name')
        self.table2.heading('father',text='Father')
        self.table2.heading('lastName',text='Last Name')
        self.table2.heading('gender',text='Gender')
        self.table2.heading('birthYear',text='Birth Year')
        self.table2.heading('address',text='Address')      
        self.table2['show']='headings'
        self.table2.column('Id',width=15)
        self.table2.column('firstName',width=15)
        self.table2.column('father',width=15)
        self.table2.column('lastName',width=15)
        self.table2.column('gender',width=15)
        self.table2.column('birthYear',width=15)
        self.table2.column('address',width=15)
        self.table2.place(x=300,y=60,width=481,height=390)
    def conn(self):
        con=sqlite3.connect('prison.db')
        print('connected sqlite3')
        return con 
    def checkData(self):
        connect=self.conn()
        c=connect.cursor()
        c.execute("""select * from Person""")
        data = c.fetchall()
        self.table2.delete(*self.table2.get_children())
        for i in data:
            self.table2.insert('', END, values=i)
            connect.commit()
        connect.close()
    def insertData(self):
        connect=self.conn()
        c=connect.cursor()
        c.execute("""insert into Person values('{}','{}','{}','{}','{}','{}','{}');""".format(
        self.per_id,self.per_firstName, self.per_father, self.per_lastName
        , self.per_gender,self.per_birthyear,self.per_address))
        connect.commit()
        connect.close()
    def clear(self):
        self.per_id.delete(0, 'end')
        self.per_firstName.delete(0, 'end')
        self.per_father.delete(0, 'end')
        self.per_lastName.delete(0, 'end')
        self.per_address.delete(0, 'end')
        self.per_birthyear.delete(0, 'end')        

class Convicts(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('700x400')
        self.title('الأحكام')
        self.resizable(False,False)
        lbl_frame=Frame(self,bg='#0C1630')
        lbl_frame.place(x=0,y=0,width=270,height=500)
        lbl_frame1=Frame(self,bg='#0C1630')
        lbl_frame1.place(x=271,y=0,width=430,height=60)
        Label(self,text='ID : ',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=30)
        self.per_id=Entry(self).place(x=100,y=27,width=130,height=25)
        Label(self,text='FROM DATE :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=70)
        self.per_fromdate=Entry(self).place(x=100,y=68,width=130,height=25)
        Label(self,text='TO DATE :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=110)
        self.per_todate=Entry(self).place(x=100,y=107,width=130,height=25)
        Label(self,text='PERSON ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=150)
        self.per_personId=Entry(self).place(x=100,y=147,width=130,height=25)
        Label(self,text='OFFENSE ID :',bg='#0C1630',font=('times new roman',10,'bold'),fg='white').place(x=10,y=190)
        self.per_offenseId=Entry(self).place(x=100,y=185,width=130,height=25)
        # ========================================= buttom =============================================
        insert_btn=Button(self,text='ADD',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        insert_btn.place(x=10,y=240)
        update_btn=Button(self,text='UPDATE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        update_btn.place(x=138,y=240)
        clear_btn=Button(self,text='CLEAR',command=self.clear ,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='15'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        clear_btn.place(x=80,y=280)
        view_btn=Button(self,text='VIEW DATA',command=self.checkData,border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        view_btn.place(x=560,y=10)
        delet_btn=Button(self,text='DELETE',border=3,fg='gold',bg='black',font=('times new roman',10,'bold'),cursor='target',width='16'
        ,activebackground='black',activeforeground='white',padx=5,pady=5)
        delet_btn.place(x=275,y=10)
        self. per_delet=Entry(self).place(x=415,y=10,width=130,height=35)
        
        scrol_y=ttk.Scrollbar(self,orient=VERTICAL)
        scrol_y.place(x=680,y=60,height=340)
     
        self.table3=ttk.Treeview(self,height=16,columns=('Id','fromDate','toDate','personId','offenseId'),show='headings',yscrollcommand=scrol_y.activate)
        scrol_y.config(command=self.table3.yview())    
        self.table3.heading('Id',text='Id')
        self.table3.heading('fromDate',text='From Date')
        self.table3.heading('toDate',text='To Date')
        self.table3.heading('personId',text='Person Id')
        self.table3.heading('offenseId',text='Offense Id')
    

        self.table3.column('Id',width=15)
        self.table3.column('fromDate',width=25)
        self.table3.column('toDate',width=25)
        self.table3.column('personId',width=25)
        self.table3.column('offenseId',width=25)

        self.table3.place(x=270,y=60,width=410,height=340)

    def conn(self):
        con=sqlite3.connect('prison.db')
        print('connected sqlite3')
        return con 
    def checkData(self):
        connect=self.conn()
        c=connect.cursor()
        c.execute("""select * from Convicts""")
        data = c.fetchall()
        self.table3.delete(*self.table3.get_children())
        for i in data:
            self.table3.insert('', END, values=i)
            connect.commit()
        connect.close()
    def clear(self):
        self.per_id.delete(0, 'end')
        self.per_fromdate.delete(0, 'end')
        self.per_todate.delete(0, 'end')
        self.per_personId.delete(0, 'end')
        self.per_offenseId.delete(0, 'end')  


Main().mainloop()