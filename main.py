import pygame
import os

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

seconds_set = 0
seconds_remaining = seconds_set 
timer_stop = True
alarm_path = None

def count_sprites(directory):
    items = os.listdir(directory)
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
    return len(files)

running_sprites_len = count_sprites(".//running_sonic")
waiting_sonic_len = count_sprites(".//waiting_sonic")

def display_time(win):
    hours = seconds_remaining // 3600
    minutes = (seconds_remaining - hours * 3600) // 60
    seconds = (seconds_remaining - hours * 3600 - minutes * 60)
    msg = font1.render(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}", True, BLACK)
    win.blit(msg, (WIDTH // 2 - msg.get_width() // 2, msg.get_height() // 2))

def running_sonic_display(win):
    index = int(current_tick / 60 % running_sprites_len) + 1
    try:
        running_sonic = pygame.image.load(f"running_sonic//{index}_r.png")
        win.blit(running_sonic, (WIDTH // 2 - running_sonic.get_width() // 2, HEIGHT - running_sonic.get_height() - 10))
    except pygame.error:
        print(f"Image {index}_r.png missing!")

def waiting_sonic_display(win):
    index = int(current_tick / 60 % waiting_sonic_len)
    try:
        waiting_sonic = pygame.image.load(f"waiting_sonic//{index}_w.png")
        scaled_image = pygame.transform.scale(waiting_sonic, (128, 144))
        win.blit(scaled_image, (WIDTH // 2 - scaled_image.get_width() // 2, HEIGHT - scaled_image.get_height() - 10))
    except pygame.error:
        print(f"Image {index}_w.png missing!")

def draw_scene(win):
    win.fill(WHITE)
    display_time(win)
    if timer_stop:
        waiting_sonic_display(win)
    else:
        running_sonic_display(win)
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
            file.write("alarm.wav")

def read_file():
    global seconds_set, alarm_path
    with open("time.txt") as file:
        lines = file.readlines()
        time = list(map(int, lines[0].strip().split(":")))
        seconds_set = time[0] * 3600 + time[1] * 60 + time[2]
        alarm_path = lines[1]
        pygame.mixer.music.load(alarm_path)


create_file()
run = True
last_tick = pygame.time.get_ticks()

while run:
    current_tick = pygame.time.get_ticks()
    if not timer_stop:
        elapsed = (current_tick - last_tick) / 1000
        seconds_remaining -= elapsed
        last_tick = current_tick
        

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