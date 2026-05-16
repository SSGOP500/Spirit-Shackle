import random
# ====================  blue Print For SnakeEnv(snake enviroment)  ====================
class SnakeEnv:
    # ====================  defining self/snake/agent  ====================
    def __init__(self):
        self.grid_size=11
        self.snake_position=[(5,5),(5,6),(5,7)]
        self.attempts=0
        self.reward=0
        self.done=False
        self.spawn_food()
        self.action=0
    # ====================  spawning of food ====================
    def spawn_food(self):
        while True:
            self.food_position = (
                random.randint(0, self.grid_size - 1),
                random.randint(0, self.grid_size - 1)
            )
            if self.food_position not in self.snake_position:
                break    
    # ====================  movement of snake ====================
    def move(self,action):
        new_x=self.snake_position[0][0]
        new_y=self.snake_position[0][1]
        if action == 0:
            new_y -= 1
        elif action == 3:
            new_x +=1
        elif action == 2:
            new_x -=1
        elif action == 1:
            new_y +=1  
        else:
            pass          
        self.snake_position.insert(0,(new_x,new_y))
    # ====================  collision detection ====================
    def is_collision(self,x,y):
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size:
            return 1
        elif (x,y) in self.snake_position[1:]:
            return 1
        return 0
    # ==================== state ====================
    def get_state(self):
        head_x, head_y = self.snake_position[0]
        food_x, food_y = self.food_position
        # ==================== food direction ====================
        if food_x < head_x:
            food_left = 1
        else:
            food_left = 0
        if food_x > head_x:
            food_right = 1
        else:            
            food_right = 0
        if food_y < head_y:
            food_up = 1
        else:
            food_up = 0
        if food_y > head_y:
            food_down = 1
        else:
            food_down = 0
        # ==================== danger direction ====================
        danger_up = self.is_collision(head_x, head_y - 1)
        danger_down = self.is_collision(head_x, head_y + 1)
        danger_left = self.is_collision(head_x - 1, head_y)
        danger_right = self.is_collision(head_x + 1, head_y)

        return (danger_up, danger_down, danger_left, danger_right, food_up, food_down, food_left, food_right)
    # ==================== steps taken ====================
    def step(self,action):
        self.reward=0
        self.action=action
        self.move(action)
    # ==================== death condition ====================
        if self.snake_position[0][0]<0:
            self.reward -=1
            self.attempts +=1
            self.done=True
            return self.get_state(), self.reward, self.done
        elif self.snake_position[0][0]>= self.grid_size:
            self.reward -=1
            self.attempts +=1
            self.done=True
            return self.get_state(), self.reward, self.done
        elif self.snake_position[0][1]< 0:
            self.reward -=1
            self.attempts +=1
            self.done=True
            return self.get_state(), self.reward, self.done
        elif self.snake_position[0][1] >= self.grid_size:
            self.reward -=1
            self.attempts +=1
            self.done=True
            return self.get_state(), self.reward, self.done
        elif self.snake_position[0] in self.snake_position[1:]:
            self.reward -=1.25
            self.attempts +=1
            self.done=True
            return self.get_state(), self.reward, self.done
        # ==================== spawned food ====================
        if self.snake_position[0] == self.food_position:
            self.reward +=5
            self.spawn_food()
            return self.get_state(), self.reward, self.done
        else:
            self.snake_position.pop(-1)
            return self.get_state(), self.reward, self.done
    # ==================== reset ====================
    def reset(self):
        self.snake_position = [(5,5),(5,6),(5,7)]
        self.reward = 0
        self.done = False
        self.spawn_food()
        self.action = 0
        return self.get_state(), self.reward, self.done
        