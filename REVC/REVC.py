with open('REVC/rosalind_revc.txt', 'r') as file:
    dna_sequence = file.read().strip()

# Reverse the DNA sequence
reversed_sequence = dna_sequence[::-1]

# Replace each nucleotide with its complement
replacements = str.maketrans({"A": "T", "T": "A", "C": "G", "G": "C"})
reverse_complement = reversed_sequence.translate(replacements)
print(reverse_complement)