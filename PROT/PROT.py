with open('PROT/rosalind_prot.txt', 'r') as file:
    rna_sequence = file.read().strip()

# Dictionary for RNA codon to amino acid translation
rna_codon_table = {'UUU': 'F',  
'CUU': 'L',      
'AUU': 'I',      
'GUU': 'V',
'UUC': 'F',   
'CUC': 'L',      
'AUC': 'I',      
'GUC': 'V',
'UUA': 'L',   
'CUA': 'L',      
'AUA': 'I',      
'GUA': 'V',
'UUG': 'L',   
'CUG': 'L',      
'AUG': 'M',      
'GUG': 'V',
'UCU': 'S',   
'CCU': 'P',      
'ACU': 'T',      
'GCU': 'A',
'UCC': 'S',   
'CCC': 'P',      
'ACC': 'T',      
'GCC': 'A',
'UCA': 'S',   
'CCA': 'P',      
'ACA': 'T',      
'GCA': 'A',
'UCG': 'S',   
'CCG': 'P',      
'ACG': 'T',      
'GCG': 'A',
'UAU': 'Y',   
'CAU': 'H',      
'AAU': 'N',      
'GAU': 'D',
'UAC': 'Y',   
'CAC': 'H',      
'AAC': 'N',      
'GAC': 'D',
'UAA': 'Stop',   
'CAA': 'Q',      
'AAA': 'K',      
'GAA': 'E',
'UAG': 'Stop',   
'CAG': 'Q',      
'AAG': 'K',      
'GAG': 'E',
'UGU': 'C',   
'CGU': 'R',      
'AGU': 'S',      
'GGU': 'G',
'UGC': 'C',   
'CGC': 'R',      
'AGC': 'S',      
'GGC': 'G',
'UGA': 'Stop',   
'CGA': 'R',      
'AGA': 'R',      
'GGA': 'G',
'UGG': 'W',   
'CGG': 'R',      
'AGG': 'R',      
'GGG': 'G'} 

# Translate RNA sequence to protein sequence
protein_sequence = []
for i in range(0, len(rna_sequence) - 2, 3):
    codon = rna_sequence[i:i+3]
    if codon in rna_codon_table:
        amino_acid = rna_codon_table[codon]
        if amino_acid == 'Stop':
            break
        protein_sequence.append(amino_acid)
protein_sequence = ''.join(protein_sequence)
print(protein_sequence)