import pygame
import color_values

pygame.init()

screen = pygame.display.set_mode([300,450])
pygame.display.set_caption('Radix Idle Game')
background = color_values.black
framerate = 60
font = pygame.font.Font("freesansbold.ttf", 16)
timer =  pygame.time.Clock()


def draw_task(color, y_coord):
    pygame.draw.circle(screen,color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen,color, [70, y_coord - 15 ,200,30])
    pygame.draw.rect(screen, color_values.black, [75,y_coord - 10,198,20])
    value_text = font.render(str(value), True, color_values.white)
    screen.blit(value_text, (16,y_coord - 10))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background)
    draw_task(color_values.green, 50)
    draw_task(color_values.green, 110)
    draw_task(color_values.green, 50)
    draw_task(color_values.green, 50)
    draw_task(color_values.green, 50)
    pygame.display.flip()
pygame.quit()