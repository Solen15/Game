import pygame
from Drawing.Rectangle import Rectangle
from Drawing.Tower import Tower
from Drawing.Disk import Disk

WIN_WIDTH = 1280
WIN_HEIGHT = 720

TABLE_WIDTH = 1000
TABLE_HEIGHT = 30
TABLE_COLOR = [107, 63, 25]
TOWERS_COUNT = 3

DISK_COUNT = 8
DISK_HEIGHT = 50
DISK_COLORS = [
    (244, 67, 54),
    (156, 39, 176),
    (63, 81, 181),
    (3, 169, 244),
    (0, 150, 136),
    (139, 195, 74),
    (255, 235, 59),
    (255, 152, 0),
]


class Game:
    def __init__(self):
        self.table = None
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.selected_tower = None

        self.reset()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            #temp = self.towers[0].pop_disk()
            #self.towers[1].add_disk(temp)
        pygame.quit()

    def reset(self):
        self.table = Rectangle(1000, 30, TABLE_COLOR)
        self.table.rect.centerx = int(WIN_WIDTH / 2)
        self.table.rect.centery = int(WIN_HEIGHT - TABLE_HEIGHT)

        self.towers = [Tower(TABLE_HEIGHT, (DISK_COUNT + 1) * DISK_HEIGHT, TABLE_COLOR)
                       for i in range(TOWERS_COUNT)]

        for i in range(TOWERS_COUNT):
            self.towers[i].rect.centerx = int(WIN_WIDTH / (TOWERS_COUNT + 1) * (i + 1))
            self.towers[i].rect.bottom = self.table.rect.top

        self.disks = [Disk(int(WIN_WIDTH / (TOWERS_COUNT + 1) - 30 * i), DISK_HEIGHT, DISK_COLORS[i])
                      for i in range(DISK_COUNT)]

        for disk in self.disks:
            self.towers[0].add_disk(disk)
            disk.rect.midbottom = self.towers[0].get_midbottom(DISK_HEIGHT)

        self.selected_tower = 0

        self.towers[self.selected_tower].disk_select()


    def draw(self):

        self.screen.fill("purple")
        self.table.draw()

        for tower in self.towers:
            tower.draw()
            if tower.temp_disk:
                tower.temp_disk.draw()

        for disk in self.disks:
            disk.draw()

        for tower in self.towers:
            #tower.draw()
            if tower.temp_disk:
                tower.temp_disk.draw()

        pygame.display.flip()


if __name__ == "__main__":
    Game().run()
