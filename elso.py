import random

szamok=[]
#100 elemű lista feltöltése 
for i in range(100):
    rszam=random.randint(1,100)
    
    szamok.append(rszam)
    
print(szamok)

jatek_szam=0
nem_talaltDB=0



kitalalando_szam=szamok[random.randint(0, len(szamok))]



tipp=input("Kérek egy egész számot [1-100] között")


while(not tipp.isdecimal()):
    print("ez nem egy egész szám!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    tipp=input("Kérek egy egész számot [1-100] között")
    
tipp=int(tipp)
    
    

if(tipp<kitalalando_szam):
     print("A kitalálandó szám nagyobb!")
     
elif(tipp>kitalalando_szam):
    print("A kitalálandó szám kisebb")
    

    
while(tipp!=kitalalando_szam):
    tipp=input("Kérek egy egész számot [1-100] között")


    while(not tipp.isdecimal()):
        print("ez nem egy egész szám!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        tipp=input("Kérek egy egész számot [1-100] között")
        
    tipp=int(tipp)
        
        

    if(tipp<kitalalando_szam):
        print("A kitalálandó szám nagyobb!")
        
    elif(tipp>kitalalando_szam):
        print("A kitalálandó szám kisebb")
        
print("gratulálok!!!!!")
