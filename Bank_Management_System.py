import sys
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='tiger',database='Bank_Management')

def open_account():
    while True:
        n=input("Enter The Name:")
        ac=input("Enter The Account No:")
        db=input("Enter The Date of Birth:")
        add=input("Enter The Address:")
        cn=input("Enter The Contact No.:")
        ob=int(input("Enter The Opening Balance:"))
        data1=(n,ac,db,add,cn,ob)
        data2=(n,ac,ob)
        sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
        sql2=('insert into amount values(%s,%s,%s)')
        x=mydb.cursor()
        x.execute(sql1,data1)
        x.execute(sql2,data2)
        mydb.commit()
        print("Data Entered Seccessfully...")
        ch=input("Do you want to enter more records(Y/N):")
        if ch=='N' or ch=='n':
            break
    main()
    
    
def deposit_amount():
    amount=int(input("Enter The Amount You Want To Deposit:"))
    ac=input("Enter The Account No:")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update amount set balance=%s where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    print("Amount Credited...")
    main()
    

def withdraw_amount():
    #ac=input("Enter The Account No:")
    #a='select balance from amount where AccNo=%s'
    #data=(ac,)
    #x=mydb.cursor()
    #x.execute(a,data)
    #result=x.fetchone()
    #t=result[0]-amount
    #sql=('update amount set balance=%s where AccNo=%s')
    #d=(t,ac)
    #x.execute(sql,d)
    #mydb.commit()
    #main() 
    while True:
        cmd='select * from bank_management.amount'
        x=mydb.cursor()
        x.execute(cmd)
        print("Please Note That The Money Can Only Be Debited If Minimun Balance Of Rs 5000 Exists")
        acc=input("Enter The Account No:")
        for i in x:
            i=list(i)
            if i[1]==acc:
                Amt=float(input("Enter the Amount to be Withdraw:"))
                if i[2]-Amt>=5000:
                    i[2]-=Amt
                    cmd="UPDATE AMOUNT SET BALANCE=%s WHERE ACCNO=%s"
                    val=(i[2],i[1])
                    x.execute(cmd,val)
                    mydb.commit()
                    print("Amount Debited...")
                    break
                else:
                    print("There Must Be Minimun Balance Of Rs 5000")
                    break
        ch=input("Do You Want To Perform More WithDraw Operation(Y/N):")
        if ch=='N' or ch=='n':
            break
    main()
    
  
def balance_enquiry():
    while True:
        ac=input("Enter The Account No.:")
        a='select * from amount where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()
        print("Balance For Account No. {} is Rs {}.".format(ac,result[-1]))
        ch=input("Do You Want To Perform More Balance Enquiry Operation(Y/N):")
        if ch=='N' or ch=='n':
            break
    main()
    
    
def customer_details():
    while True:
        ac=input("Enter The Account No.:")
        a='select * from account where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchone()
        for i in result:
            print(i)
        ch=input("Do You Want To Get More Customer Details(Y/N):")
        if ch=='N' or ch=='n':
            break
    main()
    
    
def close_an_account():
    ac=input("Enter The Account No.:")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2,data)
    mydb.commit()
    print("Account Closed...")
    main()


def main():
    print('''   
    1. OPEN NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE AN ACCOUNT
    7. Exit
    ''')
    choice=input("Enter The Task You Want To Perform:")
    if (choice=='1'):
        open_account()
    elif (choice=='2'):
        deposit_amount()
    elif (choice=='3'):
        withdraw_amount()
    elif (choice=='4'):
        balance_enquiry()
    elif (choice=='5'):
        customer_details()
    elif (choice=='6'):
        close_an_account()
    elif (choice=='7'):
        print("Exiting...")
        sys.exit()
    else:
        print("INVAIL CHOICE")
main()