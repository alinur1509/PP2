import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 570
speed = 7



font_score = pygame.font.SysFont('Arial', 36, True, True)
font_end = pygame.font.SysFont('Arial', 56, True, True)


class Block(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.rect.y += 1
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()


class Block2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

    def reset_pos_eat(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.rect.y += random.randint(-1, 2)
        # self.rect.y = random.randint(-1, 1)
        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos_eat()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.key.get_pressed()
        if pos[pygame.K_LEFT]:
            self.rect.x -= speed
        elif pos[pygame.K_RIGHT]:
            self.rect.x += speed
        elif pos[pygame.K_UP]:
            self.rect.y -= speed
        elif pos[pygame.K_DOWN]:
            self.rect.y += speed


class Game(object):

    def __init__(self):
        self.score = 0
        self.game_over = False

        self.block_list = pygame.sprite.Group()
        self.block_list_eat = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        for i in range(50):
            block = Block()
            block_eat = Block2()

            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            block_eat.rect.x = random.randrange(SCREEN_WIDTH)
            block_eat.rect.y = random.randrange(-300, SCREEN_HEIGHT)

            self.block_list.add(block)
            self.all_sprites_list.add(block)

            self.block_list_eat.add(block_eat)
            self.all_sprites_list.add(block_eat)

        self.player = Player()
        self.all_sprites_list.add(self.player)

    def process_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
                  

        return False

    def run_logic(self):

        if not self.game_over:
            self.all_sprites_list.update()

            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
            blocks_hit_list_eat = pygame.sprite.spritecollide(self.player, self.block_list_eat, True)

            for block in blocks_hit_list:
                self.score -= 1
       
            for block in blocks_hit_list_eat:
                self.score += 1
        

            if len(self.block_list_eat) == 0:
                self.game_over = True
     
            elif self.score <= -10:
                self.game_over = True
      
    def display_frame(self, screen):

        screen.fill(WHITE)
        render_score = font_score.render(f'Your score: {self.score}', True, pygame.Color('blue'))
        screen.blit(render_score, (5, 5))
        if self.game_over:
            font = pygame.font.SysFont("Arial", 25)
            text = font.render("Game Over, click to restart", True, BLACK)
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])

        if not self.game_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


def main():

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Hungry lion by ALINUR")

    clock = pygame.time.Clock()

    game = Game()

    done = False
    while not done:
        done = game.process_events()

        game.run_logic()

        game.display_frame(screen)

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()