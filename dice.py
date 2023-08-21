import pygame
import random
import os

# Initialize Pygame and create a pygame window
pygame.init()
width, height = 520, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dice Simulator")

# Define some colors
WHITE = (255, 255, 255)
GREEN = (53, 101, 77)

# Initialize fonts
SMALL_FONT = pygame.font.Font(None, 36)

# Include images using the os module and create a function to draw a window when it calls
def draw_window(dice, index):
    Dice_Image = pygame.image.load(os.path.join('images', 'd{}.png'.format(index)))
    text_for_Space = SMALL_FONT.render('Press space Bar', True, WHITE)
    text_for_OR = SMALL_FONT.render('OR', True, WHITE)
    text_for_Click = SMALL_FONT.render('Click on dice to Roll', True, WHITE)
    win.fill(GREEN)
    win.blit(text_for_Space, (175, 10))
    win.blit(text_for_OR, (235, 35))
    win.blit(text_for_Click, (165, 60))
    win.blit(pygame.transform.scale(Dice_Image, (200, 200)), (dice.x, dice.y))
    pygame.display.update()

# Main Function
def main():
    dice = pygame.Rect(160, 150, 200, 200)
    n = 1
    clock = pygame.time.Clock()
    FPS = 30  # Add this line to define the frames per second
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # Fix the indentation here
                pygame.quit()  # Fix the missing pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    n = random.randrange(1, 7)
                    draw_window(dice, n)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if dice.collidepoint(mouse_pos):
                    n = random.randrange(1, 7)
                    draw_window(dice, n)
        draw_window(dice, n)
        clock.tick(FPS)  # Move clock.tick(FPS) inside the loop

if __name__ == "__main__":
    main()  # Add this line to call the main function when the script is run
