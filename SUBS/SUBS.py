with open('SUBS/rosalind_subs.txt', 'r') as file:
    strings = file.read().strip()

# String 1 = s
# String 2 = t (substring)
# Return locations of t in s

s, t = strings.split('\n')
def find_substring_locations(s, t):
    locations = []
    index = s.find(t)
    while index != -1:
        locations.append(index + 1)
        index = s.find(t, index + 1)
    return locations
locations = find_substring_locations(s, t)
print(' '.join(map(str, locations)))