# AOC 2022 Day 3
# 12/3/2022

UPPERCASE_PRIORITY_CONVERSION = 38
LOWERCASE_PRIORITY_CONVERSION = 96


#  Does part one of day 3 for advent of code
#  Which is to take a string, split it in half and find
#  which letter occurs in both halves and then add the score of it
#  To the running total using the priority() method
def main():
    lines = readFile()
    total = 0

    for line in lines:
        compartment_one = line[0:len(line) // 2]  # Get the first half of the line
        compartment_two = line[len(line) // 2:].strip("\n")  # Get the second half of the line

        #  Loop through each letter and only processing it if it's found in both halves
        #  Only process the duplicate once
        for letter in set(compartment_one):
            if letter in compartment_two:
                repeated_letter = letter
                total += priority(repeated_letter)

    print(f"The answer to part one is: {total}")
    partTwo(lines)


def partTwo(lines):
    """
    This function takes in puzzle input as an array of strings and will
    loop through groups of 3, finding the item in common between them
    and adding the score of that to the running total using priority()

    :param lines: An array of strings that you wish to process
    :return: None
    """
    done = False
    index = 0
    total = 0

    while not done:
        group_part_one = lines[index].strip("\n")  # Get the first member of the group
        group_part_two = lines[index + 1].strip("\n")  # Get the second member of the group
        group_part_three = lines[index + 2].strip("\n")  # Get the third member of the group

        for letter in set(group_part_one):  # Loop through every letter
            #  Only process the letter if it's found in all 3 members of the group
            #  And only process the letter once
            if letter in group_part_two and letter in group_part_three:
                repeated_letter = letter
                total += priority(repeated_letter)

        index += 3  # Increment index by 3 because we are using 3 lines at a time
        if index == len(lines):
            done = True

    print(f"The answer to part two is: {total}")


def readFile():
    with open("input.txt") as file:
        lines = file.readlines()

    return lines


def priority(letter):
    # This function converts letters into their priorities
    if str(letter).isupper():  # for upper case letters
        return ord(letter) - UPPERCASE_PRIORITY_CONVERSION
    elif str(letter).islower():  # For lower case letters
        return ord(letter) - LOWERCASE_PRIORITY_CONVERSION


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
