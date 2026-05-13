def read_fasta(filename):
    name = ""
    sequence_parts = []

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                name = line[1:]
            else:
                sequence_parts.append(line)

    sequence = "".join(sequence_parts)
    return name, sequence

def read_blosum62(filename):
    matrix = {}

    with open(filename, "r") as file:
        lines = file.readlines()

    header = lines[0].split()

    for line in lines[1:]:
        parts = line.split()
        row_amino_acid = parts[0]
        scores = parts[1:]

        for i in range(len(header)):
            column_amino_acid = header[i]
            score = int(scores[i])
            matrix[(row_amino_acid, column_amino_acid)] = score

    return matrix

def compare_sequences(name1, seq1, name2, seq2, blosum_matrix):
    total_score = 0
    identical_count = 0

    sequence_length = min(len(seq1), len(seq2))

    for i in range(sequence_length):
        aa1 = seq1[i]
        aa2 = seq2[i]

        score = blosum_matrix[(aa1, aa2)]
        total_score += score

        if aa1 == aa2:
            identical_count += 1

    percentage_identity = identical_count / sequence_length * 100
    normalised_score = total_score / sequence_length

    print("=" * 60)
    print(f"Comparison: {name1} vs {name2}")
    print(f"Sequence length compared: {sequence_length}")
    print(f"BLOSUM62 total score: {total_score}")
    print(f"Normalised score per amino acid: {normalised_score:.2f}")
    print(f"Identical amino acids: {identical_count}")
    print(f"Percentage identity: {percentage_identity:.2f}%")
    print("=" * 60)
    print()

blosum62 = read_blosum62("blosum62.txt")

human_name, human_seq = read_fasta("human_DLX5.fasta")
mouse_name, mouse_seq = read_fasta("mouse_DLX5.fasta")
random_name, random_seq = read_fasta("random.fasta")

compare_sequences(human_name, human_seq, mouse_name, mouse_seq, blosum62)
compare_sequences(human_name, human_seq, random_name, random_seq, blosum62)
compare_sequences(mouse_name, mouse_seq, random_name, random_seq, blosum62)