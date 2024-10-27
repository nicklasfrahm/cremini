"""
A toleance test for an M3 bolt.
"""
from solid import OpenSCADObject, polygon, cylinder, translate
from solid.objects import color
from solid.utils import linear_extrude, down, up
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

pitch = 8
increment = 0.05
cols = 10
rows = 2

tol_z = 0.1

bolt_head_z = 3
bolt_head_r = 5.3 / 2
bold_head_clearance_r = 6 / 2
bolt_thread_z = 10
bolt_thread_major_r = 3 / 2
bolt_thread_tapping_r = 2.5 / 2
bolt_thread_clearance_r = 3.6 / 2

solid_x = pitch * (cols + 1)
solid_y = pitch * (rows + 1)
solid_z = bolt_head_z + bolt_thread_z
solid_r = 2

def bolt(thread_r = bolt_thread_major_r):
    """
    Create a bolt.
    """
    head = combine(
        cylinder(r=bold_head_clearance_r, h=bolt_head_z+tol_z),
        up(bolt_thread_z),
    )

    thread = combine(
        cylinder(r=thread_r, h=bolt_thread_z+tol_z*2),
        down(tol_z),
    )

    return head + thread

solid = combine(
    polygon(
        [
            *arc2d(Point2(solid_r, solid_r), solid_r, 180, 270),
            *arc2d(Point2(solid_x - solid_r,  solid_r), solid_r, 270, 360),
            *arc2d(Point2(solid_x - solid_r, solid_y - solid_r), solid_r, 0, 90),
            *arc2d(Point2(solid_r, solid_y - solid_r), solid_r, 90, 180),
        ],
    ),
    linear_extrude(solid_z),
    color("#333", 0.5),
)

for i in range(cols):
    for j in range(rows):
        # Scenarios:
        # - 1. self-tapping fitting
        # - 2. clearance fitting
        thread_r = bolt_thread_tapping_r + increment * i
        if j == 1:
            thread_r = bolt_thread_clearance_r + increment * i

        solid -= combine(
            bolt(thread_r=thread_r),
            translate([(1 + i) * pitch, (1 + j) * pitch, 0]),
        )

solid = combine(
    solid,
    color("#666"),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
