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
        0: Clean
        1: Jump Start(P1)
        2: Jump Start(P2)
    """
    wait_time = time.ticks_ms() + duration
    while wait_time > time.ticks_ms():
        if pin1.is_touched():
            return 1
        if pin2.is_touched():
            return 2
        time.sleep_ms(1)
    return 0


def light_up(column):
    display.set_pixel(column, 3, LED_BRIGHTNESS)
    display.set_pixel(column, 4, LED_BRIGHTNESS)
    music.pitch(150, 150, wait=False)


def start_sequence():
    """
    Returns:
        0: Clean
        1: Jump Start(P1)
        2: Jump Start(P2)
    """
    display.clear()

    # Light up the subsequent column
    for seq in range(5):
        if seq != 0:
            player_jumped = wait_for(LIGHT_INTERVAL)
            if player_jumped != 0:
                return player_jumped
        light_up(seq)

    # Lights out
    player_jumped = wait_for(go_wait())
    if player_jumped != 0:
        return player_jumped
    display.clear()
    return 0


# Main routine
while True:
    while not pin_logo.is_touched():
        time.sleep_ms(1)

    player_jumped = start_sequence()
    if player_jumped == 1:
        display.show(Image('00000:'
                       '90900:'
                       '09000:'
                       '90900:'
                       '00000'))
        time.sleep_ms(1000)
        continue
    if player_jumped == 2:
        display.show(Image('00000:'
                       '00909:'
                       '00090:'
                       '00909:'
                       '00000'))
        time.sleep_ms(1000)
        continue

    start_time = time.ticks_ms()
    while True:
        if pin1.is_touched():
            display.show(Image('00000:'
                       '09000:'
                       '90900:'
                       '09000:'
                       '00000'))
            time.sleep_ms(1000)
            break
        if pin2.is_touched():
            display.show(Image('00000:'
                       '00090:'
                       '00909:'
                       '00090:'
                       '00000'))
            time.sleep_ms(1000)
            break
        time.sleep_ms(1)

    # reaction_time = time.ticks_diff(time.ticks_ms(), start_time)
    # display.scroll("{:.3f}".format(reaction_time / 1000.0))
