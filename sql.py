from pymysql import *
from time import *
class Admin:
    def insert(self):
        self.user_name=input("Enter the Name:")
        self.password=input("Enter your password:")
        self.phone_no=int(input("Enter your Phone no:"))
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="insert into admin values('{0}','{1}',{2})".format(self.user_name,self.password,self.phone_no)
        cur=self.con.cursor()
        cur.execute(q)
        self.con.commit()
        self.con.close()
        print("Data Saved...")
        
    def update(self):
        self.user_name=input("Enter the Name:")
        self.password=input("Enter your password:")
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="update admin set password='{0}' where user_name='{1}'".format(password,user_name)
        cur=self.con.cursor()
        r=cur.execute(q)
        self.con.commit()
        if(r!=0):
            print("Data Updated...")
        else:
            print("Data invalid...")
            
    def delete(self):
        self.user_name=input("Enter the Name:")
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="delete from admin where user_name='{1}'".format(user_name)
        cur=self.con.cursor()
        r=cur.execute(q)
        self.con.commit()
        if(r!=0):
            print("Data Deleted...")
        else:
            print("Data invalid...")
            
    def print(self):
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="select * from admin"
        cur=self.con.cursor()
        cur.execute(q)
        r=cur.fetchall()
        print("user_name\tpassword\tphone_no")
        for i in r:
            for j in i:
                print(j,end="")
            print()
        self.con.close()
            
class Product:
    def insert1(self):
       self.product_id=int(input("Enter the Id:"))
       self.product_name=input("Enter the Product Name:")
       self.product_color=input("Enter the Product Color:")
       self.features=input("Enter the Features:")
       self.cost=int(input("Enter the Product Cost:"))
       self.offer=int(input("Enter the Offer details:"))
       self.emi_info=input("Enter the EMI info:")
       self.delivery_cost=input("Enter the Delivery Cost:")
       self.quantity=int(input("Enter the Quantity:"))
       self.rating=int(input("Enter the Rating:"))
       self.review=input("Enter the Review:")
       self.con=connect(host="localhost",user="root",password="",database="product_management")
       q="insert into product_info values({0},'{1}','{2}','{3}',{4},{5},'{6}','{7}',{8},{9},'{10}')".format(product_id,product_name,product_color,features,cost,offer,emi_info,delivery_cost,quantity,rating,review)
       cur=self.con.cursor()
       cur.execute(q)
       self.con.commit()
       self.con.close()
       print("Data Saved...")
       
    def update1(self):
        self.product_id=int(input("Enter the ID:"))
        self.cost=input("Enter the Cost:")
        self.emi_info=input("Enter the EMI info:")
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="update product_info set cost='{0}' and emi_info='{1}' where product_id={2}".format(cost,emi_info,product_id)
        cur=self.con.cursor()
        r=cur.execute(q)
        self.con.commit()
        if(r!=0):
            print("Data Updated...")
        else:
            print("Data invalid...")
            
    def delete1(self):
        self.product_id=int(input("Enter the Product ID:"))
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="delete from product_info where product_id={0}".format(product_id)
        cur=self.con.cursor()
        r=cur.execute(q)
        self.con.commit()
        if(r!=0):
            print("Data Deleted...")
        else:
            print("Data invalid...")
            
    def print1(self):
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="select * from product_info"
        cur=self.con.cursor()
        cur.execute(q)
        r=cur.fetchall()
        print("product_id\tproduct_name\tproduct_color\tfeatures\tcost\toffer\temi_info\tdelivery_cost\tquantity\trating\treview")
        for i in r:
            for j in i:
                print(j,end="")
            print()
        self.con.close()  
       
       
class Customer:
    def insert2(self):
        self.name=input("Enter Your Name:")
        self.age=int(input("Enter the Age:"))
        self.gender=input("Enter the Gender:")
        self.mobile_no=int(input("Enter your Mobile Number:"))
        self.address=input("Enter the Address:")
        self.district=input("Enter your District:")
        self.pincode=int(input("Enter the pincode:"))
        self.state=input("Enter the State:")
        self.product_name=input("Enter the product name:")
        self.order_date=input("Enter the Order Date:")
        self.payment_method=input("Enter the Payment Method:")
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="insert into customer_info values('{0}',{1},'{2}',{3},'{4}','{5}',{6},'{7}','{8}','{9}','{10}')".format(name,age,gender,mobile_no,address,district,pincode,state,product_name,order_date,payment_method)
        cur=self.con.cursor()
        cur.execute(q)
        self.con.commit()
        self.con.close()
        print("Data Saved...")
        
    def update2(self):
        self.name=(input("Enter the Name:"))
        self.mobile_no=int(input("Enter your Mobile No:"))
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="update customer_info set mobile_no={0} where name='{1}'".format(cost,emi_info,product_id)
        cur=self.con.cursor()
        r=cur.execute(q)
        self.con.commit()
        if(r!=0):
            print("Data Updated...")
        else:
            print("Data invalid...")
            
    def delete2(self):
        self.name=input("Enter the Name:")
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="delete from customer_info where product_id='{0}'".format(product_id)
        cur=self.con.cursor()
        r=cur.execute(q)
        self.con.commit()
        if(r!=0):
            print("Data Deleted...")
        else:
            print("Data invalid...")
            
    def print2(self):
        self.con=connect(host="localhost",user="root",password="",database="product_management")
        q="select * from customer_info"
        cur=self.con.cursor()
        cur.execute(q)
        r=cur.fetchall()
        print("name\tage\tgender\tmobile_no\taddress\tdistrict\tpincode\tstate\tproduct_name\torder_date\tpayment_method")
        for i in r:
            for j in i:
                print(j,end="")
            print()
        self.con.close()  
        

ch=int(input("1.Admin\n2.Product Info\n3.Customer Info\nSelect any 1:")) 
if(ch==1):
    a=Admin()
    choice=int(input("1.insert\n2.update\n3.delete\n4.print\nSelect any 1:"))
    if(choice==1):
        a.insert()
    elif(choice==2):
        a.update()
    elif(choice==3):
        a.delete()
    elif(choice==4):
        a.print()
    else:
        print("Invalid Choice...")
        
elif(ch==2):
    b=Product()
    choice=int(input("1.insert\n2.update\n3.delete\n4.print\nSelect any 1:"))
    if(choice==1):
        b.insert1()
    elif(choice==2):
        b.update1()
    elif(choice==3):
        b.delete1()
    elif(choice==4):
        b.print1()
    else:
        print("Invalid Choice...")

elif(ch==3):
    c=Customer()
    choice=int(input("1.insert2\n2.update2\n3.delete2\n4.print2\nSelect any 1:"))
    if(choice==1):
        c.insert2()
    elif(choice==2):
        c.update2()
    elif(choice==3):
        c.delete2()
    elif(choice==4):
        c.print2()
    else:
        print("Invalid Choice...")
    
else:
    print("Ivalid Choice:")