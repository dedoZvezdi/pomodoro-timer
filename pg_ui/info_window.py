import pygame
from constants import *

class Info_window:
    def __init__(self):
        self.x = WIDTH // 2 - INFO_WIDTH // 2
        self.y = HEIGHT // 2 - INFO_HEIGHT // 4

    def show(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, INFO_WIDTH, INFO_HEIGHT))
        pygame.draw.rect(win, BLACK, (self.x, self.y, INFO_WIDTH, INFO_HEIGHT), 1)
