from microbit import *  # noqa: F401, F403
import time
import random
import music

LED_BRIGHTNESS = 5
LIGHT_INTERVAL = 1000


class State:
    NO_JUMP_START = 0
    P1_JUMPED = 1
    P2_JUMPED = 2


def go_wait():
    return random.randint(2000, 3000)


def wait_for(duration):
    """
    wait for duration(ms) time

    Returns:
        State.NO_JUMP_START
        State.P1_JUMPED
        State.P2_JUMPED
    """
    wait_time = time.ticks_ms() + duration
    while wait_time > time.ticks_ms():
        if pin1.is_touched():
            return State.P1_JUMPED
        if pin2.is_touched():
            return State.P2_JUMPED
        time.sleep_ms(1)
    return State.NO_JUMP_START


def light_up(column):
    display.set_pixel(column, 3, LED_BRIGHTNESS)
    display.set_pixel(column, 4, LED_BRIGHTNESS)
    music.pitch(150, 150, wait=False)


def start_sequence():
    """
    Returns:
        State.NO_JUMP_START
        State.P1_JUMPED
        State.P2_JUMPED
    """
    display.clear()

    # Light up the subsequent column
    for seq in range(5):
        if seq != 0:
            state = wait_for(LIGHT_INTERVAL)
            if state != State.NO_JUMP_START:
                return state
        light_up(seq)

    # Lights out
    state = wait_for(go_wait())
    if state != State.NO_JUMP_START:
        return state
    display.clear()
    return State.NO_JUMP_START


# Main routine
while True:
    while not pin_logo.is_touched():
        time.sleep_ms(1)

    state = start_sequence()
    if state == State.P1_JUMPED:
        display.show(Image('00000:'
                           '90900:'
                           '09000:'
                           '90900:'
                           '00000'))
        continue
    if state == State.P2_JUMPED:
        display.show(Image('00000:'
                           '00909:'
                           '00090:'
                           '00909:'
                           '00000'))
        continue

    while True:
        if pin1.is_touched():
            display.show(Image('00000:'
                               '09000:'
                               '90900:'
                               '09000:'
                               '00000'))
            break
        if pin2.is_touched():
            display.show(Image('00000:'
                               '00090:'
                               '00909:'
                               '00090:'
                               '00000'))
            break
        time.sleep_ms(1)
