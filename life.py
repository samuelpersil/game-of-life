import pygame
from random import randint

pygame.init()

# Main variables
WIDTH, HEIGHT = 800, 600
MAIN_FPS = 60
AUTO_FPS = 10
square_size = 20
auto = -1 # -1 for disabled, 1 for enabled

# Color variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Screen initializing
wn = pygame.display.set_mode((WIDTH,HEIGHT))
wn.fill(BLACK)
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

# The class for each square in the grid
class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = -1
        self.rect = pygame.Rect(self.x*square_size, self.y*square_size, square_size, square_size)

    def draw_square(self):
        if self.color == -1:
            pygame.draw.rect(wn, WHITE, self.rect, 0)

        else:
            pygame.draw.rect(wn, GREEN, self.rect, 0)
        pygame.draw.line(wn, BLACK, (self.x*square_size, self.y*square_size), ((self.x+1)*square_size, self.y*square_size))
        pygame.draw.line(wn, BLACK, (self.x*square_size, self.y*square_size), (self.x*square_size, (self.y+1)*square_size))

# Creating the matrix of the positions
squares = []
def create_squares():
    for y in range(int(HEIGHT/square_size)):
        for x in range(int(WIDTH/square_size)):
            square = Square(x,y)
            squares.append(square)

# Drawing positions
def show_squares():
    for objeto in squares:
        objeto.draw_square()

# If a square is clicked
def is_clicked():
    for objeto in squares:
        if objeto.rect.collidepoint(pygame.mouse.get_pos()):
            objeto.color *= -1

# Matrix of the neighbors alive
def find_neighbors():
    global neighborhood
    neighborhood = []
    for y in range(int(HEIGHT/square_size)):
        line = []
        for x in range(int(WIDTH/square_size)):
            neighbor = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
            neighbors_alive = 0

            for z in neighbor:

                # If it's out of matrix's range
                if z[0] >= (WIDTH/square_size) or z[0] < 0 or z[1] >= (HEIGHT/square_size) or z[1] < 0:
                    pass

                else:
                    if squares[z[0] + z[1] * (int(WIDTH/square_size))].color == 1:
                        neighbors_alive += 1
            line.append(neighbors_alive)
        neighborhood.append(line)

# Life or Death
def LoD():
    for objeto in range(len(squares)):
        atual = squares[objeto]
        if atual.color == 1 and (neighborhood[atual.y][atual.x] >= 4 or neighborhood[atual.y][atual.x] <= 1) or (): # Gonna die
            atual.color *= -1
        if atual.color == -1 and neighborhood[atual.y][atual.x] == 3:
            atual.color *= -1

# Controls what happens at each generation
def generation():
    find_neighbors()
    LoD()

# Reset
def reset():
    global auto
    for objeto in squares:
        objeto.color = -1
    if auto == 1:
        auto *= -1

# Random
def random():
    for objeto in squares:
        if randint(0,1) == 1:
            objeto.color = 1
        else:
            objeto.color = -1

# Main loop
FPS = MAIN_FPS
create_squares()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): # Quit game
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # Clicks in a square
            is_clicked()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a: # Enable/Disable "auto" function
            if auto == 1:
                FPS = MAIN_FPS
            else:
                FPS = AUTO_FPS
            auto *= -1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Pass a generation
            generation()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t:
            random()

    if auto == 1: # If "auto" function is enabled
        generation()
    show_squares()
    clock.tick(FPS)
    pygame.display.update()
