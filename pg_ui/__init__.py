import pygame
import os
import sys
from visuals import display_time, running_sonic_display, waiting_sonic_display, display_circle
from constants import *

class Pg_window:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.font1 = pygame.font.SysFont("Consolas", HEIGHT // 10)
        self.icon = pygame.image.load("icon.ico")

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pomodoro")
        pygame.display.set_icon(self.icon)

        self.study_seconds = 0
        self.rest_seconds = 0
        
        self.seconds_set = 0
        self.seconds_remaining = self.seconds_set 
        self.timer_stop = True
        self.alarm_path = None
        self.session = True # True for study session || False for pause session
        self.config_file = "config.txt"

        self.running_sprites_len = self.count_sprites(".//visuals//running_sonic")
        self.waiting_sonic_len = self.count_sprites(".//visuals//waiting_sonic")

    def count_sprites(self, directory):
        items = os.listdir(directory)
        files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
        return len(files)

    def draw_scene(self, current_tick):
        self.window.fill(WHITE)
        display_circle(self.window, BLUE, WIDTH, HEIGHT, self.seconds_remaining, self.seconds_set)
        display_time(self.window, self.session, self.font1, BLACK, WIDTH, self.seconds_remaining)
        if self.timer_stop:
            waiting_sonic_display(self.window, current_tick, self.waiting_sonic_len, WIDTH, HEIGHT)
        else:
            running_sonic_display(self.window, current_tick , self.running_sprites_len, WIDTH, HEIGHT)
        pygame.display.update()

    def toogle_timer(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.timer_stop = not self.timer_stop
                pygame.mixer.music.stop()

    def restart_timer(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.timer_stop = True
                self.read_file()
                if self.session:
                    self.seconds_set = self.study_seconds
                else:
                    self.seconds_set = self.rest_seconds
                self.seconds_remaining = self.seconds_set
                pygame.mixer.music.stop()

    def switch_session(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.timer_stop = True
                self.session = not self.session
                if self.session:
                    self.seconds_set = self.study_seconds
                else:
                    self.seconds_set = self.rest_seconds
                self.seconds_remaining = self.seconds_set

    def create_file(self):
        if not os.path.exists(self.config_file):
            with open(self.config_file, "w") as file:
                file.write("0:30:0\n")
                file.write("0:10:0\n")
                file.write(alarm_file)

                file.write("\n\n\nThe purpouse of this file is to set time for study and rest session.\n\
User can also write path of the .wav or .mp3 file that will be played after timer finishes. (third row)\n\
If the path isn't specifed default alaram sound will be played.\n\n\
Setting up time:\n\
First row represent study session.\nSecond row is time for rest session.\n\
Time must be writen in this format => hour:minutes:seconds (\":\" is separator for integers).\n\n\
Pause the timer -> SPACE\nRestart the timer by reading new values -> ENTER KEYS\n\
Change session -> LEFT ARROW, RIGHT ARROW\n\n\
This file will automaticly be created after deletion.\n\
If user accidently delete instruction, they can be restored with deleting this file.\n")

    def read_file(self):
        self.create_file()
        with open(self.config_file, "r") as file:
            lines = file.readlines()
            try:
                study_time = list(map(int, lines[0].strip().split(":")))
                self.study_seconds = study_time[0] * 3600 + study_time[1] * 60 + study_time[2]
            except ValueError:
                self.study_seconds = 0

            try:
                rest_time = list(map(int, lines[1].strip().split(":")))
                self.rest_seconds = rest_time[0] * 3600 + rest_time[1] * 60 + rest_time[2]
            except ValueError:
                self.rest_seconds = 0

            try:
                self.alarm_path = lines[2][:len(lines[2]) - 1] # [:len(lines[2]) - 1] for \n at the end
            except IndexError:
                self.alarm_path = alarm_file
            except pygame.error:
                self.alarm_path = alarm_file
            pygame.mixer.music.load(self.alarm_path)

            self.seconds_set = self.study_seconds
            self.seconds_remaining = self.study_seconds # program starts with study sessions
            if self.seconds_remaining > 24 * 3600:
                self.seconds_remaining = 24 * 3600
                self.seconds_set = 24 * 3600

    def edit_file(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.timer_stop = True
                self.session = True
                self.seconds_set = self.study_seconds
                self.seconds_remaining = self.seconds_set
                self.create_file()
                file_name = self.config_file
                if sys.platform == "win32":
                    os.startfile(file_name)
                elif sys.platform == "darwin":
                    os.system(f"open {file_name}")
                else:
                    os.system(f"xdg-open {file_name}")

    def play_alarm(self):
        self.seconds_remaining = self.seconds_set
        if self.alarm_path:
            pygame.mixer.music.play(-1)

    def show(self):
        self.create_file()
        self.read_file()
        run = True
        last_tick = pygame.time.get_ticks()

        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            current_tick = pygame.time.get_ticks()
            elapsed = (current_tick - last_tick) / 1000
            last_tick = current_tick
            if not self.timer_stop:
                self.seconds_remaining -= elapsed

            if self.seconds_remaining <= 0 and not self.timer_stop: # timer hasnt stopped yet, when idle
                self.play_alarm()

                self.session = not self.session
                self.timer_stop = True
                if self.session:
                    self.seconds_remaining = self.study_seconds
                    self.seconds_set = self.study_seconds
                else:
                    self.seconds_remaining = self.rest_seconds
                    self.seconds_set = self.rest_seconds

            self.draw_scene(current_tick)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.toogle_timer(event)
                self.restart_timer(event)
                self.switch_session(event)
                self.edit_file(event)

        pygame.quit()