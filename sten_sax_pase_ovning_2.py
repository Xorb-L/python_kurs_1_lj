#sten sax påse mot slumpade datorn
import random

def spela_sten_sax_påse():
    anv_poang = 0
    dat_poang = 0
    någon_vunnit = False
    
    while någon_vunnit == False:
        # skaffar användarens val
        anv_val = input("välj sten, sax eller påse?: ")
        if anv_val not in ["sten", "sax", "påse"]:
            print("Välj mellan sten, sax och påse!")
            continue
            
        # skaffa datorn val
        dat_val = random.choice(["sten", "sax", "påse"]) # random tal 1-3
        
        print(f"Användare: {anv_val}")
        print(f"Datorn: {dat_val}")
       
        #avgöra vem som vann rundan
        if anv_val == "sten" and dat_val == "sax": #vinst anv
            anv_poang += 1
        elif anv_val == "sten" and dat_val == "påse": # förlust
            dat_poang += 1
        elif anv_val == "sax" and dat_val == "sten": # förlust
            dat_poang += 1
        elif anv_val == "sax" and dat_val == "påse": # vinst
            anv_poang += 1
        elif anv_val == "påse" and dat_val == "sten": # vinst
            anv_poang += 1
        elif anv_val == "påse" and dat_val == "sax": # förlust
            dat_poang += 1

        # kolla om någon har vunnit
        if anv_poang == 1:
            någon_vunnit = True
            print("Användare vann!!!\nGame over!")
        elif dat_poang == 1:
            någon_vunnit = True
            print("Datorn vann!!!\nGame over!")
        else:
            print("Ingen vann rundan")

    spela_igen()

def spela_igen():
    while True:
        spela_igen = input("Nytt spel? (ja/nä): ")
        if spela_igen == "ja":
            spela_sten_sax_påse() # starta om
        elif spela_igen == "nä":
            print("Game over!")
            break
        else:
            print("Vänligen skriv 'ja' eller 'nä'")

spela_sten_sax_påse()
