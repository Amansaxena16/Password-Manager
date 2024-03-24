mode = input("Would you like to add a new password or view another(View/Add) - ").lower()

def view():
    file = open("Password.txt","r")
    for line in file.readlines():
        data = line.rstrip()
        user, password = data.split("|")
        print("User Name = ",user, '|',"password = ",password)
    file.close()

def add():
    email = input("Enter Your Email!! ")
    password = input("Enter your Password!! ")

    file = open('Password.txt','a')
    file.write(email + "|" + password + "\n")
    file.close()

while(True):
    if(mode == "view"):
        view()
        break

    elif(mode == "add"):
        add()
        more = input("Want to Add more Emais(Yes/No) ").lower()
        if(more == "no"):
            break
        else:
            continue

    else:
        print("Invalid Input!!")
        continue




