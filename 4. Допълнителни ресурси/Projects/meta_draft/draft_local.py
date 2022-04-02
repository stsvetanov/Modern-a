import random

TARGET = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def generate_local_solution(solution):
    local_solution = [s for s in solution]
    num_low = 0
    num_len = len(solution)
    index = random.randint(num_low, num_len -1)
    local_solution.pop(index)
    local_solution.insert(index, random.randint(0, 9))
    return local_solution


def estimate_solution(target, solution):
    return sum(abs(x - y) for (x, y) in zip(target, solution))


def generate_random_solution(target):
    return [random.randint(0, 9) for _ in range(len(target))]


solution = generate_random_solution(TARGET)
print(f"Initial solution: {solution}")

count = 0
while True:
    if estimate_solution(TARGET, solution) == 0:
        print(f"Best solution: {solution}, iter: {count}")
        break
    next_solution = generate_local_solution(solution)
    count += 1
    if estimate_solution(next_solution, TARGET) < estimate_solution(solution, TARGET):
        solution = next_solution
        print(f"Current Solution: {solution}")
