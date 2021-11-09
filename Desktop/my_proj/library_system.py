import mysql.connector
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
    
    def issue_book(self,b_name=None,b_id=None):
        data=self.search_book(book_name=b_name , book_id=b_id)
        Cust_name=input("Enter customer name:-")
        mob_num=input("Enter mobile number:-")
        issue_date=input()

        
        
        
    


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
    b.add_book("Book1","auth1","sub1","2020-09-12",10,20,100)
    b.add_book("Book21","auth2","sub2","2020-09-13",11,20,100)
    b.add_book("Book3","auth3","sub3","2020-09-12",12,20,100)
    b.add_book("Book1","auth1","sub1","2020-09-12",10,2,100)
    b.add_book("Book3","auth3","sub3","2020-09-12",13,20,100)
    b.delete_book(13)
    data=b.search_book(Publication_date="2020-09-12")
    #b.issue_book(b_name="Book21")
    for i in data:
        print(i)
    
    
   
    
    
    