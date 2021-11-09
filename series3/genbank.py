# Solution starts here
def genbank(block_size, number_of_blocks, sequence):
    sequence = sequence.lower()
    k_print_padding = len(str(len(sequence) - (len(sequence) % (block_size * number_of_blocks))))
    string_to_return = ''
    for line_index in range(0, -(-len(sequence) // (block_size * number_of_blocks))):  # For each line to print
        """ REMARK: The end index in this range() above, is the ceiling of the division (same as math.ceil()) """
        # Create a string with the 'k' number with padding
        line = '{: >{}}'.format(line_index * block_size * number_of_blocks + 1, k_print_padding)
        """ REMARK: The formatting {:>5} will pad the given string to length 5. 
        In the line above, the number of padding is also a parameter of format() """
        for block_index in range(0, number_of_blocks):
            # Calculate begin and end index of the blocks of the line
            block_start_index = line_index * block_size * number_of_blocks + block_size * block_index
            block_end_index = line_index * block_size * number_of_blocks + block_size * (block_index + 1)
            # Append the block of the sequence
            line += ' {}'.format(sequence[block_start_index: block_end_index])
        string_to_return += line + '\n'
    return string_to_return.rstrip()


# Solution ends here


if __name__ == '__main__':
    print(genbank(4, 3, 'AGGCTGTCAATGCTAGGCATAgaagtcgTGCTGTAGagatagTCTGATAGTCGC'))
    print('---')
    print(genbank(5, 2, 'GGATGCTGGTAGATCGATAT'))
    print('---')
    print(genbank(10, 6, 'AGCT' * 252))
