import pygame
from env import SnakeEnv
# ==================== innit ====================
pygame.init()
# ==================== score ====================
score = 0
# ==================== game running ====================
game_active = False
# ==================== display size ====================
screen = pygame.display.set_mode((500, 400))
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
    clock.tick(8)
    # ==================== snake visualization ====================
    for segment in env.snake_position:
        x,y = segment
        pixel_x = offset_x + x * cell_size
        pixel_y = offset_y + y * cell_size
        if segment == env.snake_position[0]:
            pygame.draw.rect(screen,(0, 75, 0),(pixel_x, pixel_y, cell_size, cell_size))
        else:
            pygame.draw.rect(screen,(0, 255, 0),(pixel_x, pixel_y, cell_size, cell_size))
    # ==================== food visualization ====================
    fx=env.food_position[0]
    pixel_fx = offset_x + fx * cell_size
    fy=env.food_position[1]
    pixel_fy = offset_y + fy * cell_size
    pygame.draw.rect(screen,(255,0,0),(pixel_fx,pixel_fy,cell_size,cell_size))
    # ==================== score visualization ====================
    if env.reward == 5:
        score += 1
    score_font = pygame.font.SysFont("Comicsans", 18)
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    # ==================== event handling ====================
    for event in pygame.event.get():
        # ==================== quitting ====================
        if event.type == pygame.QUIT:
            running = False
        # ==================== getting input ====================
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                env.action = 0
            elif event.key == pygame.K_DOWN:
                env.action = 1
            elif event.key == pygame.K_LEFT:
                env.action = 2
            elif event.key == pygame.K_RIGHT:
                env.action = 3
            # ==================== game start after pause ====================
            elif event.key == pygame.K_SPACE:
                game_active = True
    # ==================== if game is running ====================
    if game_active:
        state,reward,done = env.step(env.action)
        # ==================== stopping ====================
        if env.done:
            game_active = False
            env.reset()
            score = 0
    # ==================== refreshing/creating new frames ====================
    pygame.display.update()
pygame.quit()