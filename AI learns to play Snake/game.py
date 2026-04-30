
import pygame
from env import SnakeEnv
# ==================== innit ====================
pygame.init()
# ==================== display size ====================
screen = pygame.display.set_mode((500,400))
# ==================== tick speed ====================
clock = pygame.time.Clock()
# ==================== env ====================
env = SnakeEnv()
env.reset()
# ==================== running and done ====================
running = True
done = False
# ==================== grid and pixels ====================
cell_size = 30
grid_size = env.grid_size
grid = cell_size*grid_size
screen_width = screen.get_width()
screen_height = screen.get_height()
offset_x = (screen_width-grid)//2
offset_y = (screen_height-grid)//2
# ==================== loop ====================
while running:  
    # ==================== black screen ====================
    screen.fill((0,0,0))
    # ==================== grid ====================
    for x in range(grid_size + 1):
        zx = offset_x + x * cell_size
        pygame.draw.line(screen, (60,60,60), (zx, offset_y), (zx, offset_y + grid))
    for y in range(grid_size + 1):
        zy = offset_y + y * cell_size
        pygame.draw.line(screen, (60,60,60), (offset_x, zy), (offset_x + grid, zy))
    # ==================== tickspeed ====================
    clock.tick(5)
    # ==================== snake visualization ====================
    for segment in env.snake_position:
        x, y = segment
        pixel_x = offset_x + x * cell_size
        pixel_y = offset_y + y * cell_size
        pygame.draw.rect(screen,(0, 255, 0),(pixel_x, pixel_y, cell_size, cell_size))
    # ==================== food visualization ====================
    fx=env.food_position[0]
    pixel_fx = offset_x + fx * cell_size
    fy=env.food_position[1]
    pixel_fy = offset_y + fy * cell_size
    pygame.draw.rect(screen,(255,0,0),(pixel_fx,pixel_fy,cell_size,cell_size))
    # ==================== closing window ====================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # ==================== stopping ====================
    if done:
        env.reset()
        done = False
    # ==================== refreshing/creating new frames ====================
    pygame.display.update()
pygame.quit()
