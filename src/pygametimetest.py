import pygame
import time

TICK = 60
SIM_MULTIPLIER = 1
SPEED = 500
TIME_STEP = 1 / TICK / SIM_MULTIPLIER * SPEED

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 20)
running = True

real_time_elapsed = 0.0
sim_time_elapsed = 0.0
start_time = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for _ in range(SIM_MULTIPLIER):
        sim_time_elapsed += TIME_STEP

    real_time_elapsed = time.time() - start_time
    fps = clock.get_fps()

    screen.fill("purple")

    lines = [
        f"FPS:      {fps:.1f}",
        f"Real:     {real_time_elapsed:.2f}s",
        f"Sim:      {sim_time_elapsed:.2f}s",
        f"Speed:    {SPEED}x  |  Mult: {SIM_MULTIPLIER}  |  dt: {TIME_STEP:.6f}s",
    ]
    for i, line in enumerate(lines):
        surf = font.render(line, True, (255, 255, 255))
        screen.blit(surf, (10, 10 + i * 24))

    pygame.display.flip()
    clock.tick(TICK)

pygame.quit()
