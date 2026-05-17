import pygame
import random
import pickle
import os
from env import SnakeEnv
# ==================== innit ====================
pygame.init()
env = SnakeEnv()
# ====================  blue Print For Agent  ====================
class Agent:
    # ====================  defining  ====================
    def __init__(self):
        self.lr=0.5
        self.gamma=0.5
        self.epsilon=0.6
        self.epsilon_decay=0.9995
        self.epsilon_min=0.01
        self.q_table={}
        self.load_q_table()
    # ====================  get q value ====================
    def get_q(self,state):
        if state not in self.q_table:
            self.q_table[state]=[0,0,0,0]
        return self.q_table[state]
    # ====================  action selection ====================
    def action_selection(self,state):
        # ==================== exploration ====================
        if random.random() < self.epsilon:
            return random.randint(0,3)
        # ==================== exploitation ====================
        q_values = self.get_q(state)
        return q_values.index(max(q_values))
    # ====================  learning ====================
    def learn(self,state,action,reward,next_state,done):
        current_q = self.get_q(state)[action]
        if done:
            target = reward
        else:
            target = reward + self.gamma * max(self.get_q(next_state))
        # ====================  learning update ====================
        self.q_table[state][action] += self.lr * (target - current_q)
    # ====================  save q table ====================
    def save_q_table(self):
        with open("q_table.pkl", "wb") as file:
            pickle.dump(self.q_table, file)
    # ====================  load q table ====================
    def load_q_table(self):
        if os.path.exists("q_table.pkl"):
            with open("q_table.pkl", "rb") as file:
                self.q_table = pickle.load(file)

agent = Agent()
episodes = 1000
# ==================== training loop ====================
for episode in range(episodes):
    env.reset()
    state = env.get_state()
    total_reward = 0
    # ==================== episode loop ====================
    while not env.done:
        action = agent.action_selection(state)
        next_state, reward, done = env.step(action)
        agent.learn(state,action,reward,next_state,done)
        state = next_state
        total_reward += reward
    # ==================== learning stabilization ====================
    agent.epsilon = max(agent.epsilon * agent.epsilon_decay, agent.epsilon_min)

agent.save_q_table()
if episode % 100 == 0:
    print(episode, total_reward)