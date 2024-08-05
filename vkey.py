import pygame
import pygame.midi
from pygame.locals import *

INSTRUMENT = 3  # 楽器の種類 (0-127)
KEY_WIDTH = 20  # 鍵盤の幅
WIDTH, HEIGHT = 800, 128  # 画面の大きさ

FPS = 60
NOTE_CENTER = 60  # 中央の音。C(ド)の音を指定
COLOR = 0, 255, 200  # 色
WHITE_COLOR = 255, 255, 255  # 白鍵の色
BLACK_COLOR = 0, 0, 50  # 黒鍵の色
BG_COLOR = 100, 0, 50  # 背景色

KEY_COLOR = 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0  # 0=白鍵, 1=黒鍵
NOTE_NAME = ('C', 'C#', 'D', 'D#', 'E',
             'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')


def main():
    pygame.init()
    pygame.midi.init()

    count = pygame.midi.get_count()
    print("get_default_input_id:%d" % pygame.midi.get_default_input_id())
    print("get_default_output_id:%d" % pygame.midi.get_default_output_id())
    print("No:(interf, name, input, output, opened)")
    for i in range(count):
        print("%d:%s" % (i, pygame.midi.get_device_info(i)))

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    midiout = pygame.midi.Output(4)
    midiout.set_instrument(INSTRUMENT)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    keys = WIDTH // KEY_WIDTH + 1
    keylist = [False] * (keys + 7)
    note_start = NOTE_CENTER - keys // 2
    note_no = None
    vel = 0
    sustain = False
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                return
            elif e.type == KEYDOWN and e.key is K_ESCAPE:
                return
            elif e.type == KEYDOWN and e.key is K_SPACE:
                sustain = True
            elif e.type == KEYUP and e.key is K_SPACE:
                sustain = False
                note_no = None
                for key, b in enumerate(keylist):
                    if b:
                        midiout.note_off(note_start + key, 0)
                        keylist[key] = False
            elif e.type == MOUSEBUTTONDOWN and (
                            e.button == 1 or e.button == 3):
                x, y = e.pos
                vel = 128 * y // HEIGHT
                key = x // KEY_WIDTH
                keylist[key] = True
                note_no = note_start + key
                midiout.note_on(note_no, vel)
                if e.button == 3:
                    keylist[key + 7] = True
                    midiout.note_on(note_no + 7, vel)
            elif e.type == MOUSEBUTTONUP and (
                            e.button == 1 or e.button == 3):
                if not sustain:
                    note_no = None
                    for key, b in enumerate(keylist):
                        if b:
                            midiout.note_off(note_start + key, 0)
                            keylist[key] = False

        screen.fill(BG_COLOR)
        for key in range(keys):
            x = key * KEY_WIDTH
            pygame.draw.rect(
                screen,
                (WHITE_COLOR, BLACK_COLOR)[
                    KEY_COLOR[(note_start + key) % 12]],
                (x + 1, 0, KEY_WIDTH - 2, HEIGHT))
            if keylist[key]:
                pygame.draw.rect(
                    screen, COLOR, (x, 0, KEY_WIDTH, HEIGHT), 3)
        clock.tick(FPS)
        pygame.display.flip()
        notes = []
        for key, b in enumerate(keylist):
            if b:
                nn = note_start + key
                notes.append('{0}:{1}'.format(NOTE_NAME[nn % 12], nn))
        pygame.display.set_caption(', '.join(notes))

try:
    main()
finally:
    pygame.quit()
