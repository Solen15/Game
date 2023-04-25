import pygame

from Drawing.Rectangle import Rectangle
from Drawing.Disk import Disk


class Tower(Rectangle):
    def __init__(self, width: int, height: int, color: tuple):
        super().__init__(width, height, color)

        self.disks = []
        self.temp_disk = None

    def draw(self):
        ds = pygame.display.get_surface()

        outer_radius = int(self.rect.height / 2)
        pygame.draw.rect(ds, self.color, self.rect,
                         border_top_left_radius=outer_radius,
                         border_top_right_radius=outer_radius)

    def add_disk(self, disk: Disk):
        self.disks.append(disk)

    def pop_disk(self):
        return self.disks.pop(0)

    def get_midbottom(self, disk_height):
        return self.rect.midbottom[0], self.rect.midbottom[1] - disk_height * (len(self.disks) - 1)

    def disk_select(self):
        self.temp_disk = Disk[self.disks[-1].width - 3, self.disks[-1].height - 3, [200, 0, 0]] #TODO
