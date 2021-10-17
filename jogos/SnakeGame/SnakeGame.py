import pygame
from pygame.locals import *
import time
import random


SIZE = 50


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("resources/apple.png").convert()
        self.apple = pygame.transform.scale(self.apple, (50, 50))
        self.x = SIZE*14
        self.y = SIZE*11

    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 19)*SIZE
        self.y = random.randint(2, 15)*SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.block = pygame.transform.scale(self.block, (50, 50))
        self.background = pygame.image.load("resources/fundo.png")

        self.length = length
        self.x = [150]*length
        self.y = [200]*length
        self.direction = 'right'

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.blit(self.background, (0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game   By: UwUsca")

        self.surface = pygame.display.set_mode((1000, 800))
        pygame.mixer.init()
        self.play_bg_music("menumusic")
        self.background = pygame.image.load("resources/fundo.png")
        self.surface.blit(self.background, (0, 0))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play_bg_music(self, sound):
        pygame.mixer.music.load(f"resources/{sound}.mp3")
        pygame.mixer.music.play(-1)

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("eatsound")
            self.snake.increase_length()
            self.apple.move()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"
        if self.snake.x[0] < 0 or self.snake.x[0] >= 1000:
            raise "Game over"
        if self.snake.y[0] < 50 or self.snake.y[0] >= 800:
            raise "Game over"

    def display_score(self):
        font = pygame.font.SysFont('impact', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        font_out = pygame.font.SysFont('impact', 31)
        score_out = font_out.render(f"Score: {self.snake.length}", True, (0, 0, 0))
        self.surface.blit(score_out, (454, 5))
        self.surface.blit(score, (455, 6))

    def show_game_over(self):
        self.play_sound("deathsound")

        gameover = pygame.image.load("resources/gameover.png")
        self.surface.blit(gameover, (0, 0))
        font = pygame.font.SysFont('Impact', 48)
        line1 = font.render(f"{self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (630, 522))
        pygame.display.flip()
        pygame.mixer.music.pause()
        self.play_bg_music("gameovermusic")

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)

    def menu_screen(self):
        menu = pygame.image.load("resources/menu.png")
        self.surface.blit(menu, (0, 0))
        pygame.display.flip()

    def run(self):
        running = True
        pause = False
        menu = True

        while menu:
            self.menu_screen()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        pygame.mixer.music.pause()
                        self.play_bg_music("ingamemusic")
                        menu = False
                    if event.key == K_ESCAPE:
                        menu = False
                        pygame.quit()
                elif event.type == QUIT:
                    menu = False
                    pygame.quit()

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.pause()
                        pause = False
                        self.play_bg_music("ingamemusic")
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(.1)


if __name__ == '__main__':
    game = Game()
    game.run()