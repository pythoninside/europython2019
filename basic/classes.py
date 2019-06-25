# Every class is a valid type.
from typing import ClassVar


class Point:
    x: int      # considered an instance variable
    y: int      # considered as instance variable
    num_points: ClassVar[int] = 0       # class variable

    def __init__(self, x: int, y: int) -> None:  # Do not annotate self
        self.x = x
        self.y = y
        Point.num_points += 1


class Point3D(Point):
    z: int

    def __init__(self, x: int, y: int, z: int) -> None:
        super().__init__(x, y)
        self.z = z


p = Point(1, 2)
# p.x = 1.2               # type error
# p.num_points += 1       # p cannot write to a class variable
print(p.num_points)     # OK
p3 = Point3D(1, 2, 3)
# p3 = p                  # error: cannot use a Point in place of a Point3D
p = p3                  # OK: Point3D upgraded to the super type
