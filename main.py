
import secrets 
import string
import bcrypt
import json
#need to wait to do check availabilty, need to first store user hashed passwords
#in a more efficient way using json and dictionary k,v pairs
# def check_availability(user):
#     with open(r'C:\Users\Public\Hashed Passwords\Hashed.txt', 'r') as f:
#     #moving to start of file
#         f.seek(0)
#         #reading file
#         data = f.read(100)
#         #adds new line if file has entries
#         if len(data) > 0:
            
    

def create_username():
    print('Valid username contains only \nletters and numbers, and no spaces.')
    valid = False
    invalid = False
    count = 0
    user = input('Enter username:')
    user = str(user)
    char_list = list(user)
    while valid == False:
        print(len(user))
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
        
        
        else:
            valid = True
            print(invalid)
        
        
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


            
        
                
                

        
    return user
        



    

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
            file.truncate(0)
            #moving back to start for no whitespace
            file.seek(0)
            file.write(json.dumps(data))

            
        


    with open(r'C:\Users\Public\Hashed Passwords\Hashed.txt', 'a+') as file:
        #moving to start of file
        file.seek(0)
        #reading file
        data = file.read(100)
        #adds new line if file has entries
        # if len(data) > 0:
        #     file.write("\n")
        # file.write(f"{user}: {hashed_pw}")


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

# username = create_username()
# print(username)

store_user_and_hashed_pw('jason', b'$2b$08$1uAGmTe2XDK/i75GZzjMS.dACbre19xy3707WDQ.UHy4W5dmGRSce' )

# user = input('Enter username:')
# password = generate_password()
# print(f"Username: {user} \nPassword: {password}")

# hash = hash_password(password)
# store_hashed_pw(user, hash)













    
    
    

    