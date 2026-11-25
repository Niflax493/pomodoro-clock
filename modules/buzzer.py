import time
from hardware import buzzer


def play_note(frequency, duration):
    buzzer.freq(frequency)
    buzzer.duty_u16(500) # Volume

    time.sleep_ms(duration)
    buzzer.duty_u16(0)


def play_melody():

    notes = [
        (440, 300), # A4
        (523, 300), # C5
        (659, 300), # E5
    ]

    for frequency, duration in notes:
        play_note(frequency, duration)
        time.sleep_ms(100)


def stop():
    buzzer.duty_u16(0)