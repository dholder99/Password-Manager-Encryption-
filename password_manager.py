from cryptography.fernet import Fernet

# generate a new encryption key
key = Fernet.generate_key()

# write the key to a file
with open("key.txt", "wb") as key_file:
    key_file.write(key)

# load the key from the file
with open("key.txt", "rb") as key_file:
    key = key_file.read()

# create a new Fernet object using the key
fernet = Fernet(key)

# get a password from the user
password = input("Enter a password: ")

# encrypt the password using the Fernet object
encrypted_password = fernet.encrypt(password.encode())

# write the encrypted password to a file
with open("password.txt", "wb") as password_file:
    password_file.write(encrypted_password)

# load the encrypted password from the file
with open("password.txt", "rb") as password_file:
    encrypted_password = password_file.read()

# decrypt the password using the Fernet object
decrypted_password = fernet.decrypt(encrypted_password)

# print the decrypted password
print("Decrypted password:", decrypted_password.decode())