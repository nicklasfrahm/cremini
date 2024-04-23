"""
An test file to calibrate 3D-printing shrinkage.
"""
from solid import OpenSCADObject, cube
from solid.objects import translate, color
from lib.utils import build, combine
from lib.units import rxxu, rxxr, r19o

# Design parameters.
brim = 5
tol_xy = 0.25

# Nanopi R5S dimensions.
r5s_x = 94.5
r5s_y = 68
r5s_z = 30

case_x = r5s_x + 2 * brim
case_y = r5s_y + 2 * brim
case_z = brim

solid = combine(
    cube([case_x, case_y, case_z]),
    translate([0, 0, 0]),
    color("#333"),
)

pocket_x = r5s_x + 2 * tol_xy
pocket_y = r5s_y + 2 * tol_xy
pocket_z = r5s_z

solid -= combine(
    cube([pocket_x, pocket_y, pocket_z + 2]),
    translate([brim - (tol_xy / 2), brim - (tol_xy / 2), -1]),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
