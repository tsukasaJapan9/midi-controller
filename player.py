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

# melody = [
#     (60, 1), (64, 1), (67, 1), (69, 1), # C, E, G, A
#     (67, 1), (64, 1),                   # G, E
#     (62, 1), (64, 1), (60, 1), (62, 1), # D, E, C, D
#     (60, 2)                             # C (長い音)
# ]

# melody = [
#     (71, 1), (74, 0.5), (76, 0.5), (77, 1), # B, D, E, F#
#     (76, 1), (74, 1),                       # E, D
#     (71, 1), (76, 1), (74, 1), (71, 1),     # B, E, D, B
#     (69, 2)                                 # A (長い音)
# ]

# melody = [
#     (68, 1), (72, 1), (75, 0.5), (73, 0.5), # Ab, C, Eb, Db
#     (72, 1), (70, 1),                       # C, Bb
#     (68, 1), (70, 1), (72, 1), (68, 1),     # Ab, Bb, C, Ab
#     (65, 2)                                 # F (長い音)
# ]

# melody = [
#     (69, 1), (71, 0.5), (72, 0.5), (74, 1), # A, B, C, D
#     (72, 1), (71, 1),                       # C, B
#     (69, 1), (67, 1), (69, 1), (67, 1),     # A, G, A, G
#     (65, 2)                                 # F (長い音)
# ]

# melody = [
#     (65, 1), (67, 1), (70, 1), (72, 2),   # F, G, Bb, C
#     (70, 1), (68, 1), (67, 2),            # Bb, A, G
#     (65, 1), (67, 1), (68, 1), (70, 1.5), # F, G, A, Bb
#     (68, 1.5), (65, 1)                    # A, F
# ]

# melody = [
#     (69, 1), (71, 0.5), (72, 0.5), (74, 1), # A, B, C, D
#     (72, 1), (71, 1),                       # C, B
#     (69, 1), (67, 1), (69, 1), (67, 1),     # A, G, A, G
#     (65, 2)                                 # F (長い音)
# ]

# melody = [
#     (62, 1), (64, 0.5), (66, 0.5), (67, 1), # D, E, F#, G
#     (66, 1), (64, 1),                       # F#, E
#     (62, 1), (61, 1), (62, 1), (61, 1),     # D, C#, D, C#
#     (59, 2)                                 # B (長い音)
# ]

# melody = [
#     (64, 1), (64, 1), (64, 1), (62, 1), (60, 2),  # E, E, E, D, C
#     (64, 1), (64, 1), (64, 1), (62, 1), (60, 2),  # E, E, E, D, C
#     (60, 1), (64, 1), (67, 1), (67, 0.5), (69, 0.5),  # C, E, G, G, A
#     (67, 1), (64, 1), (62, 1), (60, 2),  # G, E, D, C
    
#     (64, 1), (64, 1), (64, 1), (62, 1), (60, 2),  # E, E, E, D, C
#     (64, 1), (64, 1), (64, 1), (62, 1), (60, 2),  # E, E, E, D, C
#     (60, 1), (64, 1), (67, 1), (67, 0.5), (69, 0.5),  # C, E, G, G, A
#     (67, 1), (64, 1), (62, 1), (60, 2)  # G, E, D, C
# ]

melody = [
    (65, 1), (67, 1), (69, 1.5), (70, 0.5), # F, G, A, Bb
    (69, 1), (67, 1), (65, 2),              # A, G, F
    (67, 1), (69, 1), (70, 1.5), (72, 0.5), # G, A, Bb, C
    (70, 1), (69, 1), (67, 2)               # Bb, A, G
]


def main():
    m.init()
    for i in range(pygame.midi.get_count()):
        info = pygame.midi.get_device_info(i)
        print(f"{i}: {info[1]}, input({info[2]}), output({info[3]})")

    
    midiouts = [m.Output(4), m.Output(6)]

    try:
        for note, duration in melody:
            for out in midiouts:
                out.note_on(note, VEL)
            time.sleep(duration*0.5)
            for out in midiouts:
                out.note_off(note)
    finally:
        for out in midiouts:
            out.note_off(note)
            out.close()
        m.quit()

try:
    main()
finally:
    pygame.quit()
