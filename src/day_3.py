"""
Day 3: No Matter How You Slice It
"""


_INPUT_FILE = 'data/day_3_input.txt'


def _print_claim(santa_map, no_conflict_dict, number, i, j):
    if santa_map[i][j] == '.':
        santa_map[i][j] = number
        if number not in no_conflict_dict:
            no_conflict_dict[number] = True
    elif santa_map[i][j] == 'X':
        pass
    else:
        no_conflict_dict[santa_map[i][j]] = False
        santa_map[i][j] = 'X'
        no_conflict_dict[number] = False


def solve():
    """
    PART 1:

    The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully
    wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still
    affecting them - nobody can even agree on how to cut the fabric.

    The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

    Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and
    consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's
    rectangle is defined as follows:

    The number of inches between the left edge of the fabric and the left edge of the rectangle.
    The number of inches between the top edge of the fabric and the top edge of the rectangle.
    The width of the rectangle in inches.
    The height of the rectangle in inches.
    A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches
    from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented
    by # (and ignores the square inches of fabric represented by .) in the diagram below:

    ...........
    ...........
    ...#####...
    ...#####...
    ...#####...
    ...#####...
    ...........
    ...........
    ...........
    The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas.
    For example, consider the following claims:

    #1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2
    Visually, these claim the following areas:

    ........
    ...2222.
    ...2222.
    .11XX22.
    .11XX22.
    .111133.
    .111133.
    ........
    The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others,
    does not overlap either of them.)

    If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches
    of fabric are within two or more claims?

    --------------------------------------------------------------------------------------------------------------------

    PART 2:

    Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with
    any other claim. If you can somehow draw attention to it, maybe the Elves
    will be able to make Santa's suit after all!

    For example, in the claims above, only claim 3 is intact after all claims are made.

    What is the ID of the only claim that doesn't overlap?
    """
    with open(_INPUT_FILE) as file:
        claims = file.read().splitlines()

    santa_map = []
    for i in range(0, 1001):
        santa_map.append([])
        for j in range(0, 1001):
            santa_map[i].append('.')

    no_conflict_dict = {}
    for claim in claims:
        if claim:
            claim_split = claim.split(' ')
            claim_number = claim_split[0].replace('#', '')
            claim_left = claim_split[2].replace(':', '').split(',')[0]
            claim_top = claim_split[2].replace(':', '').split(',')[1]
            claim_width = claim_split[3].split('x')[0]
            claim_height = claim_split[3].split('x')[1]
            _print_claim(santa_map, no_conflict_dict, claim_number, int(claim_left), int(claim_top))
            for i in range(0, int(claim_width)):
                for j in range(0, int(claim_height)):
                    if i or j:
                        _print_claim(santa_map, no_conflict_dict, claim_number, int(claim_left) + i, int(claim_top) + j)

    count = 0
    for i in santa_map:
        for j in i:
            if j == 'X':
                count += 1

    print('Part 1: Square inches: {}'.format(count))

    no_conflict_claim = ''
    for key, value in no_conflict_dict.items():
        if value:
            no_conflict_claim = key

    print('Part 2: No conflict: {}'.format(no_conflict_claim))


if __name__ == '__main__':
    solve()
