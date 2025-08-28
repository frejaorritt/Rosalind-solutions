with open('RNA/rosalind_rna.txt', 'r') as file:
    dna_sequence = file.read().strip()

# Convert DNA sequence to RNA sequence, replacing 'T' with 'U'
rna_sequence = dna_sequence.replace('T', 'U')  
print(rna_sequence)  # Print the resulting RNA sequence