import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/target.jpg")
pygame.display.set_icon(icon)


target_image = pygame.image.load("img/target_duck.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
# add new functions
score = 0
misses = 0  # Добавляем переменную для учета промахов
font = pygame.font.SysFont(None, 36)

# Загрузка звуков
hit_sound = pygame.mixer.Sound("sounds/hit.wav")
miss_sound = pygame.mixer.Sound("sounds/miss.wav")

def draw_score_and_misses():
    score_text = font.render(f'Попал: {score}', True, (255, 255, 255))
    misses_text = font.render(f'Промах: {misses}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(misses_text, (10, 50))  # Отображаем количество промахов


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                score += 1  # Увеличить счёт
                hit_sound.play()  # Воспроизвести звук попадания
            else:
                misses += 1  # Увеличиваем количество промахов при промахе
                miss_sound.play()  # Воспроизвести звук промаха



    screen.blit(target_image, (target_x, target_y))
    draw_score_and_misses()
    pygame.display.update()



pygame.quit()

