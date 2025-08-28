with open('FIB/rosalind_fib.txt', 'r') as file:
    population = file.read().strip()

n, k = map(int, population.split()) # n = number of months, k = rabbit pairs (every pair of reproduction-age rabbits produces a litter of k rabbit pairs)
# return: total number of rabbit pairs after n months

F = [0] * (n + 1)
F[1] = 1 # month 1 has 1 rabbit pair
F[2] = 1 # month 2 has 1 rabbit pair
for i in range(3, n + 1):
    F[i] = F[i - 1] + k * F[i - 2]
print(F[n])