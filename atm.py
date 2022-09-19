import mysql.connector
yukidb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yuki$0623@",
    database="KUY_BANk"
)
print(yukidb)

mycursor=yukidb.cursor()
#KUY BANK

def kuy_reg(your_name,login_id,password,pin,amount):
    login="insert into data(your_name,login_id,password,pin,amount) values (%s,%s,%s,%s,%s)"
    user_login=(your_name,login_id,password,pin,amount)
    mycursor.execute(login,user_login)
    yukidb.commit()
    print("account created succesfully")
    
print("welcome kuy bank")
kuy_bank=int(input("1.register and  2.login:"))
if kuy_bank==1:
    print("You Pay Minimum 500 to create acccount:")
    amount=int(input("Your amount:"))
    if amount>=500:
     your_name=input("enter your name:")
     login_id=int(input("enter your id:"))
     password=input("enter your password:")
     pin=int(input("enter your pin:"))
     kuy_reg(your_name,login_id,password,pin,amount)
    else:
        print("account does not create")
   
elif kuy_bank==2:
  num=input("enter pin:")
  mycursor=yukidb.cursor()
  mycursor.execute("SELECT * FROM kuy_bank.data where pin='%s'"%(num))
  row=mycursor.fetchone()
  if mycursor.rowcount==1:
            print("login successfull")
            mycursor.execute("SELECT your_name FROM kuy_bank.data where pin='%s'"%(num))
            for your_name in mycursor:
                    print(your_name)
            youwant=int(input("1.withdraw 2.deposit 3.balance_enquiry 4.exit:"))
            if youwant==1:
                withdraw=int(input("How much:"))
                mycursor.execute("SELECT amount FROM kuy_bank.data where pin='%s'"%(num))
                col=mycursor.fetchone()
                b=list(col)
                for i in b:
                   a = (int(i))
                   c= a-withdraw
                mycursor.execute("UPDATE data SET amount='%s' where pin='%s'" %(c,num))
                print("amount withdraw successfull")
                mycursor.execute("SELECT amount FROM kuy_bank.data where pin='%s'"%(num))
                for amount in mycursor:
                    print(amount)
            elif youwant==2:
                deposite=int(input("How much:"))
                mycursor.execute("SELECT amount FROM kuy_bank.data where pin='%s'"%(num))
                col=mycursor.fetchone()
                b=list(col)
                for i in b:
                   a=(int(i))
                   total=a+deposite
                mycursor.execute("UPDATE data SET amount='%s' where pin='%s'"%(total,num))
                print("deposite successfully")
                mycursor.execute("SELECT amount FROM kuy_bank.data where pin='%s'"%(num))
                for amount in mycursor:
                    print(amount)
            elif youwant==3:
                mycursor.execute("SELECT amount FROM kuy_bank.data where pin='%s'"%(num))
                for amount in mycursor:
                    print(amount)
            elif youwant==4:
                print("your account exits") 
                exit(0)         
            
  else:
             print("pin incorrect")
            
else:
               print("press 1.register or 2.login ")
yukidb.commit()    


