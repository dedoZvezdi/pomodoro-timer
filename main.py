import pygame
import os
from visuals import display_time, running_sonic_display, waiting_sonic_display

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 400
HEIGHT = 225
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
font1 = pygame.font.SysFont("Consolas", HEIGHT // 10)


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro")

study_seconds = 0
rest_seconds = 0

seconds_set = 0
seconds_remaining = seconds_set 
timer_stop = True
alarm_path = None
session = True # True for study session || False for pause session

def count_sprites(directory):
    items = os.listdir(directory)
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
    return len(files)

running_sprites_len = count_sprites(".//running_sonic")
waiting_sonic_len = count_sprites(".//waiting_sonic")


def draw_scene(win):
    win.fill(WHITE)
    display_time(win, session, font1, BLACK, WIDTH, seconds_remaining)
    if timer_stop:
        waiting_sonic_display(win, current_tick, waiting_sonic_len, WIDTH, HEIGHT,)
    else:
        running_sonic_display(win, current_tick , running_sprites_len, WIDTH, HEIGHT)
    pygame.display.update()

def toogle_timer(event):
    global timer_stop
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            timer_stop = not timer_stop
            pygame.mixer.music.stop()

def restart_timer(event):
    global timer_stop, seconds_set, seconds_remaining
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            timer_stop = True
            read_file()
            seconds_remaining = seconds_set
            pygame.mixer.music.stop()

def create_file():
    if not os.path.exists("time.txt"):
        with open("time.txt", "w") as file:
            file.write("0:30:0\n")
            file.write("0:10:0\n")
            file.write("alarm.wav")

def read_file():
    global study_seconds, rest_seconds, alarm_path
    with open("time.txt") as file:
        lines = file.readlines()

        study_time = list(map(int, lines[0].strip().split(":")))
        study_seconds = study_time[0] * 3600 + study_time[1] * 60 + study_time[2]

        rest_time = list(map(int, lines[1].strip().split(":")))
        rest_seconds = rest_time[0] * 3600 + rest_time[1] * 60 + rest_time[2]

        alarm_path = lines[2]
        pygame.mixer.music.load(alarm_path)


create_file()
read_file()
run = True
last_tick = pygame.time.get_ticks()

while run:
    current_tick = pygame.time.get_ticks()
    elapsed = (current_tick - last_tick) / 1000
    last_tick = current_tick
    if not timer_stop:
        seconds_remaining -= elapsed
    else:
        if session:
            seconds_remaining = study_seconds
        else:
            seconds_remaining = rest_seconds

    if seconds_remaining <= 0 and not timer_stop: # timer hasnt stopped yet, when idle
        session = not session

    if seconds_remaining <= 0:
        timer_stop = True
        seconds_remaining = seconds_set
        if alarm_path:
            pygame.mixer.music.play(-1)

    draw_scene(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        toogle_timer(event)
        restart_timer(event)

pygame.quit()