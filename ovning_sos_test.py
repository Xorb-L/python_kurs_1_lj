# SOS med nödknapp
# Utgår ifrån "Project 2.1 Button & LED" 

# Skriv en funktion som heter send_sos och ta emot en parameter som heter num_of_sos. Funktionen blinkar "led" i form av SOS meddelande  (3 korta blink, 3 långa blink och 3 korta blink) num_of_sos gånger.
# Så länge knappen är nertryck ska send_sos funktion anrops, när man ha släpp knappen ska send_sos funktion inte längre anropas.
# Ladda upp lösning i Github och märkera uppgift är inlämnat här på Learnpoint 

from machine import Pin
import time

#konstanter
LED_PIN = 15  #GPIO 15
BUTTON_PIN = 13 #GPIO 13
kort_blink = 0.2 # tid för kort blink i sekunder
long_blink = 0.7
pause = 0.2 # pause mellan blink

# skap obj för led knapp
led = Pin(LED_PIN, Pin.OUT)
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)

def send_sos(num_of_sos):
    for _ in range(num_of_sos):
        # 3 korta
        for _ in range(3):
            led.on()
            time.sleep(kort_blink)
            led.off()
            time.sleep(pause)
            
        # 3 långa blink
        for _ in range(3):
            led.on()
            time.sleep(long_blink)
            led.off()
            time.sleep(pause)
        
        # 3 korta igen
        for _ in range(3):
            led.on()
            time.sleep(kort_blink)
            led.off()
            time.sleep(pause)
    # pause mellan varje sos
    time.sleep(1)

#Huvud loop för att kolla knappen
while True:
    if not button.value(): # Om knappen är nedtryckt
        send_sos(1) # skicka sos en gång
    else:
        time.sleep(0.1) # kontrollera igen efter en kort paus
