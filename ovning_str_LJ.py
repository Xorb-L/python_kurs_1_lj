#1a. räkna vokaler

def rakna_vokaler(text):
    vokaler = "aeiouåäöAEIOÅÄÖ" #lista på både stora och små vokaler
    antal_vokaler = 0 # räknare för vokaler
    for c in text: #går igenom varje bokstav i texten
        if c in vokaler: #Om bokstaven finns i vokaler
            antal_vokaler += 1 #öka räknaren
    return antal_vokaler # returnera antal vokaler
       
text = "Hej världen"
print(rakna_vokaler(text))

#-------------------------------------------------
#1b: Tar bort vokaler
#Skriv en funktion som tar emot en sträng och tar bort vokaler som finns i strängen.

def ta_bort_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  # Lista på vokaler både små och stora
    bort_vokaler = ""
    for c in text:
        if c not in vokaler:
            bort_vokaler += c  # tomt + lägg til dom bokstäver som inte finns i vokaler
    return bort_vokaler

text = "Hej världen"
print(ta_bort_vokaler(text))

#-------------------------------------------------
#2: title case

def till_titel_case(text):
ord = text.split() # Dela upp texten i en lista med ord
titel_case_ord = [ordet.capitalize() for ordet in ord]
return ' '.join(titel_case_ord)

text = "hej världen"
print(till_titel_case(text))

#-------------------------------
#3: Antal ord

def rakna_ord(text):
    ord = text.split() # dela upp texten
    return len(ord) #räkna orden

text = "Detta är en mening"
print(rakna_ord(text))

