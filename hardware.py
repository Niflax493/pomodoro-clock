# Configuration des composantes physiques (boutons, écrans, LEDs, etc.)
from machine import Pin
from modules.lcd import LCD 

# Configuration de l'écran
RS_PIN       = Pin.board.D12
E_PIN        = Pin.board.D11
D4_PIN       = Pin.board.D10
D5_PIN       = Pin.board.D9
D6_PIN       = Pin.board.D8
D7_PIN       = Pin.board.D7
CONTRAST_PIN = Pin.board.D2
lcd = LCD(rs=RS_PIN, 
          e=E_PIN, 
          d4=D4_PIN, 
          d5=D5_PIN, 
          d6=D6_PIN, 
          d7=D7_PIN,
          contrast_pin=CONTRAST_PIN)

