from simulation import simRound

for i in range(2):
    guess, attempts = simRound()
    print(guess, "in", attempts)