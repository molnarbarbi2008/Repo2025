


#A hibakezelés használata után a hiba üzenet megakadályozva lesz
try:
    
    with open("F1-2024dec.csv" ,encoding="utf-8") as fajl:
        f=fajl.read()
        
        n = 4 / 0
        
        print(f)
        print(n)
        
except FileNotFoundError:
    print("Hiba a fájl megnyitása közben!")

except ZeroDivisionError:
    print("Ne ossz nullával!")
    
except Exception:
    print("Halihóóóóóóóóó") 
    

       
print("ITT A PROGRAM VÉGE")


