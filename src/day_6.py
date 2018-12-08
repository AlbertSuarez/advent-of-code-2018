import math


"""
Day 6: Chronal Coordinates
"""


_INPUT_FILE = 'data/day_6_input.txt'


def solve():
    """
    PART 1:

    The device on your wrist beeps several times, and once again you feel like you're falling.

    "Situation critical," the device announces. "Destination indeterminate. Chronal interference detected.
    Please specify new target coordinates."

    The device then produces a list of coordinates (your puzzle input). Are they places it thinks are safe
    or dangerous? It recommends you check manual page 729. The Elves did not give you a manual.

    If they're dangerous, maybe you can minimize the danger by finding the coordinate that gives the largest
    distance from the other points.

    Using only the Manhattan distance, determine the area around each coordinate by counting the number of integer
    X,Y locations that are closest to that coordinate (and aren't tied in distance to any other coordinate).

    Your goal is to find the size of the largest area that isn't infinite. For example, consider the
    following list of coordinates:

    1, 1
    1, 6
    8, 3
    3, 4
    5, 5
    8, 9
    If we name these coordinates A through F, we can draw them on a grid, putting 0,0 at the top left:

    ..........
    .A........
    ..........
    ........C.
    ...D......
    .....E....
    .B........
    ..........
    ..........
    ........F.
    This view is partial - the actual grid extends infinitely in all directions. Using the Manhattan
    distance, each location's closest coordinate can be determined, shown here in lowercase:

    aaaaa.cccc
    aAaaa.cccc
    aaaddecccc
    aadddeccCc
    ..dDdeeccc
    bb.deEeecc
    bBb.eeee..
    bbb.eeefff
    bbb.eeffff
    bbb.ffffFf
    Locations shown as . are equally far from two or more coordinates, and so they don't count as being closest to any.

    In this example, the areas of coordinates A, B, C, and F are infinite - while not shown here, their
    areas extend forever outside the visible grid. However, the areas of coordinates D and E are finite:
    D is closest to 9 locations, and E is closest to 17 (both including the coordinate's location itself).
    Therefore, in this example, the size of the largest area is 17.

    What is the size of the largest area that isn't infinite?

    --------------------------------------------------------------------------------------------------------------------

    PART 2:

    On the other hand, if the coordinates are safe, maybe the best you can do is try to find a region near as
    many coordinates as possible.

    For example, suppose you want the sum of the Manhattan distance to all of the coordinates to be less than 32.
    For each location, add up the distances to all of the given coordinates; if the total of those distances is
    less than 32, that location is within the desired region. Using the same coordinates as above,
    the resulting region looks like this:

    ..........
    .A........
    ..........
    ...###..C.
    ..#D###...
    ..###E#...
    .B.###....
    ..........
    ..........
    ........F.
    In particular, consider the highlighted location 4,3 located at the top middle of the region. Its calculation
    is as follows, where abs() is the absolute value function:

    Distance to coordinate A: abs(4-1) + abs(3-1) =  5
    Distance to coordinate B: abs(4-1) + abs(3-6) =  6
    Distance to coordinate C: abs(4-8) + abs(3-3) =  4
    Distance to coordinate D: abs(4-3) + abs(3-4) =  2
    Distance to coordinate E: abs(4-5) + abs(3-5) =  3
    Distance to coordinate F: abs(4-8) + abs(3-9) = 10
    Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30
    Because the total distance to all coordinates (30) is less than 32, the location is within the region.

    This region, which also includes coordinates D and E, has a total size of 16.

    Your actual region will need to be much larger than this example, though, instead including all locations
    with a total distance of less than 10000.

    What is the size of the region containing all locations which have a total distance to all given coordinates
    of less than 10000?
    """
    with open(_INPUT_FILE) as file:
        coordinates = file.read().splitlines()

    coordinates = [coordinate.replace(' ', '').split(',') for coordinate in coordinates if coordinate]

    print('Get matrix dimensions and build area dictionary')
    area_dict = {}
    area_key = 1
    max_i = max_j = 0
    for i, j in coordinates:
        area_dict[area_key] = dict(coordinates=[int(i), int(j)])
        area_key += 1
        if int(i) > max_i:
            max_i = int(i)
        if int(j) > max_j:
            max_j = int(j)

    print('Build matrix')
    matrix = []
    distance = []
    distance_safe = []
    for i in range(0, max_i):
        matrix.append([])
        distance.append([])
        distance_safe.append([])
        for j in range(0, max_j):
            matrix[i].append(0)
            distance[i].append(math.inf)
            distance_safe[i].append(0)

    print('Iterate over input')
    inf_keys = {}
    for key, value in area_dict.items():
        print('Calculate distances for {}'.format(key))
        for i in range(0, max_i):
            for j in range(0, max_j):
                is_limit = i == 0 or j == 0 or i + 1 == max_i or j + 1 == max_j
                manhattan_distance = abs(value['coordinates'][0] - i + 1) + abs(value['coordinates'][1] - j + 1)
                distance_safe[i][j] += manhattan_distance
                if manhattan_distance < distance[i][j]:
                    distance[i][j] = manhattan_distance
                    matrix[i][j] = key
                elif manhattan_distance == distance[i][j]:
                    matrix[i][j] = -1
                if is_limit and manhattan_distance <= distance[i][j]:
                    inf_keys[key] = True

    print('Calculate area')
    result_dict = {}
    for i in range(0, max_i):
        for j in range(0, max_j):
            key = matrix[i][j]
            if key != -1:
                if key not in result_dict:
                    result_dict[key] = 0
                result_dict[key] += 1

    print('Set infinite values')
    for key in inf_keys.keys():
        result_dict[key] = -1

    print('Get maximum area')
    sort_area = sorted(result_dict, key=result_dict.get, reverse=True)

    print('Part 1: Maximum area = {}'.format(result_dict[sort_area[0]]))

    print('Get safe area')
    safe_area = 0
    for i in range(0, max_i):
        for j in range(0, max_j):
            if distance_safe[i][j] < 10000:
                safe_area += 1

    print('Part 2: Safe area = {}'.format(safe_area))


if __name__ == '__main__':
    solve()
