import matplotlib.pyplot as plt

def read_fasta(filename):
    sequences = {}
    header = None
    seq_parts = []

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('>'):
                if header is not None:
                    sequences[header] = ''.join(seq_parts)
                header = line
                seq_parts = []
            else:
                seq_parts.append(line)

        if header is not None:
            sequences[header] = ''.join(seq_parts)

    return sequences

stop_codon = input('Enter a stop codon (TAA, TAG, TGA): ').upper()
if stop_codon not in ['TAA', 'TAG', 'TGA']:
    print('Invalid stop codon')

def longest_orf_for_stop(sequence, chosen_stop):
    best_orf = ''

    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == 'ATG':
            for j in range(i + 3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]

                if codon == chosen_stop:
                    orf = sequence[i:j+3]
                    if len(orf) > len(best_orf):
                        best_orf = orf
                    break
                elif codon in {'TAA', 'TAG', 'TGA'}:
                    break

    return best_orf

def count_codons_in_orf(orf):
    codon_counts = {}

    for i in range(0, len(orf), 3):
        codon = orf[i:i+3]
        if len(codon) == 3:
            codon_counts[codon] = codon_counts.get(codon, 0) + 1

    return codon_counts

fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
sequences = read_fasta(fasta_file)

total_counts = {}

for sequence in sequences.values():
    orf = longest_orf_for_stop(sequence, stop_codon)

    if orf:
        codon_counts = count_codons_in_orf(orf)

        for codon, count in codon_counts.items():
            total_counts[codon] = total_counts.get(codon, 0) + count

if total_counts:
    labels = list(total_counts.keys())
    sizes = list(total_counts.values())

    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels)
    plt.title(f'Codon frequency for genes with stop codon {stop_codon}')
    plt.savefig(f'{stop_codon}_codon_frequency_pie_chart.png')
    print('Pie chart saved.')
else:
    print('No ORFs found for that stop codon.')