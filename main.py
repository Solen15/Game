import pygame
from Drawing.Rectangle import Rectangle


class Game:
    def __init__(self):
        self.table = None
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
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

        self.table = Rectangle(100, 30, [50,50,50])
        #self.bar.rect.centerx = int(WIN_WIDTH / 2)
        #self.bar.rect.top = self.towers[0].rect.bottom

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
        pygame.display.flip()

        self.dt = self.clock.tick(60) / 1000


# pygame.quit()

if __name__ == "__main__":
    Game().run()

