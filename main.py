
import secrets 
import string
import bcrypt
import json
#need to wait to do check availabilty, need to first store user hashed passwords
#in a more efficient way using json and dictionary k,v pairs
def username_taken(user):
    '''Check if username is taken, returns True if username already 
    located in database'''
    with open(r'C:\Users\Public\Hashed Passwords\Hashed.txt', 'r') as file:
    #moving to start of file
        file.seek(0)
        data = json.loads(file.read())
        for username in data:
            if user.lower() == username.lower():
                return True            
    

def create_username():
    print('Please enter a username.\nValid username contains only letters \nand numbers, and no spaces.')
    valid = False
    invalid = False
    user = input('Enter username:')
    user = str(user) 
    while valid == False:
        if len(user) > 10 or len(user) < 3:
            #check username length
            print('Username size incorrect.\nSize should be more than 3 characters \nand less than 10 characters. \nPlease try again.')
            user = input('Enter username:')
            continue
        for character in user:
            #check if username has invalid characters
            if character not in string.ascii_letters + string.digits:
                invalid = True
                #conditional for following loop to use    
        
        if invalid == True:
            print('Invalid username, please try again.')
            invalid = False
            user = input('Enter username:')
            continue

        if username_taken(user) == True:
            print('Username already taken, please try again.')
            user = input('Enter username:')
            continue
        
        else:
            #generating new password
            password = generate_password()
            print(f"Username is available.\nYour username is: {user}\nPassword is: {password}")
            #store username and password in file
            password = hash_password(password)
            store_user_and_hashed_pw(user, password)

            valid = True
            
        
        
        # for character in user:
        #     if character not in string.ascii_letters + string.digits:
        #         invalid = True
        #         continue

        # if invalid == True:
        #     print('Invalid username, please try again.')
        #     user = input('Enter username:')
        #     continue
            
                
                
            
        # else:
        #     Valid = True
                

                #for character causing each character to return error,
                #need to find a way to stop as soon as it finds a single
                #error


            
        
                
                

        
    return 
        



    

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

def store_user_and_hashed_pw(user, hashed_pw):
       #ADD USER STORE TO THIS, CREATE LINES FOR USER/PASS
       #USE JSON FOR STORING DICTS
    hashed_pw = hashed_pw.decode('utf-8')
    pw_dict = {user:hashed_pw}

    #a+
    with open(r'C:\Users\Public\Hashed Passwords\Hashed.txt', 'r+') as file:
        file.seek(0)
        data = file.read(1)
        if len(data) < 1:
            #decoding hashed pw for json to write it
            file.write(json.dumps(pw_dict))

        else:
            file.seek(0)
            data = file.read()
            #changing back into a dictionary
            data = json.loads(data)
            #adding new user/pass combo
            data[user] = hashed_pw
            #deleting previous list
            #if error occured between deletion and insertion feasibly there could be
            #a huge bug where all data on passwords gets lost without being replaced, so this
            #would not be a stable option for a server
            #add a password save backup before this step
            file.truncate(0)
            #moving back to start for no whitespace
            file.seek(0)
            file.write(json.dumps(data))

            
        



#Hashing and salting password
def hash_password(plaintext_password):
    #Hash the password
    #gensalt(slowness_level)
    
    return bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt(8))

def authenticate(plaintext_password, hashed_password):
    '''checks the hashed password taking the plaintext_password and the hashed password 
    as arguments'''
    #checking the hashed password, bcrypt has already saved the salt to the hash itself
    return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_password)

username = create_username()


# store_user_and_hashed_pw('jason', b'$2b$08$1uAGmTe2XDK/i75GZzjMS.dACbre19xy3707WDQ.UHy4W5dmGRSce' )


# user = input('Enter username:')
# password = generate_password()
# print(f"Username: {user} \nPassword: {password}")

# hash = hash_password(password)
# store_hashed_pw(user, hash)













    
    
    

    