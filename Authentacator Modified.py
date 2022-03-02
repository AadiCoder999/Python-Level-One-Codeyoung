username = 1234
password = 4321

print("Please Sign In To Continue On The Portal")
userusername = int(input("Enter Your Username: "))

while(username != userusername):
    print("Your username was incorrect!")
    userusername = int(input("Try Entering Your Username Again: "))
    
if(username == userusername):
    print("Your username was correct!")
userpassword = int(input("Enter Your Password: "))

while(password != userpassword):
    print("Your password was incorrect!")
    userpassword = int(input("Try Entering Your Password Again: "))

if(username == userusername and password == userpassword):

    print("Thank You For Signing In!")
    C = int(input("Please Enter 1 If You Want To Change Your Password\nPlease Enter 2 If You Want To Keep Your Password "))

    if(C == 1):
        print("Please Enter A New Password That Only Has Numbers.")
        newusername = int(input("Enter Your New Username: "))
        newpassword = int(input("Enter Your New Password: "))
        print("Your Username And Password Has Been Changed!")
    if(C == 2):
        print("Your Username And Password Will Not Be Changed.")
    if(C >= 3 or C<= 0):
        print("Sorry, But That Was Not One Of The Options. Have A Great Day!")


    if(C == 1 or C == 2):
        Q = int(input("We Have Prepared A Short List Of 6 Questions For You.\nEnter 1 If You Want To Do Them\nEnter 2 If You Don't Want To Do Them "))

        if(Q == 1):
            a = input("Ok, The First Question Is:\nWhat Is Your Favorite Color? ")
            b = input("Ok, The Second Question Is:\nWhat Is Your Favorite Animal? ")
            c = input("Ok, The Third Question Is:\nWhat Is Your Favorite Number? ")
            d = input("Ok, The Fourth Question Is:\nWhat Is Your Favorite Book? ")
            e = input("Ok, The Fifth Question Is:\nWhat Is Your Favorite TV Show? ")
            f = input("Ok, The Sixth Question Is:\nWhat Is Your Favorite Video Game? ")
            print("")
            print("You Selected:")
            print("Favorite Color:",a)
            print("Favorite Animal:",b)
            print("Favorite Number:",c)
            print("Favorite Book:",d)
            print("Favorite TV Show:",e)
            print("Favorite Video Game:",f)
            print("")
            print("Thank Your For Taking The Short List Of 6 Questions! Have A Great Day!")

        if(Q == 2):
            print("Ok, Have A Great Day!")

        if(Q >= 3 or Q<= 0):
            print("Sorry, But That Was Not One Of The Options. Have A Great Day!")
            
