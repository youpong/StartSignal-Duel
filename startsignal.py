from microbit import *  # noqa: F401, F403
import time
import random
import music

LED_BRIGHTNESS = 5
LIGHT_INTERVAL = 1000


def go_wait():
    return random.randint(2000, 3000)


def wait_for(duration):
    """
    wait for duration(ms) time

    Returns:
        False: Jump Start
    """
    wait_time = time.ticks_ms() + duration
    while wait_time > time.ticks_ms():
        if button_a.is_pressed():
            return False
        time.sleep_ms(1)
    return True


def light_up(column):
    display.set_pixel(column, 3, LED_BRIGHTNESS)
    display.set_pixel(column, 4, LED_BRIGHTNESS)
    music.pitch(150, 150, wait=False)


def start_sequence():
    """
    Returns:
        False:
            Jump Start
    """
    display.clear()

    # Light up the subsequent column
    for seq in range(5):
        if seq != 0 and not wait_for(LIGHT_INTERVAL):
            return False
        light_up(seq)

    # Lights out
    if not wait_for(go_wait()):
        return False
    display.clear()
    return True


# Main routine
while True:
    while not pin_logo.is_touched():
        time.sleep_ms(1)

    if not start_sequence():
        display.show(Image.NO)
        continue

    start_time = time.ticks_ms()
    while not button_a.is_pressed():
        time.sleep_ms(1)
    reaction_time = time.ticks_diff(time.ticks_ms(), start_time)
    display.scroll("{:.3f}".format(reaction_time / 1000.0))
