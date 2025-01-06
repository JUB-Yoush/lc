"""
it being a square acc makes it easier
because every line needs to be the same length, we can check if any of the other points are in any of the 4 directinos
we only need to check 4 times for every query, once we've found one, we need to check all other
two hashmaps? one thats x:y and y:x
no because duplicates are seperate
grid of 1000
what if I just... made a 2d array
no too many 1000^2
I need a data structure that has fast lookup (check if point with x or y
tuple key, count value
we aren't shooting a ray (only for the first, which would be n)
is there a way to tell if there is a key with a specific x or y value?
neetcode solution:
- find a diagonal point first
- then, use the x and y's of the fount point and query point to check if a horiz and vert point also exist to make a whole square
"""

from collections import defaultdict


class DetectSquaresIncorrectly:
    def __init__(self) -> None:
        self.point_map = defaultdict(int)
        self.set_x = set()
        self.set_y = set()

    def add(self, point):
        self.point_map[(point[0], point[1])] += 1
        self.set_x.add(point[0])
        self.set_y.add(point[1])
        pass

    def count(self, point):
        squares = 0 
        line_exists = False
        side_len = 0
        for key,value in self.point_map.items():
            if key[1] == point[1]:
                line_exists = True
                side_len = abs(key[0] - point[0])

        if !line_exists:
            return

        valid_vert = (point[0] + side_len) in set_x or (point[0] - side_len) in set_x:
        DIR = [[1,1],[1,-1],[-1,1],[-1,-1]]
        valid_diag = False
        for dir in DIR:
            if (point[0] + side_len*dir) in set_x and(point[1] + side_len*dir) in set_y:
                valid_diag = True
        if valid_diag and valid_vert

                





class DetectSquares:
    def __init__(self) -> None:
        self.pts_count = defaultdict(int)
        self.pts = []
        pass

    def add(self, point):
        self.pts_count[tuple(point)] += 1
        self.pts.append(point)
        pass

    def count(self, point):
        res = 0
        px,py = point
        for x,y in self.pts:
            if(abs(py-y) != abs(px-x)) or x== px or y == py:
                continue
            res += self.pts_count[(x,py)] * self.pts_count[(px,y)]
        return res




        pass
