import numpy as np
from sumo_rl import SumoEnvironment
import os

# Path to SUMO network
NET_FILE = os.path.join("..", "network", "grid.net.xml")
ROUTE_FILE = os.path.join("..", "network", "grid.rou.xml")

env = SumoEnvironment(
    net_file=NET_FILE,
    route_file=ROUTE_FILE,
    use_gui=False,       # set True to watch training
    single_agent=False,  # multi-agent
    num_seconds=3600
)

# Create simple Q-tables for each traffic light
agents = {}
for tl in env.ts_ids:
    obs_size = env.observation_spaces[tl].shape[0]
    act_size = env.action_spaces[tl].n
    agents[tl] = np.zeros((obs_size, act_size))

alpha = 0.1
gamma = 0.99
epsilon = 0.1
episodes = 20

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        actions = {}
        for tl in env.ts_ids:
            if np.random.rand() < epsilon:
                actions[tl] = env.action_spaces[tl].sample()
            else:
                actions[tl] = np.argmax(agents[tl][obs[tl]])
        next_obs, rewards, dones, infos = env.step(actions)

        # Update Q-tables
        for tl in env.ts_ids:
            q = agents[tl][obs[tl], actions[tl]]
            q_next = np.max(agents[tl][next_obs[tl]])
            agents[tl][obs[tl], actions[tl]] = q + alpha * (rewards[tl] + gamma * q_next - q)

        obs = next_obs
        done = all(dones.values())

env.close()
print("Training complete!")
