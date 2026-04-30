import random
# ====================  blue Print For SnakeEnv(snake enviroment)  ====================
class SnakeEnv:
    # ====================  defining self/snake/agent  ====================
    def __init__(self):
        self.grid_size=11
        self.snake_position=[(6,6),(6,5),(6,4)]
        self.attempts=0
        self.deaths=0
        self.reward=0
        self.done=False
        self.spawn_food()
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
    def move(self,direction):
        new_x=self.snake_position[0][0]
        new_y=self.snake_position[0][1]
        if direction == 'Up':
            new_y += 1
        elif direction == 'Down':
            new_y -= 1
        elif direction == 'Right':
            new_x +=1
        elif direction == 'left':
            new_x -=1
        else:
            pass          
        self.snake_position.insert(0,(new_x,new_y))    
    # ==================== steps taken ====================
    def step(self,direction):
        self.reward=0
        self.move(direction)
    # ==================== penalty condition ====================
        if self.snake_position[0][0]<0:
            self.reward -=1
            self.deaths +=1
            self.done=True
            return self.snake_position, self.reward, self.done
        elif self.snake_position[0][0]>= self.grid_size:
            self.reward -=1
            self.deaths +=1
            self.done=True
            return self.snake_position, self.reward, self.done
        elif self.snake_position[0][1]< 0:
            self.reward -=1
            self.deaths +=1
            self.done=True
            return self.snake_position, self.reward, self.done
        elif self.snake_position[0][1] >= self.grid_size:
            self.reward -=1
            self.deaths +=1
            self.done=True
            return self.snake_position, self.reward, self.done
        elif self.snake_position[0] in self.snake_position[1:]:
            self.reward -=1.25
            self.deaths +=1
            self.done=True
            return self.snake_position, self.reward, self.done
        # ==================== spawned food ====================
        if self.snake_position[0] == self.food_position:
            self.reward +=5
            self.spawn_food()
            return self.snake_position, self.reward, self.done
        else:
            self.snake_position.pop(-1)
            return self.snake_position, self.reward, self.done
    # ==================== reset ====================
    def reset(self):
        self.snake_position = [(6,6),(6,5),(6,4)]
        self.reward = 0
        self.done = False
        self.spawn_food()
        return self.snake_position, self.reward, self.done