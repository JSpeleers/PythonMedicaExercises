input_line_number = 0
lines = []


def input():
    global input_line_number
    input_line_number += 1
    return lines[input_line_number - 1]


def solution():
    # Solution starts here
    # Given masses dictionary
    aa_mass = {'A': 71.03711, 'C': 103.00919, 'G': 57.02146, 'M': 131.04049, 'S': 87.03203, 'H': 137.05891,
               'N': 114.04293, 'T': 101.04768, 'D': 115.02694, 'I': 113.08406, 'E': 129.04259, 'P': 97.05276,
               'K': 128.09496, 'L': 113.08406, 'R': 156.10111, 'Y': 163.06333, 'V': 99.06841, 'Q': 128.05858,
               'W': 186.07931, 'F': 147.06841}

    protein_id = input()
    total_mass = 0
    while True:
        amino_acid_sequence = input()
        if amino_acid_sequence != '':
            for character in amino_acid_sequence:  # For each character in the amino acid sequence
                total_mass += aa_mass[character]  # Sum its mass
        else:  # Final empty line
            print('Protein {} has a mass of {:.2f} Da.'.format(protein_id, total_mass))
            break
    # Solution ends here


def solution_super_short():
    # Short solution starts here
    # Given masses dictionary
    aa_mass = {'A': 71.03711, 'C': 103.00919, 'G': 57.02146, 'M': 131.04049, 'S': 87.03203, 'H': 137.05891,
               'N': 114.04293, 'T': 101.04768, 'D': 115.02694, 'I': 113.08406, 'E': 129.04259, 'P': 97.05276,
               'K': 128.09496, 'L': 113.08406, 'R': 156.10111, 'Y': 163.06333, 'V': 99.06841, 'Q': 128.05858,
               'W': 186.07931, 'F': 147.06841}

    protein_id = input()
    complete_string = ''
    amino_acid_sequence = None
    while amino_acid_sequence != '':
        amino_acid_sequence = input()
        complete_string += amino_acid_sequence
    print('Protein {} has a mass of {:.2f} Da.'.format(protein_id, sum([aa_mass[char] for char in complete_string])))
    """ REMARK: Here we take the sum of the list of all the masses using List Comprehensions """
    # Short solution ends here


if __name__ == '__main__':
    with open('resources/input_mass_of_a_protein.txt') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    solution()
    input_line_number = 0
    solution_super_short()
