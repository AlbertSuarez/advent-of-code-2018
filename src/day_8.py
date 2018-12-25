"""
Day 8: Memory Maneuver
"""


_INPUT_FILE = 'data/day_8_input.txt'


def build(idx, numbers, result):
    if idx == len(numbers):
        return

    # Get header info
    child_nodes = numbers[idx]
    idx += 1
    metadata_entries = numbers[idx]

    # Get recursively children information
    if child_nodes:
        idx += 1
        build(idx, numbers, result)

    idx += 1 if metadata_entries else 0
    result += sum(numbers[idx:idx + metadata_entries + 1 if metadata_entries else 0])
    idx += metadata_entries

    idx += 1
    build(idx, numbers, result)


def solve():
    """
    PART 1:

    The sleigh is much easier to pull than you'd expect for something its weight. Unfortunately, neither you nor the Elves know which way the North Pole is from here.

    You check your wrist device for anything that might help. It seems to have some kind of navigation system! Activating the navigation system produces more bad news: "Failed to start navigation system. Could not read software license file."

    The navigation system's license file consists of a list of numbers (your puzzle input). The numbers define a data structure which, when processed, produces some kind of tree that can be used to calculate the license number.

    The tree is made up of nodes; a single, outermost node forms the tree's root, and it contains all other nodes in the tree (or contains nodes that contain nodes, and so on).

    Specifically, a node consists of:

    A header, which is always exactly two numbers:
    The quantity of child nodes.
    The quantity of metadata entries.
    Zero or more child nodes (as specified in the header).
    One or more metadata entries (as specified in the header).
    Each child node is itself a node that has its own header, child nodes, and metadata. For example:

    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    A----------------------------------
        B----------- C-----------
                         D-----
    In this example, each node of the tree is also marked with an underline starting with a letter for easier identification. In it, there are four nodes:

    A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
    B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
    C, which has 1 child node (D) and 1 metadata entry (2).
    D, which has 0 child nodes and 1 metadata entry (99).
    The first check done on the license file is to simply add up all of the metadata entries. In this example, that sum is 1+1+2+10+11+12+2+99=138.

    What is the sum of all metadata entries?
    """
    # This solution does not work.
    print('Read file')
    with open(_INPUT_FILE) as file:
        numbers = [int(number_str) for number_str in file.read().splitlines()[0].split(' ')]

    print('Build dictionary')
    result = 0
    build(0, numbers, result)

    print('Part 1: Sum of all metadata entries = {}'.format(result))


if __name__ == '__main__':
    solve()
