import sys
sys.path.append('..')
import my_parser as p
import matplotlib.pyplot as plt

L = p.input_as_lines('inputs/inp.txt')

G = G = [[el for el in line] for line in L]
R = len(G)
C = len(G[0])

a, b = L

ins_a = a.split(',')
ins_a = [(el[0], int(el[1:])) for el in ins_a]

ins_b = b.split(',')
ins_b = [(el[0], int(el[1:])) for el in ins_b]


def get_endpoints(inss):
    m = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    pos = (0, 0)
    points = [pos]

    for ins in inss:
        dir, s = ins
        delta = m[dir]
        npos = (pos[0] + s * delta[0], pos[1] + s * delta[1])
        points.append(npos)

        pos = npos

    return points


def extract_points(p1, p2):
    if p1[0] - p2[0] == 0:
        delta = (0, 1)
        ys = [p1[1], p2[1]]
        r = range(min(ys), max(ys))
    elif p1[1] - p2[1] == 0:
        delta = (1, 0)
        xs = [p1[0], p2[0]]
        r = range(min(xs), max(xs))

    s = sorted([p1, p2], key=lambda x: sum(x))
    pos = s[0]
    points = set()
    points.add(pos)
    pos = list(pos)
    for i in r:
        pos[0] += delta[0]
        pos[1] += delta[1]
        points.add(tuple(pos))

    return points


def plot_all(points1, points2):
    """
    Plots two sets of line segments defined by consecutive points in each set.

    Parameters:
    - points1: A list of points [[x1, y1], [x2, y2], ...] defining the first set of segments.
    - points2: A list of points [[x3, y3], [x4, y4], ...] defining the second set of segments.
    """
    for i in range(len(points1) - 1):
        x1, y1 = points1[i]
        x2, y2 = points1[i + 1]
        plt.plot([x1, x2], [y1, y2], label="Set 1" if i == 0 else "", color='blue', linewidth=2)

    for i in range(len(points2) - 1):
        x1, y1 = points2[i]
        x2, y2 = points2[i + 1]
        plt.plot([x1, x2], [y1, y2], label="Set 2" if i == 0 else "", color='red', linewidth=2)

    # Add labels, legend, and grid
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.title("Two Sets of Line Segments")

    # Use unique legend labels for the sets
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    # Adjust limits for better visualization
    all_points = points1 + points2
    all_x = [p[0] for p in all_points]
    all_y = [p[1] for p in all_points]
    plt.xlim(min(all_x) - 1, max(all_x) + 1)
    plt.ylim(min(all_y) - 1, max(all_y) + 1)

    # Show the plot
    plt.show()


def find_intersections(pa, pb):
    intersections = set()
    for la1, la2 in list(zip(pa[:-1], pa[1:])):
        for lb1, lb2 in list(zip(pb[:-1], pb[1:])):
            xrangea = min(la1[0], la2[0]), max(la1[0], la2[0])
            xrangeb = min(lb1[0], lb2[0]), max(lb1[0], lb2[0])
            yrangea = min(la1[1], la2[1]), max(la1[1], la2[1])
            yrangeb = min(lb1[1], lb2[1]), max(lb1[1], lb2[1])

            # if xrange b in xrange a and yrange a in yrange b or vice versa:
            if xrangea[0] <= lb1[0] <= xrangea[1]:
                if yrangeb[0] <= la1[1] <= yrangeb[1]:
                    subpa = extract_points(la1, la2)
                    subpb = extract_points(lb1, lb2)
                    sub_intersections = subpa & subpb
                    intersections = intersections | sub_intersections

            # vice versa
            if xrangeb[0] <= la1[0] <= xrangeb[1]:
                if yrangea[0] <= lb1[1] <= yrangea[1]:
                    subpa = extract_points(la1, la2)
                    subpb = extract_points(lb1, lb2)
                    sub_intersections = subpa & subpb
                    intersections = intersections | sub_intersections

    return intersections


def dist(a, b):
    a1, a2, = a
    b1, b2 = b
    return abs(a1 - b1) + abs(a2 - b2)


def find_closest_intersection(ps):
    ps = list(ps)
    return sorted(ps, key=lambda x: dist(x, (0, 0)))[0]


end_points_a = get_endpoints(ins_a)
end_points_b = get_endpoints(ins_b)

plot_all(end_points_a, end_points_b)

intersections = find_intersections(end_points_a, end_points_b)
intersections.remove((0, 0))

closest = find_closest_intersection(intersections)
print(dist(closest, (0, 0)))


def steps_to_point(inss, point):
    m = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    pos = (0, 0)
    steps = 0

    for ins in inss:
        dir, s = ins
        delta = m[dir]
        npos = (pos[0] + s * delta[0], pos[1] + s * delta[1])
        if pos[0] == npos[0] == point[0]:
            if min(pos[1], npos[1]) <= point[1] <= max(pos[1], npos[1]):
                return steps + point[1] - min(pos[1], npos[1])
        elif pos[1] == npos[1] == point[1]:
            if min(pos[0], npos[0]) <= point[0] <= max(pos[0], npos[0]):
                return steps + point[0] - min(pos[0], npos[0])

        steps += abs(s * delta[0]) + abs(s * delta[1])
        pos = npos

    return steps

p2p = (0, 0)
p2 = float('inf')

for p in intersections:
    steps_a = steps_to_point(ins_a, p)
    steps_b = steps_to_point(ins_b, p)
    score = steps_a + steps_b
    if score < p2:
        p2 = score
        p2p = p

print(p2)
