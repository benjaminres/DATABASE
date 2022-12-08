print("@@@@@@@@@@@@@@@@@@@@")
print("@@@@@          @@@@@")
print("@@@@@           @@@@@")
print("@@@@@            @@@@@")
print("@@@@@              @@@@@")
print("@@@@@               @@@@@")
print("@@@@@                @@@@@")
print("@@@@@                  @@@@@")
print("@@@@@                    @@@@@")
print("@@@@@                     @@@@@")
print("@@@@@                      @@@@")
print("@@@@@                       @@@@")
print("@@@@@                        @@@@")
print("@@@@@                        @@@@@")
print("@@@@@                        @@@@@")
print("@@@@@                       @@@@@")
print("@@@@@                      @@@@@")
print("@@@@@                     @@@@@")
print("@@@@@                   @@@@@")
print("@@@@@                 @@@@@")
print("@@@@@                @@@@@")
print("@@@@@              @@@@@")
print("@@@@@            @@@@@")
print("@@@@@          @@@@@")
print("@@@@@        @@@@@")
print("@@@@@@@@@@@@@@@@@")

print("DataBase creator Benjamin Zaghloul")
print("Contact me here benjaminkimble77@gmail.com ")
#Temp data base for storage
LIST = ["WPL COMPUTER" , "TempFile" , "T3" , "t4"]
x = input("PLease enter your password \n")
if x == "password":
    print("Welcome to the Database")
    y = input("Who would you like to find? Press 1 if you want to list all users. \n ")
    if y == "WPL COMPUTER":
        print("IP 209.212.23.47 Computer name waynead\461libref")
    if  y == "Tempfile":
        print("This file is for testing porpouses only :(")
    if y == "1":
        print (LIST)
        y = input("Who would you like to find? Press 1 if you want to list all users.")
        if y == "WPL COMPUTER":
            print("IP 209.212.23.47 Computer name waynead\461libref")
    if y == "1":
        print (LIST)
else:
    print("Access Denied, please try again")
    x = input("PLease re-enter your password")
    if x == "password":
        print("Welcome to the Database")
        x = input("Who would you like to find? Press 1 if you want to list all users. \n")
        x = input("Who would you like to find? Press 1 if you want to list all users. \n ")
    if x == "WPL COMPUTER":
        print("IP 209.212.23.47 Computer name waynead\461libref \n")
    if x == "1":
        print (LIST)
        x = input("Who would you like to find? Press 1 if you want to list all users.")
        if x == "WPL COMPUTER":
            print("IP 209.212.23.47 Computer name waynead\461libref")
        if x == "1":
            print (LIST)
           if  y == "Tempfile":
        print("This file is for testing porpouses only :(")
    else:
        print ("The DataBase Is Now Locked")
print ("Contact me to add things to the DataBase or if bugs or logical errors occur")
