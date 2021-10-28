def solution():
    # Solution starts here
    with open('resources/woordenlijst.txt') as file:
        for line in file:
            line = line.rstrip()  # Remove whitespace and newline
            if line == line[::-1]:  # Is line equals the reversed line
                print(line)
    # Solution ends here


if __name__ == '__main__':
    solution()
