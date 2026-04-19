import numpy as np
import matplotlib.pyplot as plt

N = 10000
beta = 0.3
gamma = 0.05

vaccination_rates = range(0, 101, 10)

plt.figure(figsize=(6, 4), dpi=150)

for rate in vaccination_rates:
    V = int(N * rate / 100)

    if V >= N:
        V = N
        I = 0
        S = 0
    else:
        I = 1
        S = N - V - I
        R = 0

    I_history = [I]

    # pseudocode
    # for each vaccination rate:
    # 1. set vaccinated population
    # 2. initialize S, I, R
    # 3. run the SIR model over time
    # 4. store infected numbers
    # 5. plot infected curve for this vaccination rate

    for t in range(1000):
        infection_prob = beta * (I / N)

        new_infections = np.random.choice(
            [0, 1],
            size=S,
            p=[1 - infection_prob, infection_prob]
        ).sum()

        new_recoveries = np.random.choice(
            [0, 1],
            size=I,
            p=[1 - gamma, gamma]
        ).sum()

        S = S - new_infections
        I = I + new_infections - new_recoveries
        R = R + new_recoveries

        I_history.append(I)

    plt.plot(I_history, label=f"{rate}%")

plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()