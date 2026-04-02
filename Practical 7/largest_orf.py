seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

stop_codons = ['UAA', 'UAG', 'UGA']
largest_orf = ''

for i in range(len(seq) - 2):
    codon = seq[i:i+3]

    if codon == 'AUG':
        for j in range(i + 3, len(seq) - 2, 3):
            stop_codon = seq[j:j+3]

            if stop_codon in stop_codons:
                orf = seq[i:j+3]

                if len(orf) > len(largest_orf):
                    largest_orf = orf
                break

print('Largest ORF:', largest_orf)
print('Length:', len(largest_orf))