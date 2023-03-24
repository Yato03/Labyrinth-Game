import sys, pygame
from read_file import read_file

pygame.init()

witdh = 500

size = (witdh,witdh)
fps = 30

win = False

#COLORES
BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 100, 255, 100
BLUE = 100, 100, 255
RED = 255, 100, 100

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
num_levels = 2 #Cambiar dependiendo de la cantidad de niveles que se tengan

current_level = 1
level = read_file("levels/level{}.txt".format(current_level))
num_cells = level[3]
cell_size = witdh/num_cells


player = list(level[2][0])
player_size = cell_size//2
velocity = 1

goal = level[2][1]
goal_size = cell_size//2       

acum_x = 0
acum_y = 0

def check_collision(player, level, acum_x, acum_y):
    for obs_derecha in level[0]:
        if player[0] == obs_derecha[0] and player[1] == obs_derecha[1]+1 and acum_x > 0 or player[0] == obs_derecha[0] and player[1] == obs_derecha[1] and acum_x < 0:
            return True
    for obs_abajo in level[1]:
        if player[0] == obs_abajo[0]+1 and player[1] == obs_abajo[1] and acum_y > 0 or player[0] == obs_abajo[0] and player[1] == obs_abajo[1] and acum_y < 0:
            return True
    if player[1] >= num_cells or player[1] < 0 or player[0] >= num_cells or player[0] < 0:
        return True
    return False

def goToLevel(l):
        global current_level, num_cells, cell_size, player, player_size, velocity, goal, goal_size, acum_x, acum_y, win, level
        current_level = l
        level = read_file("levels/level{}.txt".format(current_level))
        num_cells = level[3]
        cell_size = witdh/num_cells
        player = list(level[2][0])
        player_size = cell_size//2
        goal = level[2][1]
        goal_size = cell_size//2       
        acum_x = 0
        acum_y = 0
        win = False

while True:

    #LÓGICA
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == ord('r'):
                    player = list(level[2][0])
                    acum_x = 0
                    acum_y = 0
                    win = False
            if event.key == ord('q') and win and current_level == num_levels:
                    goToLevel(1)
            if acum_x == 0 and acum_y == 0:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                        acum_x = -velocity
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                        acum_x = velocity
                elif event.key == pygame.K_UP or event.key == ord('w'):
                        acum_y = -velocity
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                        acum_y = velocity
                
    player[1] += acum_x
    player[0] += acum_y

    if check_collision(player, level, acum_x, acum_y):
        player[1] -= acum_x
        player[0] -= acum_y
        acum_x = 0
        acum_y = 0

    if player[0] == goal[0] and player[1] == goal[1]:
        win = True

    #DIBUJO
    screen.fill(WHITE)

    if not win:
        for obs_derecha in level[0]:
                x = obs_derecha[1]*cell_size + cell_size
                y = obs_derecha[0]*cell_size
                pygame.draw.line(screen, BLACK, (x, y+cell_size), (x, y), width=4)

        for obs_izquierda in level[1]:
                x = obs_izquierda[1]*cell_size
                y = obs_izquierda[0]*cell_size + cell_size
                pygame.draw.line(screen, BLACK, (x, y), (x+cell_size, y), width=4)
                
        pygame.draw.rect(screen, BLUE, (goal[1]*cell_size+goal_size//2, goal[0]*cell_size+goal_size//2, goal_size, goal_size))

        #player
        pygame.draw.ellipse(screen, RED, (player[1]*cell_size+player_size//2, player[0]*cell_size+player_size//2, player_size, player_size))
    else:
        if current_level < num_levels:
            goToLevel(current_level+1)
        else:
                pygame.draw.rect(screen, WHITE, (0, 0, witdh, witdh))
                font = pygame.font.SysFont('Arial', 30)
                text = font.render('YOU WIN', True, BLACK)
                screen.blit(text, (witdh//2-50, witdh//2-50))
                font = pygame.font.SysFont('Arial', 18)
                text = font.render('Press q to level 1', True, BLACK)
                screen.blit(text, (witdh//2-50, witdh//2))
                text = font.render('Press r to last level ', True, BLACK)
                screen.blit(text, (witdh//2-55, witdh//2+28))

    pygame.display.flip()
    clock.tick(fps)