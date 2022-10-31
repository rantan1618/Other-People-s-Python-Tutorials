import pygame

pygame.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
purple = (127,0,255)
orange = (255,165,0)


screen = pygame.display.set_mode([300,450])
pygame.display.set_caption('Radix Idle Game')
background = black
framerate = 60
font = pygame.font.Font("freesansbold.ttf", 16)
timer =  pygame.time.Clock()

# game variables
green_value = 1
red_value = 2
orange_value = 3
white_value = 4
purple_value = 5
draw.green = False
draw.red = False
draw.orange = False
draw.white = False
draw.purple = False
red_length =  


def draw_task(color, y_coord, value, draw, length, speed):
    if draw and length < 200:
        length += speed
    pygame.draw.circle(screen,color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen,color, [70, y_coord - 15 ,200,30])
    pygame.draw.rect(screen, black, [75,y_coord - 10,198,20])
    value_text = font.render(str(value), True, white)
    screen.blit(value_text, (16,y_coord - 10))



running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background)
    
    draw_task(green, 50, green_value)
    draw_task(red, 110, red_value)
    draw_task(orange, 170, orange_value)
    draw_task(white, 230, white_value)
    draw_task(purple, 290, purple_value)
    pygame.display.flip()
pygame.quit()