





#A hibakezelés használata után a hiba üzenet megakadályozva lesz
try:
    
    with open("F1-2024dec.csv" ,encoding="utf-8") as fajl:
        verseny_adatok=fajl.readlines()
        

        
        
except Exception as ex:
    print(f"Halihóóóóóóóóó!: Hiba oka: {ex}") 
    
except FileNotFoundError:
    print("Hiba a fájl megnyitása közben!")



    """
    1.[] Megszámolás
    2.[] Eldöntés 1
    Eldöntés 2
    3.[] Kiválasztás
    4.[] Keresés
    5.[] Sorozatszámítás
    6.[] Minimum/maximum kiválasztás
    7.[] Másolás
    8.[] Kiválogatás
    9.[]Szétválogatás
    10.[]Metszet
    11.[]Únió
    
    12. Rendezés
        [] Egyszerű cserés rendezés
        [] Buborékos
        [] Minimum kiválasztás
    
    
    
    """


    
#------------------------------------------
#1. Hány versenyző nem szerzett még pontot?
db=0

for i in range(1, len(verseny_adatok)):
    if(int(verseny_adatok[i].split(',')[1])==0):
        db=db+1
        
print(db, "versenyző nem szerzett még pontot!")

       

#2. Van-e  Fernando nemű versenyző?
i=0

while (i<len(verseny_adatok) and 'Fernando' not in verseny_adatok[i]):
    i=i+1
if(i<len(verseny_adatok)):
    print("Van!")
    
   
   
#Mindenki szerzett már kilencven pontot?
i=0

while(i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1])>=90):
    i=i+1
if(i<len(verseny_adatok)):
    print("Nem mindenki!")
        
        
    

    


