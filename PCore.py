
import secrets 
import string
import bcrypt
import json

#Parfait core code

def username_taken(user):
    '''Check if username is taken, returns True if username already 
    located in database'''
    with open(r'C:\Users\Public\Hashed Passwords\Hashed.txt', 'a+') as file:
    #moving to start of file
        file.seek(0)
        try:
            data = json.loads(file.read())
            for username in data:
                if user.lower() == username.lower():
                    return True     
        except:
            return   


def create_password(password):
    '''Password must conform to generated password standards, at least: one uppercase
     letter, one lowercase letter, 8 digits and one symbol, eg. Ab12345678!
     can contain more than one of each.'''
     #once done with create plassword feature, remove generate password addition
     #in create account function, and replace with create password function
     #generate password will be used solely for password recovery
    # print('Please create a password.\nMust contain one capital, one lowercase, 8 digits and one symbol')
    # password = input('Password: ')
    #print('Please create a new password.\nMust contain one capital, one lowercase,\n8 digits and one symbol')
    
    
    valid = False
    while valid == False:
        #flags for valid password
        invalid = True
        upper = False
        lower = False
        digits = False
        symbol = False
        count = 0


        
        #checking that the number of digits is at least 8
        for digit in password:
            if digit in string.digits:
                count += 1
                if count >= 8:
                    digits = True
                    # valid = True

        #checking for an uppercase character
        for upper_chars in password:
            if upper_chars in string.ascii_uppercase:
                upper = True

        #checking for a lowercase character
        for lowercase_chars in password:
            if lowercase_chars in string.ascii_lowercase:
                lower = True
        #checking for a symbol
        for symbols in password:
            if symbols in string.punctuation:
                symbol = True

        #if all flags are True allow password to continue to password matching
        if digits and symbol and lower and upper:
            invalid = False

        #if any flag is False restart the process
        if invalid:
            #send False back to handling application, password is invalid and must be retyped
            #to standards required
            return False

        else:
            #password is valid, send True to handling application
            #handling application will now need to process retyped_password()
            return True
        
        #password matching after inputting valid password
        # if not invalid:
        #     retyped_password(original_pass,retyped_pass)
            #print('Please re-enter same password.')
            #second_password = retyped_pass

            # if second_password == password:
            #     #print('Passwords matched\nAccount created.')
            #     return password
                

            # else:
            #     print('Passwords did not match\nPlease create a new password.')
            #     invalid = True
            #     continue

def retype_password(original_pass, retyped_pass):
    '''handling application will check original password against the retyped password
    this code will kick back True if passwords match, false if passwords do not match'''
    if original_pass == retyped_pass:
        return True

    else:
        return False

def validate_username(username):
    '''makes sure that username is valid based on this program's standards *contains only letters, numbers
    ,and no spaces. Returns True if valid, False if invalid.'''
    user = username
    valid = False
    
    while not valid:
        if len(user) > 10 or len(user) <3:
            return False
        if ' ' in user:
            return False
        for character in username:
            #check if username contains invalid characters
            if character not in string.ascii_letters + string.digits:
                return False
            else:
                valid = True
                return True


def account_creation(username,password):
    '''attempts to hash password and then store username+password in database, if this 
    process completes returns True, else returns False'''
    #store username and password in file
    try:
        password = hash_password(password)
        store_user_and_hashed_pw(username, password)
        return True
    except:
        return False

        
def generate_password():
    '''generates random uppercase + lowercase + 9 numbers followed by a punctuation
    character password'''
    password = None
    while len(str(password)) != 12:
        password = ''.join(secrets.choice(string.ascii_lowercase) for i in range(2))
        password = password + ''.join(secrets.choice(string.digits) for i in range(9))
        password = password + ''.join(secrets.choice(string.punctuation) for i in range(1))
        password = password.capitalize()
    return password

def store_user_and_hashed_pw(user, hashed_pw):
    '''stores username and hashed password in a text file as a dictionary'''
    user = user.lower()
    hashed_pw = hashed_pw.decode('utf-8')
    pw_dict = {user:hashed_pw}

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

def hash_password(plaintext_password):
    '''salts and hashes a plain text password'''
    #Hash the password
    #gensalt(slowness_level)
    return bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt(8))

def authenticate(plaintext_password, hashed_password):
    '''checks the hashed password taking the plaintext_password and the hashed password 
    as arguments'''

    #checking the hashed password, bcrypt has already saved the salt to the hash itself
    return bcrypt.checkpw(plaintext_password.encode('utf-8'), hashed_password)

def locate_hashed_pw(username):
    '''locates a username to verify it is in the database, if true
    sends back the hashed version of their password'''
    #if user or pass comes back incorrect, kick back False and throw up
    #error that user or pass is incorrect
    #place this function within authenticate function
    #locate user first, then go off of user for password
    with open(r'C:\Users\Public\Hashed Passwords\Hashed.txt', 'r') as file:
        user_located = False
        file.seek(0)
        data = json.loads(file.read())
        for user in data:
            if username.lower() == user.lower():
                user_located = True
            if user_located:
                return data[user].encode('utf-8')
        else:
            return False
            
def log_in(username, plaintext_password):
    '''verifies a username is valid, finds hashed password and then verifies
    against the plain text password entered'''
    #check if username matches reference DB and return hashed password
    credentials = locate_hashed_pw(username)
    if not credentials == False:
        #if username matches, authenticate password against hashed password
        #credentials now = True or False
        credentials =  authenticate(plaintext_password, credentials)
        #return True or False
        return credentials
    else:
        #return False
        return credentials


#######################MODULE TESTING PACKAGE####################################


def test_password_store(user, plaintext_password):
    '''function to store plaintext passwords FOR TEST ACCOUNTS ONLY'''
    pw_dict = {user:plaintext_password}

    with open(r'C:\Users\Public\PlainText Passwords\Test acct passwords.txt', 'r+') as file:
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
            data[user] = plaintext_password
            #deleting previous list
            #if error occured between deletion and insertion feasibly there could be
            #a huge bug where all data on passwords gets lost without being replaced, so this
            #would not be a stable option for a server
            #add a password save backup before this step
            file.truncate(0)
            #moving back to start for no whitespace
            file.seek(0)
            file.write(json.dumps(data))

def bypass_creation():
    '''function for stress testing database, bypasses user creation of accounts'''
    #creating random usernames with 9 chars randomly chosen
    username = ''.join(secrets.choice(string.ascii_lowercase) for i in range(9))
    print(username)
    #use password generation function
    password = generate_password()
    #store in test account file
    test_password_store(username,password)
    #salt and hash pw
    hashed = hash_password(password)
    #begin storing user + hashed password in real db file
    store_user_and_hashed_pw(username, hashed)
    
def testing(accounts):
    '''using n number of accounts as an int as an argument, stress tests the 
    framework of this code to check for performance or scalability issues'''

    try:
        accounts = int(accounts)
    except:
        error = 'testing error, argument must be an integer.'
        return error
    for i in range(0, accounts):
        bypass_creation()
    #log all accounts in
    test_account_login()

def test_account_login():
    '''open test db file to withdraw the user/passwords, matches them to the stored 
    hashed passwords and attempts a log in. This is executed for every test account'''

    with open(r'C:\Users\Public\PlainText Passwords\Test acct passwords.txt', 'r+') as file:
        file.seek(0)
        data = json.loads(file.read())
        for user,password in data.items():
            credentials = locate_hashed_pw(user)
            if credentials:
                #if username matches, authenticate password against hashed password
                #credentials now = True or False
                credentials =  authenticate(password, credentials)
                #return True or False
                if credentials:
                    comment = f'{user} connected'
                    return comment
                else: 
                    error = f'{user} connection failed'
                    return error
            else:
                #return False
                error = f'{user} connection failed'
                return error
            
#######################MODULE TESTING PACKAGE######################################











    
    
    

    