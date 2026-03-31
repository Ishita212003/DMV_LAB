import pygame
import sys

# -------- USER INPUT --------
try:
    width = int(input("Enter frame width: "))
    height = int(input("Enter frame height: "))
    speed = int(input("Enter circle speed (e.g., 2-10): "))
except ValueError:
    print("Invalid input! Using default values.")
    width, height, speed = 800, 600, 5

# -------- INITIAL SETUP --------
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle with Axes")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# Circle properties
x, y = width // 2, height // 2
radius = 20

# -------- MAIN LOOP --------
running = True
while running:
    screen.fill((0, 0, 0))  # black background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- KEYBOARD INPUT --------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # -------- DRAW AXES --------
    pygame.draw.line(screen, (255, 255, 255), (0, height//2), (width, height//2), 1)  # X-axis
    pygame.draw.line(screen, (255, 255, 255), (width//2, 0), (width//2, height), 1)  # Y-axis

    # -------- DRAW AXIS LABELS --------
    for i in range(0, width, 50):
        label = font.render(str(i - width//2), True, (255, 255, 255))
        screen.blit(label, (i, height//2 + 5))

    for j in range(0, height, 50):
        label = font.render(str(height//2 - j), True, (255, 255, 255))
        screen.blit(label, (width//2 + 5, j))

    # -------- DRAW CIRCLE --------
    pygame.draw.circle(screen, (0, 255, 0), (x, y), radius)

    # -------- DISPLAY POSITION --------
    pos_text = font.render(f"X: {x - width//2}, Y: {height//2 - y}", True, (255, 255, 0))
    screen.blit(pos_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()