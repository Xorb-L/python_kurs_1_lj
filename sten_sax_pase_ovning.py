#sten sax påse mot slumpade datorn
import random
anv_poäng = 0
dat_poäng = 0
någon_vunnit = False

while någon_vunnit == False:
    # skaffar användarens val
    anv_val = input("välj sten, sax eller påse?: ")
    if anv_val not in ["sten", "sax", "påse"]:
        print("Välj mellan sten, sax och påse!")
        continue
        
    # skaffa datorn val
    dat_val = random.randint(1,3) # random tal 1-3
    if dat_val == 1:
        dat_val = "sten"
    elif dat_val == 2:
        dat_val = "sax"
    else:
        dat_val = "påse"
    print("användare: " + str(anv_val))
    print("datorn: " + str(dat_val))
    # slumpat

    #avgöra vem som vann rundan
    if anv_val == "sten" and dat_val == "sax": #vinst anv
        anv_poäng += 1
    elif anv_val == "sten" and dat_val == "påse": # förlust
        dat_poäng += 1
    if anv_val == "sax" and dat_val == "sten": # förlust
        dat_poäng += 1
    elif anv_val == "sax" and dat_val == "påse": # vinst
        anv_poäng += 1
    if anv_val == "påse" and dat_val == "sten": # vinst
        anv_poäng += 1
    elif anv_val == "påse" and dat_val == "sax": # förlust
        dat_poäng += 1
    #else:
    #    print("ingen vann rundan")

    #print("användarens poäng: " + str(anv_poäng))
    #print("datorns poäng: " + str(dat_poäng))

    if anv_poäng == 1:
        någon_vunnit = True
        print("Användaren vann!!!\nGame over!")
    elif dat_poäng == 1:
        någon_vunnit = True
        print("Datorn vann!!!\nGame over!")
    else:
        print("ingen vann rundan")

        

