import random 
#generator haseł

def get_pas():
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?@.'
    pas = ''.join(random.sample(al, 8))
    return pas
print(get_pas())
