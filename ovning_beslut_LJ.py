#2 Beslut
#Övn 1

for i in range(1, 101): #räkna 1- 100 och spara det i i
    if i % 3 == 0 and i % 5 == 0: # om i(talet) är jämnt delbart med 3 och 5
            print("FizzBuzz")
    elif i % 3 == 0: # om talet är delbart med 3
        print("Fizz")
    elif i % 5 == 0: # om talet är delbart med 5
        print("Buzz")
    else:
        print(i)
       
#----------------------------------
#Övn 2

skott_ar = int(input("Skriv in ett årtal\n"))

if (skott_ar % 4 == 0 and skott_ar % 100 != 0) or (skott_ar % 400 == 0):
    print("Det är ett skottår")
else:
    print("Det är inte ett skottår")