from cryptography.fernet import Fernet

# Reading the Key File
def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

key = load_key()

fer = Fernet(key)

mode = input("Would you like to add a new password or view another(View/Add) - ").lower()

def view():
    file = open("Password.txt","r")
    for line in file.readlines():
        data = line.rstrip()
        user, password = data.split("|")
        print("User Name = ",user, '|',"password = ",fer.decrypt(password.encode()).decode())
    file.close()

def add():
    email = input("Enter Your Email!! ")
    password = input("Enter your Password!! ")

    file = open('Password.txt','a')
    file.write(email + "|" + fer.encrypt(password.encode()).decode() + "\n")
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


# --> This function() is used to create the Key for encrytion!! 
# def write_key():
#     key = Fernet.generate_key()
#     key_file =  open('key.key','wb')  
#     key_file.write(key)
#     key_file.close()



