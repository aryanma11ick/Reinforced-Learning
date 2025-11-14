# Multi-Agent Traffic Signal Control - SUMO Project

## Overview
This project demonstrates **multi-agent RL controlling traffic lights** on a 3x3 grid using SUMO and SUMO-RL. Each intersection is an agent observing lane queues and selecting traffic light phases.

## Folder structure
- `network/` - SUMO network and routes
- `src/train.py` - Multi-agent RL training
- `src/test_gui.py` - Run simulation with GUI
- `results/` - CSV logs
- `videos/` - Record demo

## Requirements
- Windows 10/11
- SUMO installed and added to PATH
- Python 3.9+
- Libraries: `sumo-rl`, `traci`, `gymnasium`, `numpy`, `stable-baselines3`

## Run
1. Train RL agents (optional, minimal example uses random actions):
```bash
python src/train.py
