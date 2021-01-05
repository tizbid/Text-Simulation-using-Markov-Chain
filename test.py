name = 'peter'

def job():
    if name == 'john':
        role = 'SE'
    else:
        role = 'PE' 
    return role
   
def salary():
    role = job()
    if role == 'SE':
        pay = 1000
    else:
        pay = 1500
    return print(pay)
    

salary() 
