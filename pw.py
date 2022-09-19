
import secrets 
import string

password = None


while len(str(password)) != 11:
    password = ''.join(secrets.choice(string.ascii_lowercase) for i in range(2))
    password = password + ''.join(secrets.choice(string.digits) for i in range(8))
    password = password + ''.join(secrets.choice(string.punctuation) for i in range(1))
    password = password.capitalize()
    

        
        



print(password)

    
    
    

    