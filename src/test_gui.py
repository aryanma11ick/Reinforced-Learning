from sumo_rl import SumoEnvironment
import os

NET_FILE = os.path.join("..", "network", "grid.net.xml")
ROUTE_FILE = os.path.join("..", "network", "grid.rou.xml")

env = SumoEnvironment(
    net_file=NET_FILE,
    route_file=ROUTE_FILE,
    use_gui=True,      # watch the simulation
    single_agent=False,
    num_seconds=3600
)

obs = env.reset()
done = False
while not done:
    actions = {tl: env.action_spaces[tl].sample() for tl in env.ts_ids}  # random demo policy
    obs, reward, dones, info = env.step(actions)
    done = all(dones.values())

env.close()
