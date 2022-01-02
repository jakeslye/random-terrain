import pygame
import time
import random

WIDTH = 1800
HEIGHT = 900
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

MULTIPLIER = 10
SMOOTHING = 0.5

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.Font("freesansbold.ttf", 32)
pygame.display.set_caption("generation")

clock = pygame.time.Clock()

nums = [random.randint(0, 500) + 1 * MULTIPLIER]
i = 0
length = len(nums)

while length < 1800:
    nums.append(random.randint(abs(nums[i] - 1 * MULTIPLIER), nums[i] + 1 * MULTIPLIER))
    length = len(nums)
    i += 1

length = len(nums)

time = pygame.time.get_ticks()
text = font.render("Generation time: " + str(time / 1000), True, WHITE, BLUE)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                timer = pygame.time.Clock()

                nums = [random.randint(0, 500)]
                i = 0
                length = len(nums)

                while length < 1800:
                    nums.append(random.randint(abs(nums[i] - 1 * MULTIPLIER), nums[i] + 1 * MULTIPLIER))
                    length = len(nums)
                    i += 1

                length = len(nums)

                text = font.render("", True, WHITE)

    screen.fill(BLACK)

    for i in range(length):
        print(i)
        screen.blit(text, (5, 5))
        pygame.draw.rect(screen, BLUE, pygame.Rect(1 * i, HEIGHT - SMOOTHING * nums[i], 1, SMOOTHING * nums[i]))
    pygame.display.flip()
pygame.quit()