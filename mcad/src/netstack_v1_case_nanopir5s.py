"""
An test file to calibrate 3D-printing shrinkage.
"""
from math import floor
from solid import OpenSCADObject
from solid.objects import translate, cube, scale, color, cylinder
from solid.utils import up, rotate
from lib.utils import build, combine
from lib.units import rxxu, r19i, inches
from lib.features import corners, corner

from netstack_v1_nanopir5s import r5s_x, r5s_y, r5s_z

tol_z = 0.1
tol_xy = 0.25
unit_count = 4
margin_screw = 10
margin_base = 3
margin_case = margin_base * 1

# Create the outline of the case.
case_x = (floor(r19i(1)) - unit_count * margin_base) / 3
case_y = r5s_y + 2 * margin_case
case_z = rxxu(1) - 2 * tol_z
solid = cube([case_x, case_y, case_z])

# Create the pocket for the Nanopi R5S.
pocket_x = r5s_x + 2 * tol_xy
pocket_y = r5s_y + 2 * tol_xy
pocket = combine(
    cube([pocket_x, pocket_y, case_z]),
    scale([1, 1, case_z / r5s_z]),
    translate([(case_x - pocket_x) / 2, (case_y - pocket_y) / 2, margin_case]),
)
solid -= pocket

# Create slot to remove the Nanopi R5S.
slot_x = pocket_x / 2
slot_y = pocket_y / 2
slot_z = margin_case + 2 * tol_z
slot = combine(
    cube([slot_x, slot_y, slot_z]),
    translate([(case_x - slot_x) / 2, (case_y - slot_y) / 2, -tol_z]),
)
solid -= slot

# Create access holes for the Nanopi R5S.
front_x = pocket_x - 2 * margin_base
front_y = case_y + 2 * margin_base
front_z = r5s_z - 2 * margin_base
front = combine(
    cube([front_x, front_y, front_z]),
    translate([(case_x - front_x) / 2, -margin_base, margin_base + margin_case]),
)
solid -= front

# Align case to ensure symmetric screw holes.
solid = combine(
    solid,
    translate([0, 0, (rxxu(1) - case_z) / 2]),
)

# Create the screw holes.
solid -= corners(
    case_x,
    case_y,
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
