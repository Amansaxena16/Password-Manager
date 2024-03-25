Description:
The Secure Password Manager is a Python-based application that allows users to securely store and manage their passwords. It utilizes the Fernet encryption algorithm from the cryptography library to encrypt and decrypt passwords, ensuring data security. The user can choose to either view existing passwords or add new ones. Additionally, the application provides the flexibility to continue adding passwords or exit after each addition. The encryption key is securely stored in a separate file (key.key) for added security.

Instructions:

.Run the Python script.
.Choose between viewing existing passwords or adding new ones.
.If adding passwords, enter the email and password details.
.Optionally, continue adding more passwords or exit the application.
.Passwords are securely encrypted using the Fernet algorithm.

Note:
Ensure to keep the key.key file secure, as it contains the encryption key necessary for decrypting passwords. Back up this file to prevent data loss.