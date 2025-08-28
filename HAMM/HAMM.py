with open('HAMM/rosalind_hamm.txt', 'r') as file:
    strings = file.read().strip()

# String 1 = s
# String 2 = t
# Hamming distance = the number of corresponding symbols that differ in s and t
s, t = strings.split('\n')

hamming_distance = sum(1 for i, j in zip(s, t) if i != j)
print(hamming_distance)