import mysql.connector
from datetime import date
from random import randint 
class books:
    def __init__(self):
        book_name=None
        Author_name=None
        Publication_date=None
        id_num=None
        rack_num=None
    
    def add_book(self,book_name,Author_name,subject,Publication_date,book_id,num_of_books,rack_num):
        my_cur.execute("select book_id from Book_tab where book_id=%s", (book_id,))
        data= my_cur.fetchall()
        if len(data)==0:
            my_cur.execute('''insert into Book_tab values(%s,%s,%s,%s,%s,%s,%s)''',(book_name,Author_name,subject,Publication_date,book_id,rack_num,num_of_books))
        else:
            my_cur.execute('''update Book_tab
            set num_of_books=num_of_books+%s
            where book_id=%s
            ''',(num_of_books,book_id))
        my_cur.execute("commit")

    
    def delete_book(self,book_id):
        my_cur.execute("select book_id from Book_tab where book_id=%s", (book_id,))
        data= my_cur.fetchall()
        if len(data)==0:
            raise Exception("No books found with given book id")
        else:
            my_cur.execute('''delete from Book_tab where book_id=%s''',(book_id,))
    
    
    def search_book(self,book_id=None,Author_name=None,subject=None,book_name=None,Publication_date=None,rack_num=None):
        my_cur.execute('''select * from Book_tab
                        where book_id=%s or author_name=%s or sub_category=%s or book_name=%s or pub_date=%s or rack_num=%s ''',(book_id,Author_name,subject,book_name,Publication_date,rack_num))
        data= my_cur.fetchall()
        if data==0:
            raise Exception("No such books found!")
        return data
    
    def reg_member(self):
        cust_name=input("Enter customer name:-")
        try:
            mob_num=int(input("Enter mobile number:-"))
        except:
            raise Exception("Enter valid details") 
        
        if len(str(mob_num))<10 :
            raise Exception("Enter valid details") 
        my_cur.execute("select mob_num from customer_table where mob_num=%s", (mob_num,))
        data= my_cur.fetchall()
        if len(data)==0:
            mem_id=str(randint(0,9))
            for i in range(6):
	            mem_id+=str(randint(0,9))
            my_cur.execute('''insert into customer_table values(%s,%s,%s,%s)''',(cust_name,str(mob_num),mem_id,0))
            my_cur.execute('''commit''')

        else:
            raise Exception("This mobile number already exists")
            

            
    def verify_user(self):
        pwd=input("Enter your user id:-")
        my_cur.execute("select mem_id from customer_table where mem_id=%s", (pwd,))
        data=my_cur.fetchall()
        if len(data)==0:
            raise Exception("No records with this id")
            return False
        else:   
            return True
    
    def reserve_book(self,book_id):
        print("Your book is reserved")
    
    def issue_book(self):
        if self.verify_user()==True:
            b_id=input("Enter id  of book:")
            data=self.search_book(book_id=b_id)
            
            if len(data)==0:
                raise Exception("No records with this id")
            
            else:
                if data[0][6]>0:
                    mem_id=input("Please enter ur user id:-")
                    
                    my_cur.execute("select * from customer_table where mem_id=%s", (mem_id,))
                    nob_data=my_cur.fetchall()
                    
                    if nob_data[0][3]<5:
                        my_cur.execute("select book_id from issue_book_table where book_id=%s and customer_id=%s", (b_id,mem_id))
                        nosb=my_cur.fetchall()
                        print(nosb)
                        if len(nosb)>1:
                            raise Exception("Sorry you cannot take same book again")
                        else:        
                            my_cur.execute('''insert into issue_book_table values(%s,%s,%s,%s)''',(mem_id,b_id,date.today(),None))
                        
                            my_cur.execute('''update Book_tab 
                                              set num_of_books=num_of_books-1 
                                              where book_id=%s ''',(b_id,))
                            
                            my_cur.execute('''update customer_table
                                              set cust_books=cust_books+1
                                              where mem_id=%s''',(mem_id,))
                            my_cur.execute('''commit''')
                    else:
                        raise Exception('We are sorry,but you cannot take more than 5 books')
                else:
                    print("OOPS! the book is   out of stock")
                    ch=input('Would u like to reserve this book?(y/n)')
                    if ch=='y':
                        self.reserve_book(b_id)
                    else:
                        raise Exception("Come back next time")
    
        else:
            raise Exception("Please register as member")
    
    def deposit_book(self,book_id):
        if self.verify_user()==True:
            my_cur.execute("select issue_date from issue_book_table where book_id=%s",(book_id,))
            submit_date=date(2021,11,24)
            data=my_cur.fetchall()
            diff=submit_date-data[0][0]
            if diff.days>10:
                fine=(diff.days-10)*10
                print("Please pay a fine of Rs.",fine," for further process")
                return
            else:
                mem_id=input("Please enter ur user id:-")
                
                my_cur.execute('''update Book_tab 
                                  set num_of_books=num_of_books+1 
                                  where book_id=%s ''',(book_id,))
                my_cur.execute('''update customer_table
                                  set cust_books=cust_books-1
                                  where mem_id=%s''',(mem_id,))
                my_cur.execute('''update issue_book_table
                                  set submit_date=%s
                                  where book_id=%s''',(submit_date,book_id))

                my_cur.execute("commit")
                            
                            
if __name__=='__main__':
    db=mysql.connector.connect(host="localhost",user="root",password="pass@word1")
    b=books()
    my_cur=db.cursor(buffered=True)
    my_cur.execute("use proj_new_db")
    print('''WELCOME TO LIBRARY SYSTEM)
    How can we help you?
    1. Register (for new users only)
    2. Log in
    3. Add books
    4. Issue books 
    5. Submit books
    6. Delete books''')
    b.deposit_book(12)
    
   

    
    
    
   
    
    
    