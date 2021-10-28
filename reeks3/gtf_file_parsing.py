def solution():
    # Solution starts here
    # Not sure if this one is correct, do we just have to count the number of lines per chromosome?
    elements = {}
    with open('resources/gencode.gtf') as file:  # ! path to file can change
        for line in file:
            chromosome = line[:line.index(' ')]  # the chromosome is the string before the first space
            if chromosome in elements.keys():
                elements[chromosome] += 1  # if we have the key in the dict, add 1
            else:
                elements[chromosome] = 1  # if we don't have the key in the dict, put the value to 1
    for key in sorted(elements.keys()):
        print('{}\t{}'.format(key, elements[key]))  # for each sorted key in the dict, print the key and value
    # Solution ends here


if __name__ == '__main__':
    solution()
