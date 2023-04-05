import pygame
from Drawing.Rectangle import Rectangle
from Drawing.Tower import Tower

WIN_WIDTH = 1280
WIN_HEIGHT = 720

TABLE_WIDTH = 1000
TABLE_HEIGHT = 30

TOWERS_COUNT = 3
DISK_COUNT = 8
DISK_HEIGHT = 50

class Game:
    def __init__(self):
        self.table = None
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()
        pygame.quit()

    def draw(self):
        self.screen.fill("purple")

        self.table = Rectangle(1000, 30, [107, 63, 25])
        self.table.rect.centerx = int(WIN_WIDTH / 2)
        self.table.rect.centery = int(WIN_HEIGHT - TABLE_HEIGHT)

        self.towers = [Tower(TABLE_HEIGHT, (DISK_COUNT + 1) * DISK_HEIGHT, [107, 63, 25])
                       for i in range(TOWERS_COUNT)]

        for i in range(TOWERS_COUNT):
            self.towers[i].rect.centerx = int(WIN_WIDTH / (TOWERS_COUNT + 1)* (i + 1))
            self.towers[i].rect.bottom = WIN_HEIGHT - TABLE_HEIGHT #5 * MIN_SIZE


        pygame.draw.circle(self.screen, "red", self.player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= 300 * self.dt
        if keys[pygame.K_s]:
            self.player_pos.y += 300 * self.dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 300 * self.dt
        if keys[pygame.K_d]:
            self.player_pos.x += 300 * self.dt

        self.table.draw()
        for tower in self.towers:
            tower.draw()

        pygame.display.flip()

        self.dt = self.clock.tick(60) / 1000


# pygame.quit()

if __name__ == "__main__":
    Game().run()

