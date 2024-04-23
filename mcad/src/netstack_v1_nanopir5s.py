"""
An test file to calibrate 3D-printing shrinkage.
"""
from solid import OpenSCADObject, polygon
from solid.objects import color
from solid.utils import linear_extrude
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

# Nanopi R5S dimensions.
r5s_x = 94.5
r5s_y = 68
r5s_z = 30
r5s_r = 4

solid = combine(
    polygon(
        [
            *arc2d(Point2(r5s_r, r5s_r), r5s_r, 180, 270),
            *arc2d(Point2(r5s_x - r5s_r,  r5s_r), r5s_r, 270, 360),
            *arc2d(Point2(r5s_x - r5s_r, r5s_y - r5s_r), r5s_r, 0, 90),
            *arc2d(Point2(r5s_r, r5s_y - r5s_r), r5s_r, 90, 180),
        ],
    ),
    linear_extrude(r5s_z),
    color("#333"),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
