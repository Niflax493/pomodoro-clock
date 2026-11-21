from machine import Pin, PWM
from time import sleep_ms, sleep_us

CONSTRASTE = 0.5
 
class LCD:
    def __init__(self, 
                 rs:Pin.board, 
                 e:Pin.board,
                 d4:Pin.board,
                 d5:Pin.board, 
                 d6:Pin.board,
                 d7:Pin.board, 
                 contrast_pin:Pin.board,
                 contrast=CONSTRASTE, 
                 cols=8, 
                 rows=2):
        self.rs = Pin(rs, Pin.OUT, value=0)
        self.e = Pin(e, Pin.OUT, value=0)
        self.data = [Pin(p, Pin.OUT, value=0) for p in (d4, d5, d6, d7)]
        self.cols = cols
        self.rows = rows
 
        # Contraste par PWM : à régler avant l'initialisation de l'écran.
        # Plus la valeur (0.0 à 1.0) est haute, plus le texte est pâle.
        self.pwm = PWM(Pin(contrast_pin), freq=1000)
        self.set_contrast(contrast)
 
        # Séquence d'initialisation HD44780 en mode 4 bits
        sleep_ms(50)
        for _ in range(3):
            self._write4(0x03)
            sleep_ms(5)
        self._write4(0x02)            # passage en mode 4 bits
        self.command(0x28)            # 4 bits, 2 lignes, police 5x8
        self.command(0x0C)            # affichage ON, curseur OFF
        self.command(0x06)            # curseur qui avance vers la droite
        self.clear()
 
    def set_contrast(self, value):
        """value entre 0.0 et 1.0 (rapport cyclique de la PWM sur V0)."""
        if self.pwm is None:
            return
        value = max(0.0, min(1.0, value))
        self.pwm.duty_u16(int(value * 65535))
 
    def _write4(self, nibble):
        for i, pin in enumerate(self.data):
            pin.value((nibble >> i) & 1)
        self.e.value(1)
        sleep_us(2)
        self.e.value(0)
        sleep_us(50)
 
    def _send(self, value, rs):
        self.rs.value(rs)
        self._write4(value >> 4)
        self._write4(value & 0x0F)
 
    def command(self, cmd):
        self._send(cmd, 0)
        sleep_us(50)
 
    def clear(self):
        self.command(0x01)
        sleep_ms(2)
 
    def move_to(self, col, row):
        offsets = (0x00, 0x40)       # adresses DDRAM des lignes 0 et 1
        self.command(0x80 | (offsets[row] + col))
 
    def putstr(self, text):
        for ch in text:
            self._send(ord(ch), 1)
