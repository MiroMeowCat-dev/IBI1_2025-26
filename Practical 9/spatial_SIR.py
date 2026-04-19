import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100))

outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.3
gamma = 0.05

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Initial outbreak")
plt.show()

# pseudocode
# for each time step:
# 1. find all infected cells
# 2. for each infected cell, check its 8 neighbours
# 3. infect susceptible neighbours with probability beta
# 4. allow infected cells to recover with probability gamma
# 5. update the population grid
# 6. plot selected time points

# plot initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Time 0")
plt.show()

for t in range(1, 101):
    new_population = population.copy()

    infected_positions = np.where(population == 1)
    infected_cells = list(zip(infected_positions[0], infected_positions[1]))

    for i, j in infected_cells:
        # check all 8 neighbours
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue

                ni = i + di
                nj = j + dj

                # make sure neighbour is inside the grid
                if 0 <= ni < 100 and 0 <= nj < 100:
                    # only susceptible neighbours can be infected
                    if population[ni, nj] == 0:
                        if np.random.random() < beta:
                            new_population[ni, nj] = 1

        # infected cell can recover
        if np.random.random() < gamma:
            new_population[i, j] = 2

    population = new_population

    if t in [10, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time {t}")
        plt.show()