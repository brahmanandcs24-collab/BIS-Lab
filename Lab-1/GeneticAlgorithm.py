import random

num_jobs = 5
num_machines = 2

processing_time = [
    [3, 2],   
    [2, 4],   
    [4, 3],   
    [2, 1],   
    [3, 4]    
]

population_size = 6
generations = 20
mutation_rate = 0.1


def calculate_makespan(schedule):
    machine_time = [0] * num_machines

    for job in schedule:
        for machine in range(num_machines):
            machine_time[machine] += processing_time[job][machine]

    return max(machine_time)


def fitness(schedule):
    return 1 / (1 + calculate_makespan(schedule))


population = []

for _ in range(population_size):
    schedule = list(range(num_jobs))
    random.shuffle(schedule)
    population.append(schedule)


for generation in range(generations):

    population.sort(key=fitness, reverse=True)

    parent1 = population[0]
    parent2 = population[1]

    point = random.randint(1, num_jobs - 1)

    child = parent1[:point]

    for job in parent2:
        if job not in child:
            child.append(job)

    if random.random() < mutation_rate:
        i, j = random.sample(range(num_jobs), 2)
        child[i], child[j] = child[j], child[i]

    population[-1] = child


best_schedule = max(population, key=fitness)

print("Best Job Schedule:")

for job in best_schedule:
    print("J" + str(job + 1), end=" ")

print("\nMinimum Makespan:",
      calculate_makespan(best_schedule))
