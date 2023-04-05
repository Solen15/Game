import pygame

from Drawing.Rectangle import Rectangle


class Tower(Rectangle):
    def __init__(self, width: int, height: int, color: tuple):
        super().__init__(width, height, color)

        self.disks = []

    def draw(self):
        ds = pygame.display.get_surface()

        outer_radius = int(self.rect.height / 2)
        pygame.draw.rect(ds, self.color, self.rect,
                         border_top_left_radius=outer_radius,
                         border_top_right_radius=outer_radius)

