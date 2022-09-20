
from main import log_in
# user = 'striker'
# password = 'Oo46870466{'
# print(log_in(user,password))
attempts = 0
connection = False
while connection == False:
    username, password = input('Enter username:'), input('Enter password:')
    connection = log_in(username, password)
    attempts += 1
    
    if connection == False and attempts < 3:
        print('Username or password is incorrect.\nPlease try again.')
        continue
    if attempts == 3 and connection == False:
        print('Log in attempts exceeded.')
        break

    else:
        print('connected')
        
while connection == True:
    message = input('Enter a message:')
    if message == exit:
        print('Ending connection')
        break


