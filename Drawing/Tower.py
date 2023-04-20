import pygame

from Drawing.Rectangle import Rectangle
from Drawing.Disk import Disk


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


    def add_disk(self, disk: Disk):
        self.disks.append(disk)

    def pop_disk(self):
        return self.disks.pop()

