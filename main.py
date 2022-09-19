
import secrets 
import string
import bcrypt

def generate_password():
    '''generates random uppercase + lowercase + 8 numbers followed by a punctuation
    character password'''
    password = None
    while len(str(password)) != 11:
        password = ''.join(secrets.choice(string.ascii_lowercase) for i in range(2))
        password = password + ''.join(secrets.choice(string.digits) for i in range(8))
        password = password + ''.join(secrets.choice(string.punctuation) for i in range(1))
        password = password.capitalize()
    return password

def store_hashed_pw(user, hashed_pw):
       
    with open(r'C:\Users\Public\Hashed Passwords\Hashed.txt', 'a+') as f:
        #moving to start of file
        f.seek(0)
        #reading file
        data = f.read(100)
        #adds new line if file has entries
        if len(data) > 0:
            f.write("\n")
        f.write(f"{user}: {hashed_pw}")


#Hashing and salting password
def hash_password(plaintext_password):
    #Hash the password
    #salt gets saved to password itself with bcrypt
    #gensalt(slowness_level), slower is generally better when working with hashing
    #this makes it more difficult to brute force the password
    
    return bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt(8))

def authenticate(plaintext_password, hashed_password):
    '''checks the hashed password taking the plaintext_password and the hashed password 
    as arguments'''
    #checking the hashed password, bcrypt has already saved the salt to the hash itself
    return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_password)



# user = input('Enter username:')
# password = generate_password()
# print(f"Username: {user} \nPassword: {password}")

# hash = hash_password(password)
# store_hashed_pw(user, hash)




# password = generate_password()
# print(password)

# hashed = hash_password(password)
# print(hashed)

# print(authenticate(password, hashed))












    
    
    

    