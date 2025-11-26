





#A hibakezelés használata után a hiba üzenet megakadályozva lesz
try:
    
    with open("F1-2024dec.csv" ,encoding="utf-8") as fajl:
        verseny_adatok=fajl.readlines()
        

        
        
except Exception as ex:
    print(f"Halihóóóóóóóóó!: Hiba oka: {ex}") 
    
except FileNotFoundError:
    print("Hiba a fájl megnyitása közben!")



    """
    1.[x] Megszámolás
    2.[x] Eldöntés 1
    Eldöntés 2
    3.[x] Kiválasztás
    4.[x] Keresés
    5.[x] Sorozatszámítás összegzés
    6.[x] Minimum/maximum kiválasztás
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
    
   
   
#2(2).Mindenki szerzett már kilencven pontot?
i=1

while(i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1])>=90):
    i=i+1
if(i<len(verseny_adatok)):
    print("Nem mindenki!")
    




#3.melyik csapat tagja a Yuki Tsunoda?
i=0
while verseny_adatok[i].split(",")[0]!="Yuki Tsunoda":
    i+=1
print("Yuki Tsunoda a", verseny_adatok[i].split(",")[2])



#4.kereses melyik cspatban van Pierre Gasly?
i=1
while i<len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok[i]:
    i=i+1
if i<len(verseny_adatok):
    print("Pierre Gasly", verseny_adatok[i].split(',')[2].strip(), "csapatbn van")
else:
    print("nincs")




#5.adja meg a pontszamok átlagát
S=0
for i in range (1, len(verseny_adatok)):
    S+=int(verseny_adatok[i].split(',')[1])
print(f"A versenyzők pontszámának átlaga: {S/len(verseny_adatok)-1}")




#6.kinek volt a legtöbb pontja?
maxi=1
maxertek=verseny_adatok[i].split(',')[1]


for i in range(2, len(verseny_adatok)):
    if(verseny_adatok[i]>verseny_adatok[maxi]):
        maxi=i
        maxertek=verseny_adatok[i].split(',')[1]
print(f"A legnagyobb érték: {maxertek}")


    
    


#8.versenyzők pontszáma alapján növekvő sorrenbe:
for i in range(1, len(verseny_adatok)-1):
    min=i
    minertek=int(verseny_adatok[i].split(',')[1])
    for j in range(i+1, len(verseny_adatok)):
        if(int(verseny_adatok[j].split(',')[1])<int(verseny_adatok[min].split(',')[1])):
            min=j
            minertek=int(verseny_adatok[j].split(',')[1])
    s=verseny_adatok[i]
    verseny_adatok[i]=verseny_adatok[min]
    verseny_adatok[min]=s
for i in verseny_adatok:
    print(i)
      
      
      
      
      
      
      
      
      
        
        
    

    


