with open('GC/rosalind_gc.txt', 'r') as file:
    FASTA = file.read().strip()

# Calculate GC content, output ID and GC percentage of string with highest percentage 
def gc_content(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / len(sequence)) * 100

FASTA = FASTA.split('>')[1:] 
max_gc = 0
max_id = ''
for i in FASTA:
    lines = i.split('\n')
    id = lines[0]
    sequence = ''.join(lines[1:])
    gc = gc_content(sequence)
    if gc>max_gc:
        max_gc = gc
        max_id = id

print(max_id)
print(f"{max_gc:.6f}")