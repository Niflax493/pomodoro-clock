from hardware import lcd
from modules.buzzer import play_melody

lcd.clear()
lcd.move_to(0,0)
lcd.putstr("- MODE -")
lcd.move_to(0,1)