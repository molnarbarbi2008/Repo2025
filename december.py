"""
    Ebben a feladatban a 12.B tanulócsoport
    DHCP témakörben
    mutatott teljesítményének néhány elemével
    kell műveleteket végeznie!
    
    Az adatok a 12B_dhcp_ponttabla.txt fájlban találhatóak meg!
    
    A fájl felépítése:
    1.sor: Tartalmazza a maximális pontszám feliratot és az értéket.
    2.sor: Az adatsorok oszlopaiban szereplő értékek magyarázatai:
        név
        elméleti dolgozat pontszáma
        gyakorlati dolgozat pontszáma
        össz pontszám
    3. sortól: az adatok
    
    A fejlécben és az adatértékek között az elválasztó karakter: ';'
    
    A programot metódusok segítségével oldja meg!
    A fájl végén találja a programot, ahol meghívhatja a metódusokat és kiírhatja az eredményeket. Kiírásnál jelenjen meg a feladat sorszáma is!
    Pl.: 13. feladat:
            A pontszámok átlaga: 435 pont.
"""

# *************************************
# GLOBÁLIS VÁLTOZÓK

ossz_pontszam = 0

tanulo_adatok = []


inputfile="szoveg.txt"

def halozat_eredmenyek(fajl):
    try:
        with open(fajl, encoding="utf-8") as f:
            global ossz_pontszam
            tanulo_adatok_adatok = f.readlines()

    except Exception as ex:
        print(f"Halihóóóóó!: Hiba oka: {ex}")
    except FileNotFoundError:
        print("Hiba a fájl megnyitása közben!")
        
        
# *************************************

# METÓDUSOK/FÜGGVÉNYEK

"""
    1.
    Olvassa be a fájl tartalmát figyelembe véve a fájl szerkezetét!
    A maximális pontszámot tárolja el az ossz_pontszam változóban!
    A tanulók adatait egy "2D"-s listában  (lista a listában: tanulo_adatok) tárolja el.
    A metódus neve: fajl_beolvasas
"""





"""
    2.
    Határozza meg hány tanulóból áll a csoport!
    A metódus neve: csoport_letszam
"""





"""
    3.
    Határozza meg melyik tanuló gyűjtötte a legtöbb pontszámot!
    A metódus neve: legszorgalmasabb
"""





"""
    4.
    Mikulás közeledtével a tanár mindenkinek bónusz pontokat ír jóvá.
    Minden tanuló az össz pontszámának 5%-át kapja meg bónuszként.
    Kiírásnál jelenítse meg a tanulók nevét és az új pontszámokat.
    A metódus neve: miki_ajandek
"""





# *************************************
#   PROGRAM
# *************************************
cim = "Eredmény feldolgozó szkript"
print(f"\n{'*' * 40}\n{cim.upper():^40}\n{'*' * 40}\n\n")


# fajl_beolvasas

# csoport_letszam

# legszorgalmasabb

# miki_ajandek


halozat_eredmenyek(inputfile)
print("\nProgram vége. BYE!\n")

