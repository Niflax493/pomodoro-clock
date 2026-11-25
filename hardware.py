# Configuration des composantes physiques (boutons, écrans, LEDs, etc.)
from machine import Pin
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

# Configuration des boutons de navigation
__NEXT_BTN_PIN = Pin.board.D6
__PREV_BTN_PIN = Pin.board.D5
__SELECT_BTN_PIN = Pin.board.D4
__POWER_BTN_PIN = Pin.board.D3
next_btn = Button(__NEXT_BTN_PIN)
prev_btn = Button(__PREV_BTN_PIN)
select_btn = Button(__SELECT_BTN_PIN)
power_btn = Button(__POWER_BTN_PIN)

# Updates the state of all buttons used
def update_all_buttons():
    for BUTTON in __BUTTONS:
        BUTTON.update()
        
__BUTTONS = (next_btn, prev_btn, select_btn, power_btn)