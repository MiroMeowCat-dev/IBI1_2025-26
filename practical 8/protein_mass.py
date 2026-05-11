def protein_mass(sequence):
    amino_acid_masses = {
        "A": 89.1,
        "C": 121.2,
        "D": 133.1,
        "E": 147.1,
        "F": 165.2,
        "G": 75.1,
        "H": 155.2,
        "I": 131.2,
        "K": 146.2,
        "L": 131.2,
        "M": 149.2,
        "N": 132.1,
        "P": 115.1,
        "Q": 146.2,
        "R": 174.2,
        "S": 105.1,
        "T": 119.1,
        "V": 117.1,
        "W": 204.2,
        "Y": 181.2
    }
    total_mass = 0.0

    for amino_acid in sequence:
        if amino_acid not in amino_acid_masses:
            raise ValueError(f"Invalid amino acid: {amino_acid}")
        total_mass += amino_acid_masses[amino_acid]

    return total_mass

# Example function call
example_sequence = "ACDE"
print("Protein mass:", protein_mass(example_sequence))
