letters='abcdefghijklmnopqrstuvwxyz'
def encrypt(text,key):
    cipher=''
    for i in text:
        i=i.lower()
        if i!=' ':
            index=letters.find(i)
            if index==-1:
                cipher=cipher+i
            else:
                new_index = (index - key) % 26
                cipher += letters[new_index]
    return cipher

k=int(input('Enter the key: '))
t=input('Enter the text to encrypt: ')
print("The encrypted text is: ")
print(encrypt(t,k))


