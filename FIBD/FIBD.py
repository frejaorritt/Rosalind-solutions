with open('FIBD/rosalind_fibd.txt', 'r') as file:
    integers = file.read().strip()

# Takes offspring 1 month to mature and reproduce
# Return the total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months
n, m = map(int, integers.split())

def fibd(n, m):
    generations = [1,1]
    months = 2
    while months<n:
        iter1 = generations[-2]
        iter2 = generations[-1]
        if months<m:
            generations.append(iter1 + iter2)
        elif months == m:
            generations.append(iter1 + iter2 - 1)
        else:
            mortality = generations[-(m+1)]
            generations.append(iter1 + iter2 - mortality)
        months += 1
    return generations[-1]

print(fibd(n, m))