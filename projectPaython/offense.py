
import sqlite3
from tokenize import Name
class Date:
    def __init__ (self,year,month,day):

        if int(year) > 1930 and int(year) < 2022 :
            self.__year=year
        else:
            print (" the year must be in range 1930 to dateNow ")
        if int(month) > 0 and int(month) < 13 :
            self.__month=month
        else:
            print (" the month must be in range 1 to 12 ")
        if int(day) > 0 and int(day) < 32 :
            self.__day=day
        else:
            print (" the day must be in range 1 to 31 ")

    def getYear(self):
        return self.__year
    def getMonth(self):
        return self.__month
    def getDay(self):
        return self.__day
    def allDate(self):
        return self.getYear()+str("-")+self.getMonth()+str("-")+self.getDay()
# =========================== OFFENSE TABLE==================================  
    
class Offense_Win:
    def __init__(self,Id,name):
        if   Id > 0:
            self.Id=Id
        if len(name)>2:
            self.name=name

    try :
        def conn(self):
            con=sqlite3.connect('prison.db')
            print('connected sqlite3')
            return con  
        def insertData(self):
            Id=int(input('Enter ID : '))  
            name=input('Enter Name : ')
            connect=self.conn()
            c=connect.cursor()
            c.execute("insert into Offense values('%s','%s')"%(Id,name))
            connect.commit()
            print('inserted row')
            connect.close()
        def deleteData(self):
            Id=int(input('Enter ID : '))  
            connect=self.conn()
            c=connect.cursor()
            c.execute("delete from Offense where Id= ? " ,(Id,))
            print('delete table')
            connect.commit()
            connect.close()
        def checkData(self):
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from Offense')
            data=c.fetchall()
            i=0
            while i<len(data):
                print(data[i])
                i+=1
        def UpdateData(self):
            name=input('Enter Name : ')
            Id=int(input('Enter ID : '))  
            connect=self.conn()
            c=connect.cursor()
            c.execute('update Offense set  name=? where id=?'\
                        ,(name,Id))
            print('update table')
            connect.commit()
            connect.close()
        def SearchData(self):
            name=input('Enter Name : ')
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from  Offense where name=?  '\
                        ,(name))
            rows=c.fetchall()
            connect.close()
            print(rows)
    except Exception as ee:
         print(ee)


# ================================== CONVICTS TABLE =======================================
        
class Convicts_Win:
    def __init__(self,Id,fromdate,todate,pId,oId):
        self.__Id=Id
        self.__fromDate=fromdate
        self.__toDate=todate
        self.__personId=pId
        self.__offenseId=oId
        
    def getId(self):
        if self.__Id > 0 :
           return self.__Id

    def getFromdate(self):
        return self.__fromDate
  
    def getTodate(self):
        return self.__toDate

    def getPersonId(self):
        if self.__personId > 0 :
           return self.__personId

    def getOffenseId(self):
        if self.__offenseId > 0 :
           return self.__offenseId

    
            
    try :
        def conn(self):
            con=sqlite3.connect('prison.db')
            print('connected sqlite3')
            return con  
        
        #========================= INSERT DATA ================================
        def insertData(self):
            Id=int(input("Enter ID : "))
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            d1=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            fromDate=d.allDate()
            toDate=d1.allDate()
            personId=int((input("Enter PersonID : ")))
            offenseId=int((input("Enter OfeenseID : ")))
            connect=self.conn()
            c=connect.cursor()
            s="insert into Convicts values('%s','%s','%s','%s','%s')"%(Id,fromDate,toDate,personId,offenseId)
            c.execute(s)
            connect.commit()
            print('inserted row')
            connect.close()
        #========================= DELETE DATA ================================
        def deleteData(self):
                Id=int(input("Enter ID : "))
                connect=self.conn()
                c=connect.cursor()
                c.execute("delete from Convicts where Id= ? " ,(Id,))
                print('delete table')
                connect.commit()
                connect.close()
        #========================= VIEW DATA ================================
        def checkData(self):
                connect=self.conn()
                c=connect.cursor()
                c.execute('select * from Convicts')
                data=c.fetchall()
                i=0
                while i<len(data):
                    print(data[i])
                    i+=1
        #========================= UPDATE DATA ================================
        def updateData(self):
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            d1=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            fromDate=d.allDate()
            toDate=d1.allDate()
            personId=int((input("Enter PersonID : ")))
            offenseId=int((input("Enter OfeenseID : ")))
            Id=int(input('Enter ID : '))
            connect=self.conn()
            c=connect.cursor()
            c.execute('update Convicts set  fromDate=? ,toDate=? ,personId=? ,offenseId=?  where Id=?'\
                       ,(fromDate,toDate,personId,offenseId,Id))
            print('update table')
            connect.commit()
            connect.close()
        # ========================= SERACH DATA  =====================================
        def SearchData(self):
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            d1=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            fromDate=d.allDate()
            toDate=d1.allDate()
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from  Convicts where  fromDate=? or toDate=? '\
                        ,(fromDate,toDate))
            rows=c.fetchall()
            connect.close()
            print(rows) 
    except Exception as ee:
        print(ee)

# ===================================== PERSON TABLE ==============================================
class Person_Win:
    def __init__(self,Id,firstname,father,lastname,gender,birthyear,address):
        if  Id > 0:
            self.Id=Id
        if len(firstname) > 2:
            self.firstName=firstname
        if len(father) > 2:
            self.father=father
        if len(lastname) > 2:
            self.lastName=lastname
        if gender in ('male','female'):
            self.gender=gender
            self.birthYear=birthyear
        if len(address) > 2:
            self.address=address
        
   
    try :   
        def conn(self):
            con=sqlite3.connect('prison.db')
            print('connected sqlite3')
            return con 
          #========================= INSERT DATA ================================
        def insertData(self):
            Id=int(input("Enter ID : "))
            firstName=(input("Enter FirstName : "))
            father=(input("Enter Father : "))
            lastName=(input("Enter LastName : "))
            gender=(input("Enter Gender : "))
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            birthYear=d.allDate()
            address=input("Enter Adress : ")
            connect=self.conn()
            c=connect.cursor()
            c.execute("insert into Person values('%s','%s','%s','%s','%s','%s','%s')"%(
            Id,firstName,father,lastName,gender,birthYear,address))
            print('inserted row')
            connect.commit()
            connect.close()
          #========================= DELETE DATA ================================
        def deleteData(self):
            Id=int(input("Enter ID : "))
            connect=self.conn() 
            c=connect.cursor()
            c.execute("delete from Person where Id= ? " ,(Id,))
            print('delete table')
            connect.commit()
            connect.close()
          #========================= VIEW DATA ================================
        def checkData(self):
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from Person')
            data=c.fetchall()
            i=0
            while i<len(data):
                print(data[i])
                i+=1
          #========================= UPDATE DATA ================================
        def updateData(self):
            firstName=(input("Enter FirstName : "))
            father=(input("Enter Father : "))
            lastName=(input("Enter LastName : "))
            gender=(input("Enter Gender : "))
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            birthYear=d.allDate()
            address=input("Enter Adress : ")
            Id=int(input("Enter ID : "))
            connect=self.conn()
            c=connect.cursor()
            c.execute('update Person set   firstName=? ,father=? , lastName=? , gender=? , birthYear=? , address=?  where Id=?'\
                    ,(firstName,father,lastName,gender,birthYear,address,Id))
            print('update table')
            connect.commit()
            connect.close()
          #========================= SERACH DATA ================================
        def SearchData(self):
            firstName=(input("Enter FirstName : "))
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from  Person where firstName=?  ',\
                        (firstName))
            rows=c.fetchall()
            connect.close()
            print(rows)
    except Exception as ee:
        print(ee)

# ================================ VISITINGS TABLE  ========================================

class Visitings_Win:
    def __init__(self,Id,dateVisit,personId,VisitOrName,mountInMinutes):
        if Id > 0 :
            self.__Id=Id
        self.__dateVisited=dateVisit
        if personId > 0 :
            self.__personId=personId
        if len(VisitOrName) > 2 :
            self.__VisitOrName=VisitOrName
        if mountInMinutes > 0 :
            self.__MountInMinutes=mountInMinutes


    try :
        def conn(self):
            con=sqlite3.connect('prison.db')
            print('connected sqlite3')
            return con
      
          #========================= INSERT DATA ================================
        def insertData(self):
            Id=int(input("Enter ID : "))
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            dateVisited=d.allDate()
            personId=int(input("Enter personID : "))
            VisitOrName=input("Enter visitor Name : ")
            MountInMinutes=int(input("Enter Mount In Minute : "))
            connect=self.conn()
            c=connect.cursor()
            c.execute("insert into Visitings values('%s','%s','%s','%s','%s')"%(Id,dateVisited,personId,VisitOrName,MountInMinutes))
            connect.commit()
            print('inserted row')
            connect.close()
          #========================= DELETE DATA ================================
        def deleteData(self,Id):
            connect=self.conn()
            c=connect.cursor()
            c.execute("delete from Visitings where Id= ? " ,(Id,))
            print('delete table')
            connect.commit()
            connect.close()
        def checkData(self):
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from Visitings')
            data=c.fetchall()
            i=0
            while i<len(data):
                print(data[i])
                i+=1
          #========================= UPDATE DATA ================================
        def updateData(self):
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            dateVisited=d.allDate()
            personId=int(input("Enter personID : "))
            VisitOrName=input("Enter visitor Name : ")
            MountInMinutes=int(input("Enter Mount In Minute : "))
            Id=int(input("Enter ID : "))
            connect=self.conn()
            c=connect.cursor()
            c.execute('update Visitings set dateVisited=? ,personId=? , VisitOrName=? , MountInMinutes=?   where Id=? '\
                       ,(dateVisited,personId,VisitOrName,MountInMinutes,Id))
            print('update table')
            connect.commit()
            connect.close()
          #========================= SERACH DATA ================================
        def SearchData(self,dateVisited="",personId="",VisitOrName="",MountInMinutes=""):
                connect=self.conn()
                c=connect.cursor()
                c.execute('select * from Visitings where dateVisited=? OR personId=? OR VisitOrName=? OR MountInMinutes=? '\
                        ,(dateVisited,personId,VisitOrName,MountInMinutes))
                rows=c.fetchall()
                connect.close()
                print(rows) 
    except Exception as ee:
        print(ee)
 # ===================================== DUNGEON TABLE ==========================================       
class Dungeon_Win:
    def __init__(self,Id,Name,Size):
        self.__Id=Id
        self.__Name=Name
        self.__Size=Size
    def getId(self):
        if self.__Id > 0:
           return self.__Id
    def getName(self):
        if len(self.__Name) > 2:
           return self.__Name
    def getSize(self):
        if self.__Size > 0:
           return self.__Size
    try :
        def conn(self):
            con=sqlite3.connect('prison.db')
            print('connected sqlite3')
            return con
             #========================= INSERT DATA ================================
        def insertData(self):  
            Id=int(input('Enter Id : '))
            Name=input('Enter Name : ')
            Size=input('Enter Size : ')
            connect=self.conn()
            c=connect.cursor()
            c.execute("insert into Dungeon values('%s','%s','%s')" %(Id,Name,Size))
            connect.commit()   
            print('inserted row')
            connect.close()
             #========================= DELETE DATA ================================
        def deleteData(self):
            Id=int(input('Enter Id : '))
            connect=self.conn()
            c=connect.cursor()
            c.execute('delete from Dungeon where Id= ? ',(Id))
            print('delete table')
            connect.commit()
            connect.close()
             #========================= VIEW DATA ================================
        def checkData(self):
                connect=self.conn()
                c=connect.cursor()
                c.execute('select * from Dungeon')
                data=c.fetchall()
                i=0
                while i<len(data):
                    print(data[i])
                    i+=1
             #========================= UPDATE DATA ================================
        def UpdateData(self):  
            Name=input('Enter Name : ')
            Size=input('Enter Size : ')
            Id=int(input('Enter Id : '))
            connect=self.conn()
            c=connect.cursor()
            c.execute('update Dungeon set  Name=? ,Size=?  where Id=?'\
                       ,(Name,Size,Id))
            print('update table')
            connect.commit()
            connect.close()
             #========================= SERACH DATA ================================
        def SearchData(self):
            Name=input('Enter Name : ')
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from  Dungeon where  Name=?  '\
                        ,(Name))
            rows=c.fetchall()
            connect.close()
            print(rows) 
    except Exception as ee:
        print(ee)
class DungeonMoves_Win:
    
    def __init__(self,Id,dungeonId,personId,fdate):
        if Id > 0:
            self.__Id=Id
        if dungeonId > 0 :
            self.__dungeonId=dungeonId
        if personId > 0 :   
            self.__personId=personId
        self.__FromDate=fdate
   
    try :
        def conn(self):
            con=sqlite3.connect('prison.db')
            print('connected sqlite3')
            return con
            #========================= INSERT DATA ================================
        def insertData(self):
            Id=int(input("Enter ID : "))
            dungeonId=int(input("Enter Dungeon ID : "))
            personId=int(input("Enter Person ID : "))
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            FromDate=d.allDate()
            connect=self.conn()
            c=connect.cursor()
            c.execute("insert into DungeonMoves values('%s','%s','%s','%s')"%(Id,dungeonId,personId,FromDate))
            connect.commit()   
            print('inserted row')
            connect.close()
             #========================= DELETE DATA ================================
        def deleteData(self):
            Id=int(input("Enter ID : "))
            connect=self.conn()
            c=connect.cursor()
            c.execute("delete from DungeonMoves where Id= ? " ,(Id,))
            print('delete table')
            connect.commit()
            connect.close()
        def checkData(self):
                connect=self.conn()
                c=connect.cursor()
                c.execute('select * from DungeonMoves')
                data=c.fetchall()
                i=0
                while i<len(data):
                    print(data[i])
                    i+=1
             #========================= UPDATE DATA ================================
        def updateData(self):
            dungeonId=int(input("Enter Dungeon ID : "))
            personId=int(input("Enter Person ID : "))
            d=Date(input("Enter Year : "), 
            input("Enter Month : "),
            input("Enter Day : "))
            FromDate=d.allDate()
            Id=int(input("Enter ID : "))
            connect=self.conn()
            c=connect.cursor()
            c.execute('update DungeonMoves set  dungeonId=? ,personId=?, FromDate=?  where Id=?'\
                       ,(dungeonId,personId,FromDate,Id))
            print('update table')
            connect.commit()
            connect.close()
             #========================= SERACH DATA ================================
        def SearchData(self):
            Id=int(input("Enter ID : "))
            connect=self.conn()
            c=connect.cursor()
            c.execute('select * from  DungeonMoves where Id=? '\
                        ,(Id))
            rows=c.fetchall()
            connect.close()
            print(rows) 
   
          
            # قائمة الزنزانات التي انتقل اليها سجين
        def selectIsNameDungeon(self,firstName,father,lastName,):
            connect=self.conn()
            c=connect.cursor()
            c.execute("""select Dungeon.Name from Dungeon where Dungeon.Id
            in(select DungeonMoves.dungeonId from DungeonMoves where personId=(select Person.Id from Person 
            where Person.firstName=? and father=? and Person.lastName=?))""" ,(firstName,father,lastName))
            connect.commit()
            rows=c.fetchall()
            connect.close()
            print(rows) 
        # اسماء السجناء وفق جرم معين
        def selectPersonConvicts(self):
            name=input('Enter Name : ')
            connect=self.conn()
            c=connect.cursor()
            c.execute("""select Person.firstName from Person where Person.Id
            in(select Convicts.personId from Convicts where Convicts.offenseId =(select Offense.Id from Offense
            where Offense.Name=? ))""" ,(Name))
            connect.commit()
            rows=c.fetchall()
            connect.close()
            print(rows) 
    except Exception as ee:
        print(ee)
d=DungeonMoves_Win(1,2,3,"fdtydut")
d1=Dungeon_Win(1,"dungeon",5)
visit=Visitings_Win(1, "2/2/2002", 2, "mohammd",5)
p1=Person_Win(1, "aisha","khled", "alkrz","fmale" ,2000, "albab")
c=Convicts_Win(1,2000-2-2,2001-1-1,2,1)
o=Offense_Win(1,"ajhsj")
o.insertData()
