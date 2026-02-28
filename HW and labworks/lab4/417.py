from math import sqrt
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

def calculate_distance(point1: Point, point2: Point) -> float:
    dx = point2.x - point1.x
    dy = point2.y - point1.y

    distance = sqrt(dx**2 + dy**2)

    return distance

def is_inside(point: Point, r: float) -> bool:
    return point.x**2 + point.y**2 <= r**2
    
def calculate_inner_points(r, point1: Point, point2: Point):
    if is_inside(point1, r) and is_inside(point2, r):
        return point1, point2

    
    m = (point2.y - point1.y)/(point2.x - point1.x)
    a = 1 + m**2
    b = 2*point1.x + 2*point1.y*m
    c = point1.x**2 + point1.y**2 - r**2

    determinant = b**2 - 4*a*c

    if determinant <= 0:
        return Point(0, 0), Point(0, 0)
    else:
        k1 = (-b + sqrt(determinant))/(2*a)
        k2 = (-b - sqrt(determinant))/(2*a)

        intersection_point1 = Point(point1.x + k1, point1.y + m*k1)
        intersection_point2 = Point(point1.x + k2, point1.y + m*k2)

        if is_inside(point1, r):
            if calculate_distance(point2, intersection_point1) < calculate_distance(point2, intersection_point2):
                return point1, intersection_point1
            else:
                return point1, intersection_point2
        elif is_inside(point2, r):
            if calculate_distance(point1, intersection_point1) < calculate_distance(point1, intersection_point2):
                return point2, intersection_point1
            else:
                return point2, intersection_point2
        else:
            delta = point1.x - intersection_point1.x
            c = point2.x
            if delta == 0:
                delta = point1.y - intersection_point1.y
                c = point2.y
            
            k = c/delta

            if k >= 0:
                return Point(0, 0), Point(0,0)
            else:
                return intersection_point1, intersection_point2


r = float(input())

point1 = Point(*map(float, input().split()))
point2 = Point(*map(float, input().split()))

inner_point1, inner_point2 = calculate_inner_points(r, point1, point2)

length = calculate_distance(inner_point1, inner_point2)

print(f"{length:.10f}")