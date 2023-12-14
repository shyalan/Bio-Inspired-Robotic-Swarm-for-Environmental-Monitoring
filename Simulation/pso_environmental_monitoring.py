import random
import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.best_position = position
        self.best_fitness = 0  # Initialize to 0

class Circle:
    def __init__(self):
        self.explored = False
        self.color = random.choice(['red', 'green', 'blue'])

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def update_explored_area(particles, fixed_radius, grid_size, circles):
    for particle in particles:
        x, y = map(int, particle.position)
        x = max(0, min(grid_size - 1, x))
        y = max(0, min(grid_size - 1, y))

        if not circles[x][y].explored:
            particle.best_fitness += 1
            circles[x][y].explored = True

def initialize_circles(grid_size):
    return [[Circle() for _ in range(grid_size)] for _ in range(grid_size)]

def draw_circles(circles, grid_size):
    circle_size = grid_size / len(circles)

    for i in range(len(circles)):
        for j in range(len(circles[i])):
            if circles[i][j].explored:
                color = circles[i][j].color
                marker = 'o'  # Marker for normal temperature

                if color == 'red':
                    marker = 's'  # Square marker for high temperature
                elif color == 'blue':
                    marker = '^'  # Triangle marker for cold temperature

                plt.scatter(i * circle_size, j * circle_size, s=200, c=color, marker=marker, alpha=0.3)

    legend_labels = {
        'red': 'High Temperature',
        'green': 'Normal Temperature',
        'blue': 'Cold Temperature',
    }

    handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, markersize=10, markerfacecolor=color)
               for color, label in legend_labels.items()]

    plt.legend(handles=handles, loc='upper right')

def has_converged(particles, convergence_threshold=0.01):
    positions = [particle.position for particle in particles]
    distances = [distance(p1, p2) for p1 in positions for p2 in positions if p1 != p2]
    return all(distance <= convergence_threshold for distance in distances)

def get_unexplored_position(particles, grid_size):
    explored_positions = set(tuple(map(int, particle.position)) for particle in particles)
    unexplored_positions = [(x, y) for x in range(grid_size) for y in range(grid_size)
                            if (x, y) not in explored_positions]
    
    if unexplored_positions:
        return random.choice(unexplored_positions)
    else:
        return (random.uniform(0, grid_size), random.uniform(0, grid_size))

def pso(swarm_size, total_area, max_iterations):
    grid_size = int(math.sqrt(total_area) * 10)

    inertia_weight = 0.7
    cognitive_weight = 2.0
    social_weight = 2.0

    fixed_radius = 15

    particles = [Particle(
        position=(random.uniform(0, grid_size), random.uniform(0, grid_size)),
        velocity=(random.uniform(-0.1, 0.1), random.uniform(-0.1, 0.1))
    ) for _ in range(swarm_size)]

    plt.figure(figsize=(8, 8))

    circles = initialize_circles(grid_size)

    iteration = 0
    red_star_position = (grid_size / 2, grid_size / 2)

    while iteration < max_iterations:
        plt.clf()

        update_explored_area(particles, fixed_radius, grid_size, circles)

        total_colored_circles = sum(circles[i][j].explored for i in range(grid_size) for j in range(grid_size))
        total_explored_area = (total_colored_circles / (grid_size**2)) * total_area

        draw_circles(circles, grid_size)

        center_mass = (sum(p[0] for p in [particle.position for particle in particles]) / len(particles),
                       sum(p[1] for p in [particle.position for particle in particles]) / len(particles))

        red_star_position = (
            red_star_position[0] + 0.1 * (center_mass[0] - red_star_position[0]),
            red_star_position[1] + 0.1 * (center_mass[1] - red_star_position[1])
        )

        if iteration % 20 == 0:
            red_star_position = get_unexplored_position(particles, grid_size)

        for particle in particles:
            current_fitness = particle.best_fitness

            if current_fitness > particle.best_fitness:
                particle.best_fitness = current_fitness
                particle.best_position = particle.position

        converged = has_converged(particles)

        if converged:
            new_red_star_position = get_unexplored_position(particles, grid_size)
            red_star_position = new_red_star_position

        for particle in particles:
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)

            new_velocity = (
                inertia_weight * particle.velocity[0] +
                cognitive_weight * r1 * (particle.best_position[0] - particle.position[0]) +
                social_weight * r2 * (red_star_position[0] - particle.position[0]),
                inertia_weight * particle.velocity[1] +
                cognitive_weight * r1 * (particle.best_position[1] - particle.position[1]) +
                social_weight * r2 * (red_star_position[1] - particle.position[1])
            )

            particle.velocity = new_velocity

            new_position = (
                particle.position[0] + particle.velocity[0],
                particle.position[1] + particle.velocity[1]
            )

            new_position = (
                max(0, min(grid_size, new_position[0])),
                max(0, min(grid_size, new_position[1]))
            )

            particle.position = new_position

        plt.scatter(*zip(*[particle.position for particle in particles]), label='Particles')
        plt.scatter(*zip(red_star_position), color='red', marker='*', label='Global Best')
        plt.scatter(*zip(red_star_position), s=300, color='red', marker='*')
        plt.xlim(0, grid_size)
        plt.ylim(0, grid_size)
        plt.title(f'Particle Swarm Optimization - Iteration {iteration + 1}\n'
                  f'Total Explored Area: {total_explored_area:.2f} km^2\n'
                  f'ECE: {total_explored_area / total_area * 100:.1f}%', fontsize=10, color='black')

        plt.legend()

        plt.pause(0.1)

        iteration += 1

    plt.show()

if __name__ == "__main__":
    swarm_size = int(input("Enter the Swarm (population) Size: "))
    total_area = float(input("Enter the Total Area in km^2: "))
    max_iterations = int(input("Enter the Number of Iterations: "))

    pso(swarm_size, total_area, max_iterations)

# Created by Shyalan Ramesh
# PSO Simulation for Environmental Monitoring