#3 Dictionaries
#Övn 1

pro_tid = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

mest_tid = 0
mest_tid_pro = ""

for projekt in pro_tid:
    if "Erik" in pro_tid[projekt]: #finns erik med i projektet
        eriks_tid = pro_tid[projekt]["Erik"]
       
        if eriks_tid > mest_tid:
            mest_tid = eriks_tid
            mest_tid_pro = projekt
if mest_tid_pro:
    print(f"Erik har spenderat mest tid på {mest_tid_pro}, med {mest_tid} timmar.")
else:
    print("Erik har inte jobbat på något av projekten.")

lina_pro = {}
for projekt, personer in pro_tid.items():  # gå igenom varje projekt
    if "Lina" in personer and personer["Lina"] > 30: #kolla om lina är med och har mer än 30 timmar i ett projekt
        lina_pro[projekt] = personer # lägg till projektet i den nya dictionaryn

print(lina_pro)

