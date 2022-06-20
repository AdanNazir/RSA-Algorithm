

import random


c=0
e=0
n=0
phi=0
d=0
l1=[]
l2=[]
message=[]



def gcd (x,y):
    while y !=0:
        x , y = y, x %y
    return x

def Encryption(message,e,n):
    
    enc=pow(message,e)
    enc1=enc%n
    return enc1

def Decryption(c,d,n):
 
    dec=pow(c,d)
    dec=dec%n
    return dec


def Private_Key(a,m):
    for val in range(1,m):
        if (((a%m) * (val%m)) % m == 1):
            return val
    x+=1


def Public_Key (key1,key2):
    PrivateKey=0
    PublicKey=0
    
    n=0
    e=0
    
    n=key1*key2
    phi = (key1-1)*(key2-1)
    e = random.randrange(1,n)
    while (gcd(e, phi)) !=1:
        e = random.randrange(1,n)
    return (e,n,phi)


while(1):
    print("1. Key Generation, 2.Encryption/Decryption, 3.Quit=>")
    inp=input()
    inp=int(inp)
    if inp==1:
        print("Enter the first prime number: ")
        in1=input()
        in1=int(in1)
        
        print("Enter the second prime number : ")
        in2=input()
        in2=int(in2)
        
        e,n,phi=Public_Key(in1,in2)
        print("Public Key : ")
        print(e,n)
        
        d=Private_Key(e,phi)
        print("Private Key: ")
        print(d,n)
    
    if inp==2:

        D=int(input("Enter the first part of the Public/Private key: "))

        N=int(input("Enter the second part of the Public/Private key: "))
        
        print("Enter the message to Encrpyt/Decrypt: ")
        
        for i in range(0,9):
            me=input()
            me1=int(me)
            message.append(me1)
            
        if D==e:
            for i in range(0,9):
                l1.append(Encryption(message[i],e,n))
                print("Encrpyted Message: ",l1[i])
            message.clear()
            
        else:
            for i in range(0,9):
                x=Decryption(l1[i],D,n)
                print("Decrypted Message: ",x)
                
        
            message.clear()
    
    elif inp==3:
        break
        
    






