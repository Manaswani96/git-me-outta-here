import random

modes = [
    "Gradient Descent: slowly improving, slightly depressed",
    "Newton's Method: confident, fails dramatically",
    "Stochastic GD: chaotic but somehow works",
    "Genetic Algorithm: evolving out of spite",
    "Simulated Annealing: cold start, hot finish"
]

print("Today's optimization mode:", random.choice(modes))
