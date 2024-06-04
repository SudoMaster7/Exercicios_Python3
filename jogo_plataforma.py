import pygame
import random

# Inicializando o Pygame
pygame.init()

# Definindo as dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Plataforma")

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Definindo a taxa de frames
clock = pygame.time.Clock()
FPS = 60

# Classe do Jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT - 150)
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 0.3

    def update(self):
        self.speed_y += self.gravity
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Prevenindo que o jogador saia da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speed_y = 0

    def jump(self):
        if self.rect.bottom == SCREEN_HEIGHT:
            self.speed_y = -10

# Classe dos Obstáculos
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - 50

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

# Inicializando o jogador e os grupos de sprites
player = Player()
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

all_sprites.add(player)

for _ in range(3):
    obstacle = Obstacle()
    obstacle.rect.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 1000)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Função principal do jogo
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed_x = -5
                elif event.key == pygame.K_RIGHT:
                    player.speed_x = 5
                elif event.key == pygame.K_SPACE:
                    player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.speed_x < 0:
                    player.speed_x = 0
                elif event.key == pygame.K_RIGHT and player.speed_x > 0:
                    player.speed_x = 0

        all_sprites.update()

        # Detectando colisão
        if pygame.sprite.spritecollide(player, obstacles, False):
            running = False

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
