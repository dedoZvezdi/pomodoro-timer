import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60
clock = pygame.time.Clock()
font1 = pygame.font.SysFont("Consolas", HEIGHT // 20)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pomodoro")

seconds_set = 0
seconds_reimaning = seconds_set 
timer_stop = True
alarm_path = None

def display_time(win):
    hours = seconds_reimaning // 3600
    minutes = (seconds_reimaning - hours * 3600) // 60
    seconds = (seconds_reimaning - hours * 3600 - minutes * 60)
    msg = font1.render(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}", True, BLACK)
    win.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - msg.get_height() // 2))

def draw_scene(win):
    win.fill(WHITE)
    display_time(win)
    pygame.display.update()

def toogle_timer(event):
    global timer_stop
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            timer_stop = not timer_stop
            pygame.mixer.music.stop()

def restart_timer(event):
    global timer_stop, seconds_set, seconds_reimaning
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            timer_stop = True
            read_file()
            seconds_reimaning = seconds_set
            pygame.mixer.music.stop()

def create_file():
    with open("time.txt", "w") as file:
        file.write("0:0:5\n")
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
while run:
    clock.tick(FPS)
    if not timer_stop:
        seconds_reimaning -= 1 / 60 # it works with FPS=1, but secondary thread need for checking for exit

    if seconds_reimaning <= 0:
        timer_stop = True
        seconds_reimaning = seconds_set
        if alarm_path:
            pygame.mixer.music.play(-1)

    draw_scene(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        toogle_timer(event)
        restart_timer(event)

pygame.quit()