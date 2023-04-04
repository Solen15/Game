import pygame


class Rectangle:
    def __init__(self, width: int, height: int, color: tuple):
        self.color = color
        self.rect = pygame.Rect(0, 0, width, height)

    def draw(self):
        ds = pygame.display.get_surface()

        pygame.draw.rect(ds, self.color, self.rect, border_radius=int(self.rect.height / 2))
