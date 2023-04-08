#Module for donating books
#This module would be imported to the main program via the 'import' function
print ("❋❃❋❃❋WELCOME TO THE DONATIONS SECTION!❋❃❋❃❋")
print("We have the following genres for our Public Library:")
print("                    ➭Horror")
print("                    ➭Fantasy")
print("                    ➭Biography & Autobiography")
print("                    ➭Humor")
print("                    ➭Sci-fi")
print("-----Please fill the following details to donate books-----")
def donate():
    str1=''
    ans='yes'
    while ans=='yes':
        bname=input("Enter book name: ")
        qty=int(input("Enter quantity of the book: "))
        genre=input("Book belongs to which genre? ")
        ans=input("Do you want to donate more books?(yes/no) ")
        #To write the data into file of desired genre
        f=open(genre+".txt","a")
        f.write('\n')
        f.write(bname)
        
        f.close()
        #Closing the file is important so as to prevent unwanted loss of data
    else:
        print("Thank You for donating books to the Public Library!")
donate()   
#constant values
Libowner1='Somya Sirmour'
Libowner2='Samridhi Dewangan'
Libowner3='Ameetaa Sengupta'





   







