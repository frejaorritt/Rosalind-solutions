with open('IPRB/rosalind_iprb.txt', 'r') as file:
    population = file.read().strip()

k, m, n = map(int, population.split()) # k = homozygous dominant, m = heterozygous, n = homozygous recessive

def iprb(k,m,n):
    # Total number of individuals
    total = k + m + n
    # All possible pairings and their probabilities to produce an individual with at least one dominant allele
    prob_kk = (k / total) * ((k - 1) / (total - 1))
    prob_km = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    prob_mm = (m / total) * ((m - 1) / (total - 1))
    prob_mn = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1)) 
    prob_kn = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1)) 
    # Probability of at least one dominant allele in the offspring
    prob_dominant = prob_kk + prob_km + prob_kn + (0.75 * prob_mm) + (0.5 * prob_mn)
    return prob_dominant

result = iprb(k, m, n)
print(result)