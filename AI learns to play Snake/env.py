import random
# ====================  blue Print For SnakeEnv(snake enviroment)  ====================
class SnakeEnv:
    # ====================  defining self/snake/agent  ====================
    def __init__(self):
        self.grid_size=11
        self.snake_position=[(5,5),(5,6),(5,7)]
        self.attempts=0
        self.deaths=0
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
            last_action = 0
        elif action == 3:
            new_x +=1
            last_action = 3
        elif action == 2:
            new_x -=1
            last_action = 2
        elif action == 1:
            new_y +=1  
            last_action = 1
        else:
            pass          
        self.snake_position.insert(0,(new_x,new_y))   
        if action == 0 and last_action == 1:
            return
        elif action == 1 and last_action == 0:
            return
        elif action == 2 and last_action == 3:
            return
        elif action == 3 and last_action == 2:
            return
    # ==================== steps taken ====================
    def step(self,action):
        self.reward=0
        self.move(action)
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
        self.snake_position = [(5,5),(5,6),(5,7)]
        self.reward = 0
        self.done = False
        self.spawn_food()
        self.action = "Up"
        return self.snake_position, self.reward, self.done