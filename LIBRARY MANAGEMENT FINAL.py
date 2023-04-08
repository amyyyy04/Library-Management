#This is the source code for library management system
#This program makes use of python interpreter along with mysql and text & binary files
#Implementation of Library Management System.

print("❋❃❋❃❋❃❋WELCOME TO SAMAMSO LIBRARY MANAGEMENT SYSTEM̳!̳❋❃❋❃❋❃❋")
print("➭Press 1 if you are already a member.")
print("➭Press 2 if you are a newcomer.")
choice = int(input("Enter your choice (1 OR 2): "))


def displaybooks():    
    #first showing the menu to users.
    print("❋❃❋❃❋ Please select one genre from the following ❋❃❋❃❋")
    print("1-Horror")
    print("2-Fantasy")
    print("3- Biography & Autobiography")
    print("4-Humor")
    print("5-Sci-fi")
    choice=int(input("Enter Your Choice: "))
    #Prints the content of files of different genres
                
    if choice==1:
        f=open("Horror.txt","r")
        print(f.read())
    if choice==2:
        f=open("Fantasy.txt","r")
        print(f.read())
    if choice==3:
        f=open("bio.txt","r")
        print(f.read())
    if choice==4:
        f=open("Humor.txt","r")
        print(f.read())
    if choice==5:
        f=open("scifi.txt","r")
        print(f.read())

if choice ==1:
    login = True
    while login==True:
        import pickle
        Name =input("Enter your Registered Name: ")
        Pw=input("Enter Registered Password: ")
        f=open("user data.dat",'rb')
    #Entry will be granted only if the user enters correct name and password
    #using try & EOFError block reduces the chances of runtime exceptions.   
        try:
            while True:
                entry= pickle.load(f)
                if entry['name']== Name:
                    if entry['password']==Pw:
                        print(" Login successful! ")
                        login = False
    #User details have already been entered in a dictionary.
    #User details are the same as entered upon the time of membership.
                        
        except EOFError:
            if login==True:
                print("Name or password is wrong. Please check again.")
                f.close()
            else:
                f.close()
    while True:
        
        print("---:Browse our Menu:---")
        print("1 - Display Books")
        print("2 - Issue Book")
        print("3 - Return Book")
        print("4 - Donate Books") 
        print("5 - Show my book record")
        print("6 - Logout")
        print()
        print()
        ch=int(input("Enter your Choice: "))     
       
        if ch==1:
            displaybooks()
            print()
                                              
        
        if ch==2:
             
            def issuebook(Name):
                Date=input("Enter date of issue:") 
                import mysql.connector as ms
                mydb=ms.connect(host='localhost',user='root',passwd='Samridhi@123',database='library')
                mycursor=mydb.cursor()
                mycursor.execute('show tables')
                l=[]
                for x in mycursor:
                    l.append(x)
                #list will contain contents or rows of show tables in form of tuples                
            
                if (Name,) in l:
                    import mysql.connector as ms
                    mydb=ms.connect(host='localhost',user='root',passwd='Samridhi@123',database='library')
                    mycursor=mydb.cursor()
                    mycursor.execute('INSERT INTO '+Name+" VALUES(\'"+Bookname+"\','Issued',\'"+Date+"\')")
                    mydb.commit()
                #writing data into user table by using INSERT clause
                    print("Book issued successfully")
                else:
                    print("Record not found. Please enter the correct registered name.",sep='...')
                return
            Name=input("Enter Your Name (In Small Letters)")
            Bookname=input("Enter Book to be Issued:")
            genre=input("Enter Genre")
            f=open(genre+".txt",'r')
            #Opening book of required genre using string concatenation
            if Bookname in (f.read()):                
                issuebook(Name)
            else:
                print("This book is not available in the library.")
            print()
         
        if ch == 3:
            
            def returnbook():
                Name=input("Enter Your Name: ")
                bookname=input("Enter Book to be Returned")
                import mysql.connector as ms
                mydb=ms.connect(host='localhost',user='root',passwd='dreamcometrue',database='library')
                cursor=mydb.cursor()
                cursor.execute("UPDATE "+Name+" SET status='returned' WHERE Bookname = \'"+bookname+"\'")
            #Updating the user table
                mydb.commit()
                mydb.close()
                print("Book returned successfully!")
                print("Thank You for returning book on time!")
                print()                      
                return
            returnbook()

        
        if ch==4:
            
            import donation
            #importing module namely "donation"        
        
        if ch==5:
            
            def recshow():
                import mysql.connector as ms
                Name=input("Enter your name (in small letters)")
                mydb=ms.connect(host='localhost',user='root',passwd='dreamcometrue',database='library')
                cursor=mydb.cursor()
                cursor.execute('SELECT * FROM '+Name)
            # This fetches all the contents of the table
                myrec=cursor.fetchall()
                print("This is the detailed record of", Name,":-")
                for x in myrec:
                    print(x[0],x[1],x[2],sep="---")
                return
            
            recshow()
            print()
            
        
         
        if ch==6:
            
            print("        Thank you for using Samamso Library! We hope you had a good time!")
            print("                    Eagerly waiting for your next visit!")
            print("-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃-❃--❃-❃-❃-❃-  ")
            break
        #breaking the 'while' loop upon Logging OUT. 
        
#Creating account
elif choice==2:
    print("1 - Display Books")
    print("2 - Create membership account")
    ch1=int(input("Enter your choice:"))
    if ch1==1:
        displaybooks()
        
    if ch1==2:
        import pickle
        user_data={}
        file=open("user data.dat","ab")
        name=input("Enter Your Name: ")
        age=int(input("Enter Your Age: "))
        gender=input("Enter Your Gender: ")
        phno=int(input("Enter 10-Digit Phone Number: "))
        pwd=input("Create a password: ")
    #Writing data into dictionary 
        user_data['name']=name
        user_data['age']=age
        user_data['gender']=gender
        user_data['password']=pwd
        user_data['phone']=phno
        
    #writing user's data into the file
        pickle.dump(user_data,file)
        print("                Account Created Successfully!")
        print("❋❃❋❃❋Thank you for creating account in Samamso Library!❋❃❋❃❋")
        file.close()
        def membertable():
            #creating table for data entry
            import mysql.connector as ms
            mydb=ms.connect(host= 'localhost', user='root', passwd='dreamcometrue', database='library')
            mycursor=mydb.cursor()
            mycursor.execute('create table '+name+' ( Bookname varchar(30), Status varchar(10), Date_of_Issue varchar(10) PRIMARY KEY)')                     
            mydb.commit()
            return
        membertable()
#END OF PROGRAM
        
