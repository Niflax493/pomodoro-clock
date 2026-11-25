from hardware import *
from time import sleep
lcd.clear()
lcd.move_to(0,0)
lcd.putstr("- MODE -")

i = 0
cycles = 4 # Number of cycles
work = 25 # 25 minutes of work
pause = 5 # 5 minutes break
while True:
    if (prev_btn.is_clicked()):
        i+=1
            
    if (next_btn.is_clicked()):
        i-=1
        
    update_all_buttons()
    print(i)
    sleep(0.05)