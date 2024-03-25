# Fernet --> Fernet is a symmetric encryption algorithm provided by the cryptography library in Python. It requires a secret key to encrypt and decrypt data.
from cryptography.fernet import Fernet

# Reading the Key File
def load_key():
    file = open('key.key','rb') 
    key = file.read() # Here reading the file in read binary form and storing in key variable
    file.close()
    return key

key = load_key() # function call and storing data
fer = Fernet(key)

# Asking to View or to Add the Password
mode = input("Would you like to add a new password or view another(View/Add) - ").lower()

# View Function to see the passwords
def view():
    file = open("Password.txt","r")
    for line in file.readlines():
        data = line.rstrip()  # Removing all the white spacing and newline with rstrip()
        user, password = data.split("|")  #spliting the username and password will split()
        print("User Name = ",user, '|',"password = ",fer.decrypt(password.encode()).decode()) # Decrypting the data
    file.close()

# Add Function to add all the password into the file
def add():
    email = input("Enter Your Email!! ") # taking Input from user
    password = input("Enter your Password!! ") # taking Input from user

    file = open('Password.txt','a') # Here creating a pass.txt file in append mode
    file.write(email + "|" + fer.encrypt(password.encode()).decode() + "\n") # writing the data into the file in encryted form using Fernet
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



