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
    for x in range(grid_size):
        for y in range(grid_size):
            pixel_x = offset_x + x * cell_size
            pixel_y = offset_y + y * cell_size
            if (x + y) % 2 == 0:
                cell_color =(15, 15, 20)
            else:
                cell_color =(28, 31, 42)
            pygame.draw.rect(screen,cell_color,(pixel_x, pixel_y, cell_size, cell_size))
    # ==================== tickspeed ====================
    clock.tick(8)
    # ==================== snake visualization ====================
    for index, segment in enumerate(env.snake_position):
        x, y = segment
        pixel_x = offset_x + x * cell_size
        pixel_y = offset_y + y * cell_size
        color_constant = index / (len(env.snake_position) - 1)
        normalized_color = 85 + color_constant * (155 - 85)
        pygame.draw.rect(screen,(0,normalized_color,0),(pixel_x,pixel_y,cell_size,cell_size),border_radius=8)
        # ==================== eye visualization ====================
        if index == 0:
            eye_x = pixel_x + cell_size // 2
            eye_y = pixel_y + cell_size // 2
            eye_offset_x = cell_size // 5
            eye_offset_y = cell_size // 6
            eye_radius = cell_size // 6
            pupil_radius = eye_radius // 2
            pygame.draw.circle(screen,(255,255,255),(eye_x-eye_offset_x,eye_y-eye_offset_y),eye_radius)
            pygame.draw.circle(screen,(255,255,255),(eye_x+eye_offset_x,eye_y-eye_offset_y),eye_radius)
            # ==================== eye movement ====================
            if env.action == 0:
                pygame.draw.circle(screen,(0,0,0),(eye_x-eye_offset_x,eye_y-eye_offset_y-3),pupil_radius)
                pygame.draw.circle(screen,(0,0,0),(eye_x+eye_offset_x,eye_y-eye_offset_y-3),pupil_radius)
            elif env.action == 1:
                pygame.draw.circle(screen,(0,0,0),(eye_x-eye_offset_x,eye_y-eye_offset_y+3),pupil_radius)
                pygame.draw.circle(screen,(0,0,0),(eye_x+eye_offset_x,eye_y-eye_offset_y+3),pupil_radius)
            elif env.action == 2:
                pygame.draw.circle(screen,(0,0,0),(eye_x-eye_offset_x-3,eye_y-eye_offset_y),pupil_radius)
                pygame.draw.circle(screen,(0,0,0),(eye_x+eye_offset_x-3,eye_y-eye_offset_y),pupil_radius)
            elif env.action == 3:
                pygame.draw.circle(screen,(0,0,0),(eye_x-eye_offset_x+3,eye_y-eye_offset_y),pupil_radius)
                pygame.draw.circle(screen,(0,0,0),(eye_x+eye_offset_x+3,eye_y-eye_offset_y),pupil_radius)
            else:
                pygame.draw.circle(screen,(0,0,0),(eye_x-eye_offset_x,eye_y-eye_offset_y),pupil_radius)
                pygame.draw.circle(screen,(0,0,0),(eye_x+eye_offset_x,eye_y-eye_offset_y),pupil_radius)
    # ==================== food visualization ====================
    fx=env.food_position[0]
    pixel_fx = offset_x + fx * cell_size
    fy=env.food_position[1]
    pixel_fy = offset_y + fy * cell_size
    pygame.draw.rect(screen,(255,0,0),(pixel_fx,pixel_fy,cell_size,cell_size), border_radius=10)
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
            # ==================== game start ====================
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