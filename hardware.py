# Configuration des composantes physiques (boutons, écrans, LEDs, etc.)
from machine import Pin, PWM
from modules.lcd import LCD
from modules.button import Button

# Configuration de l'écran
__RS_PIN       = Pin.board.D12
__E_PIN        = Pin.board.D11
__D4_PIN       = Pin.board.D10
__D5_PIN       = Pin.board.D9
__D6_PIN       = Pin.board.D8
__D7_PIN       = Pin.board.D7
__CONTRAST_PIN = Pin.board.D2
lcd = LCD(rs=__RS_PIN, 
          e=__E_PIN, 
          d4=__D4_PIN, 
          d5=__D5_PIN, 
          d6=__D6_PIN, 
          d7=__D7_PIN,
          contrast_pin=__CONTRAST_PIN)

# Configuration du buzzer
BUZZER_PIN = Pin.board.D13
buzzer = PWM(BUZZER_PIN, freq=440, duty_u16=0)