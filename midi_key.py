import time

import pygame
import pygame.midi as m
from pygame.locals import *

VEL = 127

def main():
    m.init()
    input, output = None, None
    for i in range(pygame.midi.get_count()):
        info = pygame.midi.get_device_info(i)
        print(f"{i}: {info[1]}, input({info[2]}), output({info[3]})")
        if "micro" in str(info[1]) and info[2] == 1:
            input = i
        elif "SH-4d" in str(info[1]) and info[3] == 1:
            output = i

    print(f"use input: {input}")
    print(f"use output: {output}")

    if input is None or output is None:
         return

    midiin = m.Input(input)
    midiout = m.Output(output)

    try:
        while True:
            if midiin.poll():
                event = midiin.read(1)[0][0]
                if event[0] == 144:
                    # midiout.note_on(event[1], event[2])
                    midiout.note_on(event[1], VEL)
                    print(event[1])
                elif event[0] == 128:
                    midiout.note_off(event[1])
            time.sleep(0.001)
    finally:
        # midiout.note_off(note)
        midiout.close()
        m.quit()

try:
    main()
finally:
    pygame.quit()
