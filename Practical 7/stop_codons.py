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

def extract_gene_name(header):
    parts = header.split()

    for part in parts:
        if part.startswith('gene:'):
            return part.split(':')[1]

    return header[1:]

def find_in_frame_stops(sequence):
    stop_codons = {'TAA', 'TAG', 'TGA'}
    found_stops = set()

    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == 'ATG':
            for j in range(i + 3, len(sequence) - 2, 3):
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    found_stops.add(codon)
                    break

    return found_stops

fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
sequences = read_fasta(fasta_file)

with open('stop_genes.fa', 'w') as out_file:
    for header, sequence in sequences.items():
        stops = find_in_frame_stops(sequence)

        if stops:
            gene_name = extract_gene_name(header)
            stop_list = ','.join(sorted(stops))
            out_file.write(f'>{gene_name}|{stop_list}\n')
            out_file.write(sequence + '\n')