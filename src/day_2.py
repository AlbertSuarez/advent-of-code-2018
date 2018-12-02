"""
Day 2: Inventory Management System
"""


_INPUT_FILE = 'data/day_2_input.txt'


def solve_part_1():
    """
    "Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box
    IDs should be similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk
    too far away to hear any more.

    Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were
    discovered - and use your fancy wrist device to quickly scan every box and produce a list of the likely candidates
    (your puzzle input).

    To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID
    containing exactly two of any letter and then separately counting those with exactly three of any letter. You can
    multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

    For example, if you see the following box IDs:

    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.
    Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter
    which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

    What is the checksum for your list of box IDs?
    """
    with open(_INPUT_FILE) as file:
        words = file.read().splitlines()

    count_twice = 0
    count_three_times = 0
    frequency = {}
    for word in words:
        if word:
            for character in word:
                if character not in frequency:
                    frequency[character] = 1
                else:
                    frequency[character] = frequency[character] + 1
            exists_twice = False
            exists_three_times = False
            for value in frequency.values():
                if value == 2:
                    exists_twice = True
                elif value == 3:
                    exists_three_times = True
            count_twice += int(exists_twice)
            count_three_times += int(exists_three_times)
            frequency = {}

    print('Part 1: Checksum = {}'.format(count_twice * count_three_times))


def solve_part_2():
    """
    Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

    The boxes will have IDs which differ by exactly one character at the same position in both strings.
    For example, given the following box IDs:
    abcde
    fghij
    klmno
    pqrst
    fguij
    axcye
    wvxyz
    The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the
    IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

    What letters are common between the two correct box IDs? (In the example above, this is found by
    removing the differing character from either ID, producing fgij.)
    """
    with open(_INPUT_FILE) as file:
        words = file.read().splitlines()

    len_characters = len(words[0])
    for i, first_word in enumerate(words):
        for j, second_word in enumerate(words):
            if first_word and second_word and i != j:
                common_characters = 0
                for idx in range(0, len_characters):
                    common_characters += int(first_word[idx] == second_word[idx])
                if common_characters == len_characters - 1:
                    result = ''
                    for idx in range(0, len_characters):
                        if first_word[idx] == second_word[idx]:
                            result += first_word[idx]
                    print('Part 2: Letters common = {}'.format(result))
                    return


if __name__ == '__main__':
    solve_part_1()
    solve_part_2()
