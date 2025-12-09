
verseny_adatok = []

inputfajl="F1-2024dec.csv"

def adatok_beolvasas(fajlnev):
    try:
        with open(fajlnev, encoding="utf-8") as fajl:
            global verseny_adatok
            verseny_adatok = fajl.readlines()

    except Exception as ex:
        print(f"Halihóóóóó!: Hiba oka: {ex}")
    except FileNotFoundError:
        print("Hiba a fájl megnyitása közben!")







    """
    1. [X] Megszámolás
    2. [X] Eldöntés 1
       [X] Eldöntés 2
    3. [X] Kiválasztás
    4. [X] Keresés
    5. [x] Sorozatszámítás, összegzés
    6. [x] Minimum/maximum kiválasztás
    
    7. [] Másolás
    8. [] Kiválogatás
    9. [] Szétválogatás
    10.[] Metszet
    11.[] Únió
    
    12. Rendezés
        [] Egyszerű cserés rendezés
        [] Buborékos
        [] Minimum kiválasztásos
    """

#ELJÁRÁS
def pontatlanok():

# 1. Hány versenyző nem szerzett még pontot?
    db = 0

    for i in range(1, len(verseny_adatok)):
        if(int(verseny_adatok[i].split(',')[1]) == 0):
            db = db + 1

    print(f"{db} versenyző nem szerzett még pontot.\n")


# ---------------------------------------------------------
#FÜGGVÉNY
def versenyzo_kereso(nev):
    # 2.A Van-e Fernando nevű versenyző?
    i = 0
    while (i<len(verseny_adatok)and nev not in verseny_adatok[i]):
        i=i+1
    if (i<len(verseny_adatok)):
        print("Van ilyen versenyző")
    else:
        print("Nincs ilyen versenyző")  

# ---------------------------------------------------------

#ELJÁRÁS
def melyik_csapat(nev):
    #4. melyik csapatban volt Pierre Gasly?
    i=1
    while i<len(verseny_adatok) and nev not in verseny_adatok[i]:
        i=i+1
    if i<len(verseny_adatok):
        print(nev , " a(z)", verseny_adatok[i].split(",")[2].strip(), "csapatban van!:)")
    else:
        print("Nincs ilyen versenyző ezért egyik csapatban sincs bennt!:(")


#FÜGGVÉNY
def istallo(csapatnev):
#8. kik vannak a Mclaren istálloban
    db1=0
    masik_lista=[]
    for i in range(2,len(verseny_adatok)):
        if verseny_adatok[i].split(",")[2].strip()==csapatnev:
            db1=db1+1
            masik_lista.append(verseny_adatok[i].split(",")[0])


    return masik_lista

#eljaras
def kilencven(pont):
    # 2.B Mindenki szerzett már 90 pontot?
    i=1
    while i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1])>=90:
        i=i+1
    if i==len(verseny_adatok):
        print("van")
    else:
        print("nem")




#eljaras
def pilota(pilot):
    3. #Melyik istálló pilotája a Yuki Tsunoda?
    i=0
    while verseny_adatok[i].split(",")[0]!=pilot:
        i+=1
    print(f"{pilot} a",verseny_adatok[i].split(",")[2])



""" 
# ---------------------------------------------------------    
 


 #eljaras
#5. számolja ki a versenyzők pontszámainak átlagát
S=0
for i in range(1, len(verseny_adatok)):
    S+=int(verseny_adatok[i].split(',')[1])
print(f"a versenyzők pontszámainak átlaga: {S/len(verseny_adatok)-1}")

# ---------------------------------------------------------

#6. Max kiválasztás    
maxi=1
max=verseny_adatok[i].split(",")[1]
for i in range(3,len(verseny_adatok)):
    if verseny_adatok[i]>verseny_adatok[maxi]:
        maxi=i
        max=verseny_adatok[i]

# ---------------------------------------------------------
        
#6. Min kiválasztás
mini=1
min=verseny_adatok[i].split(",")[1]
for i in range(2,len(verseny_adatok)):
    if verseny_adatok[i]<verseny_adatok[mini]:
        mini=i
        min=verseny_adatok[i]
print("A legkevesebb ponttal rendelkező versenyző: ",verseny_adatok[mini].split(",")[0])

# ---------------------------------------------------------


#9. SZÉTVÁLOGATÁS
# kinek van kinek nincs pontja?
dby=0
dbx=0
y=[]
x=[]
for i in range(1, len(verseny_adatok)):
    if(int(verseny_adatok[i].split(",")[1])>0):
        dby=dby+1
        y.append(verseny_adatok[i].split(",")[0])
    else:
        dbx=dbx+1
        x.append(verseny_adatok[i].split(",")[0])
print(f"Van pontja:{y}\n\nnincs pontja: {x}")
        





# ---------------------------------------------------------

#7. MÁSOLÁS
#







# ---------------------------------------------------------

#12. RENDEZÉS: minimmumkiválasztásos

#Versenyzők pontszáma alapján növekvő sorrendbe:
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

 """
#PROGRAM


adatok_beolvasas(inputfajl)
#1. F eljárás hívás
pontatlanok()


#2.F függvény hívás
van_e=versenyzo_kereso("Fernando")
if van_e:
    print("Van Fernando")
else:
    print("Nincs Fernando")


#4.F eljárás hívás
melyik_csapat("Pierre Gasly")


#8.F függvény hívás
csapat_nev="McLaren"
tag_lista=istallo("McLaren")
print(f"Ezek a személyek vannak a {csapat_nev} istálloban: ")
i=1
for nev in tag_lista:
    print(f"\t{i}.{nev:>30}#")
    i+=1



#2B
kilencven(90)


#
print("ITT A PROGRAM VÉGE!")