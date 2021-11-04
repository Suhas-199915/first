from abc import *
import sqlite3
class universities(ABC):
    @abstractmethod
    def fees(self,fees):
        pass
    @abstractmethod
    def bank(self,bname):
        pass
    @abstractmethod
    def roi(self,n):
        pass
    
class USC(universities):
    def fees(self,fees):
        self.fees=fees
        return self.fees
    def bank(self,b):
        self.bname=b
        return self.bname
    def roi(self,n):
        self.roi=n
        return self.roi

class UCLA(universities):
    def fees(self,fees):
        self.fees=fees
        return self.fees
    def bank(self,b):
        self.bname=b
        return self.bname
    def roi(self,n):
        self.roi=n
        return self.roi

class MIT(universities):
    def fees(self,fees):
        self.fees=fees
        return self.fees
    def bank(self,b):
        self.bname=b
        return self.bname
    def roi(self,n):
        self.roi=n
        return self.roi

def insert_stud_db(Name,Registration_no,Year,Verbal_score,Quant_score,Sum):
  co.execute('INSERT INTO student_information VALUES(?,?,?,?,?,?)',(Name,Registration_no,Year,Verbal_score,Quant_score,Sum))

def print_stud_db():
  cur=co.execute('SELECT * from student_information')
  for row in cur:
    print(row)

  
def create_stud_db():
  tables=co.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='student_information' ''').fetchall()
  if tables==[]:
    conn.execute('''CREATE TABLE student_information(
    Student_name VARCHAR[10],
    Reg_num INT PRIMARY KEY,
    Year_of_examination INT,
    Verbal_score INT,
    Quant_score INT,
    Total_score INT)''')
  return 
def create_clg_db():
  tables=co.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='clg_info' ''').fetchall()
  if tables==[]:
	  conn.execute(''' CREATE TABLE clg_info(
    Clg_name VARCHAR[10],
    Fee INT
    )''')
  return
def insert_clg_db(clg,fee):
  co.execute('INSERT INTO clg_info VALUES(?,?)',(clg,fee))
def print_clg_db():
  cur=co.execute('SELECT * FROM clg_info')
  for row in cur:
    print(row) 


conn=sqlite3.connect('project.db')
co=conn.cursor()
db_status='False'
Name=input("Enter you name:-")
print(Name)
Registration_no=input("Enter your Seven digit registration no:- ")
print(Registration_no)
Year=input("Enter the year of examination:- ")
print(Year)
Verbal_score=int(input("Enter your verbal score out of 170:- "))
Quant_score=int(input("Enter your Quant score out of 170;- "))
Sum=Verbal_score+Quant_score
print("Your GRE score out of 340:- ",Sum)
create_stud_db()
insert_stud_db(Name,Registration_no,Year,Verbal_score,Quant_score,Sum)
print_stud_db()

Question=input("Do you want to have a look at the list of universities?;-")
l1=["USC","UCLA","MIT"]
l2=[45000,50000,60000]


if Question=='yes':
    print("Here are the list of universities with the respective fees:")
    create_clg_db()
    for data in range(len(l1)):
      insert_clg_db(l1[data],l2[data])
    print_clg_db()
for i in range(len(l1)):
    print('college:',l1[i],'Fees:',l2[i])


a=USC()

b=UCLA()

c=MIT()


if Sum >=315 and Sum <=320:
    print('The college available for you with fees is:-',l1[3],"",l2[3],'$')
if Sum >=321 and Sum <=325:
    print('The colleges available for you with fees are:-',l1[0],"",",",l1[1])
    print("Details of USC")
    print("Fees=",a.fees(45000),"$")
    print("Banks available=", a.bank(["HDFC","Axis","SBI","Kotak","HSBC"]))
    print("Rate of interest=",a.roi(8))
    print()
    print("Details of UCLA")
    print("Fees=",b.fees(50000),"$")
    print("Banks available=",b.bank(["HDFC","Axis","SBI","Kotak","HSBC"]))
    #print("Rate of interest=",b.roi(9)) 
    print("Are you looking for finance options")
elif Sum>=326 and Sum<=340:
    print('The college available for you with fees is:-',l1[2],"",l2[2],"$")
    print("Fees=",c.fees(60000),"$")
    print("Banks available=",c.bank(["HDFC","Axis","SBI","Kotak","HSBC"]))
    #print("Rate of interest=",b.roi(9)) 
    #print("Rate of interest=",b.roi(9)) 
elif Sum<=320:
    print("Sorry, No colleges are available.Better luck next time!!")


#Banking code
d={"SBI":[5,"no"], "Axis":[7,"yes"],
"HDFC":[8,"yes"], "HSBC":[6,"yes"],
"Kotak":[6.5,"no"]}

a=input("Are you looking for finance options: yes or No ")
if a=="yes":
    l=[]
    b=input("do you want a bank with onlin services?: yes or no ")
    if b=="yes":
        for i in d:
            if d[i][1]=="yes":
                l.append(i)
    else:
        for i in d:
            if d[i][1]!="yes":
                l.append(i)
    print(l)

#print(d)
#print(d["SBI"][1]["Savings"])


def fun(l):
    a=100000
    for i in l:
       for j in d:
           if i==j:
               if int(a)>d[i][0]:
                   a=d[i][0]
                   b=i
    print("The bank which is most suitable to you is", b , "bank")    
    print("Do you want to continue with", b, "bank")
    x=input()
    if x=="yes":
        print("You have selected", b, "bank")
    else:
        l.remove(b)
        print(l)
        y1=input("Do you want to select any bank from above list of banks? Yes or No:")
        if y1=="yes":
            x2=input("Select from any bank")
            if x2 in l:
                print("You have chosen",x2,"bank")
            else:
                print("You haven't chosen any from the given list of banks")
        else:
            x2=input("Do you want more parameters to select upon your bank? We have 1 more option i.e.the rate of interest. Yes or No : ")
            if x2=="yes":
                mb=[]
                for i in l:
                    if i in d:
                        mb.append(d[i][0])
                print(mb)
                x3=int(input("From the given list of minimum balances which would you like to go for:"))
                if x3 in mb:
                    for i in d:
                        if d[i][0]==x3:
                            print("You have chosen",i,"bank")
            else:
                print("Thank you for using our application")
fun(l)