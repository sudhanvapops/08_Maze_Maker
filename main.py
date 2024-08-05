import pygame
from sys import exit

pygame.init()

width, height = 425, 425
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Generator")
clock = pygame.time.Clock()

# Variables
WID,HIG = 400,400
row,col = 10,10
row_cell_size,col_cell_size = WID//row, HIG//col

# Functions
def draw_maze():

    for i in range(row+1):
        pygame.draw.line(screen,"White",(10,(row_cell_size*i)+10),(WID+10,(row_cell_size*i)+10))
    for i in range(col+1):
        pygame.draw.line(screen,"White",((col_cell_size*i)+10,10),((col_cell_size*i)+10,HIG+10))

while True:
    screen.fill("Black")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    draw_maze()

    pygame.display.update()
    clock.tick(60)