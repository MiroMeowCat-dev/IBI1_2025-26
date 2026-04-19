import numpy as np
import matplotlib.pyplot as plt

# initial conditions
N = 10000
I = 1
S = N - I
R = 0

beta = 0.3
gamma = 0.05

# store values over time
S_history = [S]
I_history = [I]
R_history = [R]

# pseudocode
# for each time step:
# 1. calculate infection probability = beta * (I / N)
# 2. randomly decide how many susceptible people become infected
# 3. randomly decide how many infected people recover
# 4. update S, I, R
# 5. save new values to history lists
for t in range(1000):
        infection_prob = beta * (I / N)

        new_infections = np.random.choice([0, 1], size=S, p=[1 - infection_prob, infection_prob]).sum()

        new_recoveries = np.random.choice([0, 1], size=I, p=[1 - gamma, gamma]).sum()

        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        S_history.append(S)
        I_history.append(I)
        R_history.append(R)
plt.figure(figsize=(6, 4), dpi=150)

plt.plot(S_history, label='susceptible')
plt.plot(I_history, label='infected')
plt.plot(R_history, label='recovered')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.show()