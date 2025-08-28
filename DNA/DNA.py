from collections import Counter

with open('DNA/rosalind_dna.txt', 'r') as file:
    dna_sequence = file.read().strip()
# Count the occurrences of each nucleotide in the DNA sequence
nucleotide_counts = Counter(dna_sequence)
# Print the counts of each nucleotide
print(nucleotide_counts['A'], nucleotide_counts['C'], nucleotide_counts['G'], nucleotide_counts['T'])