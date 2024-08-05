import time

import pygame
import pygame.midi as m
from pygame.locals import *

INSTRUMENT = 1  # 楽器の種類 (0-127)
NOTE_CENTER = 60  # 中央の音。C(ド)の音を指定
NOTE_NAME = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
VEL = 127

"""
プロンプト例

フォーマットはpythonのリスト形式で以下のようにお願いします
---
melody = [
    (note, length),  # note
]
"""

melody = [
    ([64, 71, 67], 2),
    ([65, 62, 69], 2),
    ([64, 60, 67], 4)
]


def main():
    m.init()
    for i in range(pygame.midi.get_count()):
        info = pygame.midi.get_device_info(i)
        print(f"{i}: {info[1]}, input({info[2]}), output({info[3]})")


    midiouts = [m.Output(4)]

    try:
        for note, duration in melody:
            for out in midiouts:
                if isinstance(note, list):
                    for n in note:
                        out.note_on(n, VEL)
                else:
                    out.note_on(note, VEL)

            time.sleep(duration)

            for out in midiouts:
                if isinstance(note, list):
                    for n in note:
                        out.note_off(n)
                else:
                    out.note_off(note)
    finally:
        for out in midiouts:
            if isinstance(note, list):
                for n in note:
                    out.note_off(n)
            else:
                out.note_off(note)
            out.close()
        m.quit()

try:
    main()
finally:
    pygame.quit()
