
import secrets 
import string
pwuse = input('Enter what password is for: ')
password = None


while len(str(password)) != 11:
    password = ''.join(secrets.choice(string.ascii_lowercase) for i in range(2))
    password = password + ''.join(secrets.choice(string.digits) for i in range(8))
    password = password + ''.join(secrets.choice(string.punctuation) for i in range(1))
    password = password.capitalize()


#a is write, a+ is read and write pointing to end of file 
# put r in front of a string to convert it to raw code for the path to be read      
with open(r'C:\Users\oudud\Desktop\Passwords\Passwords.txt', 'a+') as f:
    #moving to start of file
    f.seek(0)
    #reading file
    data = f.read(100)
    #adds new line if file has entries
    if len(data) > 0:
        f.write("\n")
    f.write(f"{pwuse}: {password}")



print(pwuse,':' ,password)

    
    
    

    