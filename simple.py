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

# melody = [
#     # Verse
#     (60, 1), (62, 1), (64, 1), (67, 1), # C, D, E, G
#     (64, 1), (60, 1),                   # E, C
#     (65, 1), (64, 1), (62, 1), (60, 1), # F, E, D, C
#     (62, 1), (67, 1),                   # D, G

#     # Chorus
#     (67, 1), (69, 1), (71, 1),          # G, A, B
#     (72, 1), (71, 1), (69, 1),          # C, B, A
#     (65, 1), (64, 1), (62, 1),          # F, E, D
#     (60, 1), (64, 1), (67, 1)           # C, E, G
# ]

melody = [
    (60, 1), (64, 1), (67, 1), (69, 1), # C, E, G, A
    (67, 1), (64, 1),                   # G, E
    (62, 1), (64, 1), (60, 1), (62, 1), # D, E, C, D
    (60, 2)                             # C (長い音)
]

def main():
    m.init()
    for i in range(pygame.midi.get_count()):
        print("%d:%s" % (i, pygame.midi.get_device_info(i)))

    midiout = m.Output(4)
    midiout.set_instrument(INSTRUMENT)

    try:
        for note, duration in melody:
            midiout.note_on(note, VEL)
            time.sleep(duration)
            midiout.note_off(note)
    finally:
        midiout.note_off(note)
        midiout.close()
        m.quit()

try:
    main()
finally:
    pygame.quit()
