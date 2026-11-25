from machine import Pin

class Button:
    def __init__(self, pin: Pin.board):
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.curr_val = self.__get_pin_value()
        self.prev_val = self.curr_val
        
    def update(self):
        self.prev_val = self.curr_val
        self.curr_val = self._pressed()
    
    def update(self):
        self.prev = self.curr
        self.curr = self._pressed()

    def is_clicked(self):    # vient d'être appuyé
        return self.curr and not self.prev

    def is_held(self):       # reste appuyé
        return self.curr and self.prev

    def is_released(self):   # vient d'être relâché
        return self.prev and not self.curr