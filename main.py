import mysql.connector as mysql
db = mysql.connect(host = "localhost", user = "root", passwd = "root", database="library")
mycursor = db.cursor()

import smtplib
def issuemail(nm,bno,dt,ml):
    gmail_user = “palak2609s@gmail.com”
    gmail_app_password = ''abc123” 
    sent_from = gmail_user
    sent_to = [ml]
    sent_subject = "LIBRARY"
    sent_body = "Dear "+ nm + "\n book no "+str( bno)+" is issued to you on "+str(dt)+"\n "
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
  try:
       server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def submitmail(nm,bno,dt,ml):
    gmail_user = “palak2609s@gmail.com”
    gmail_app_password = “abc123”
    sent_from = gmail_user
    sent_to = [ml]
    sent_subject = "LIBRARY"
    sent_body = "Dear "+ nm + "\n book no "+str( bno)+" is submitted by you on "+str(dt)+"\n "
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()
        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)


def addbook():
    bcode= int(input("Enter book code :"))
    bname= (input("Enter book name : "))
    category= (input("Enter category : "))
    language=(input("Enter book language : "))
    bprice= float(input("Enter book price : "))
    qty= int(input("Enter quantity : "))
    data=(bcode,bname,category,language,bprice,qty)
    query=("insert into Books values({},'{}','{}','{}',{},{})".format(bcode,bname,category,language,bprice,qty))
    mycursor.execute(query)
    db.commit()
    print("DATA ENTERED SUCCESSFULLY!!!")
    main()

def issueb():
    name= input("Enter name : ")
    regno=input("Enter registration no. : ")
    bcode=input("Enter book code : ")
    issuedate= input("Enter date : ")
    email=input("Enter email id : ")
    issue=("insert into issue values('{}',{},{},'{}','{}')".format(name,regno,bcode,issuedate,email))
    data= (name,regno,bcode,issuedate,email)
    mycursor = db.cursor()
    mycursor.execute(issue)
    db.commit()
    print("BOOK ISSUED TO ",name)
    
    issuemail(name,bcode,issuedate,email)
    print("book is issued")
    bookup(bcode,-1)
    
    def submitb():
    name= input("Enter your name : ")
    regno=input("Enter your registration no. : ")
    bcode=input("Enter book code : ")
    submitdate= input("Enter date : ")
    email=input("Enter email id : ")
    submit=("insert into submit values('{}',{},{},'{}','{}')".format(name,regno,bcode,submitdate,email))
    data = (name,regno,bcode,submitdate,email)
    mycursor.execute(submit)
    db.commit()
    print("BOOK SUBMITTED BY ",name)

    submitmail(name,bcode,submitdate,email)
    print("book is submitted")
    bookup(bcode,1)
                
           
def delbook():
    bcode= int(input("Enter book code of the book which has to be deleted : "))
    d=("delete from books where bcode={}".format(bcode))
    mycursor.execute(d)
    db.commit()
    print("DATA DELETED SUCCESSFULLY")
    main()


def displaybooks():
    display="select * from books"
    mycursor= db.cursor()
    mycursor.execute(display)
    result = mycursor.fetchall()
    for i in result:    
        print("BOOK NAME : " , i[1])
        print("BOOK CODE : " , i[0])
    main()


def bookup(bcode,u):
    a=("select Qty from books where bcode = {}".format(bcode))
    data=(bcode,)
    #mycursor= db.cursor()
    mycursor.execute(a)
    result = mycursor.fetchone()
    t= result[0]+u
    sql= ("update books set Qty={} where bcode={}".format(t,bcode))
    #d=(t,bcode)
    mycursor.execute(sql)
    db.commit()
    main()


def main():
    print("")
    print("************************     LIBRARY MANAGEMENT    **************************")
    print("")
    print("1. ADD BOOKS ")
    print("2. ISSUE BOOKS ")
    print("3. SUBMIT BOOKS ")
    print("4. DELETE BOOKS ")
    print("5. DISPLAY BOOKS ")
    print("6. EXIT")
    ch=int(input("Enter the choice number: "))
    while True: 
        if (ch==1):
            addbook()
        elif (ch==2):
            issueb()
        elif ch==3 :
            submitb()
        elif ch==4:
            delbook()
        elif ch==5:
            displaybooks()
        elif ch==6:
            break
        else:
            print("wrong choice")
        main()


def pswd():
    ps=input("Enter the password: ")
    if ps=="1":
        main()
    else:
        print("Wrong password")
pswd()
