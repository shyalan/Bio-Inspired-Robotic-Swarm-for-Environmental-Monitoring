# Particle Swarm Optimization for Environmental Monitoring

## Overview

This Python simulation employs Particle Swarm Optimization (PSO) to model the exploration of an unknown environment by a swarm of robots. The robots aim to converge on the global best position, represented by a red star on the map, providing a heuristic approach to environmental monitoring. The simulation prompts users to input the swarm size, total area to explore, and the number of iterations, offering flexibility in experimentation.

## Motivation

Environmental monitoring plays a crucial role in understanding and preserving ecosystems. The use of swarms of robots enhances efficiency in exploring vast and uncharted territories, enabling data collection and analysis in a timely manner. PSO provides a decentralized and adaptive solution to guide the swarm toward the most promising areas.

## How to Run

1. Clone the repository to your local machine.
2. Ensure you have Python installed (version 3.x).
3. Install required libraries using:
    ```bash
    pip install matplotlib
    ```
4. Run the simulation by executing the `pso_environmental_monitoring.py` file.

## Key Features

- **Swarm Exploration:** The swarm of robots dynamically adjusts its positions based on PSO principles to efficiently explore the unknown environment.
- **Temperature Representation:** Randomly placed temperatures on the map signify different climate conditions, with colors indicating high, normal, and cold temperatures.
- **Global Best Position:** The red star represents the global best position, guiding the swarm to unexplored territories.
- **Dynamic Red Star Movement:** After every 20 iterations, the global best position jumps to a new uncharted territory, simulating unpredictable environmental changes.

## Libraries Used

- `random`: Used for generating random numbers.
- `math`: Utilized for mathematical operations.
- `matplotlib`: Employed for visualizing the simulation with plots and animations.

## Algorithms and Equations

The simulation employs Particle Swarm Optimization (PSO), a nature-inspired optimization algorithm.

### Particle Velocity and Position Update Equations

The velocity and position of each particle are updated using PSO equations, facilitating adaptive movement towards optimal positions.

### Environmental Coverage Efficiency (ECE) Equation

The Environmental Coverage Efficiency is calculated as the ratio of the total explored area to the total area, expressed as a percentage.

## Visualization

Animated GIFs showcase the simulation run and the efficiency graph, providing a visual representation of the PSO algorithm in action.

**PSO Simulation**

<img src="https://github.com/shyalan/Bio-Inspired-Robotic-Swarm-for-Environmental-Monitoring/blob/main/Simulation/Data/exploration1.gif" width="400" height="auto"> <img src="https://github.com/shyalan/Bio-Inspired-Robotic-Swarm-for-Environmental-Monitoring/blob/main/Simulation/Data/exploration2.gif" width="400" height="auto">


- **Efficiency Graph**
![Efficiency Graph](Data/efficiency_graph.png)

Efficiency Graph showing 50 attempts in the simulation and its ECE%.
## Limitations

- The simulation assumes a 2D grid representation of the environment.
- Random placement of temperatures may lead to varying results in different runs.
- The convergence threshold may need adjustment based on specific use cases.
- The visualization may not be optimal for very large grid sizes.
- The Calculation of the total explored area is based of the total area and therefore in smaller land masses, it provides in-accurate explored areas as it counts each explored area in smaller fractions and similarly for larger areas.
- Sensory data such as temeprature and terrain shapes tend to be overlayed upon on each other for larger area and spaced out for smaller areas.
- Computational Power nad processing Speeds for larger simulations.

## Author

Shyalan Ramesh

Feel free to explore and modify the code to suit your needs!
