"""
An test file to calibrate 3D-printing shrinkage.
"""
from math import floor
from solid import OpenSCADObject
from solid.objects import translate, cube, color
from lib.utils import build, combine
from lib.units import rxxu, r19i
from lib.features import corners

from netstack_v1_nanopir5s import r5s_x, r5s_y, r5s_z

tol_z = 0.15
tol_xy = 0.4
unit_count = 4
margin_screw = 10
margin_base = 3
vent_count = 5

# Create the outline of the case.
case_x = (floor(r19i(1)) - unit_count * margin_base) / 3
case_y = r5s_y + 2 * margin_base + 2 * tol_xy
case_z = rxxu(1) - 2 * tol_z
solid = cube([case_x, case_y, case_z])

# Define the pocket for the Nanopi R5S.
pocket_x = r5s_x + 2 * tol_xy
pocket_y = r5s_y + 2 * tol_xy
pocket_z = r5s_z + 2 * tol_z

# Create slot to remove the Nanopi R5S.
slot_x = pocket_x / 2
slot_y = pocket_y / 2
slot_z = margin_base + 2 * tol_z
slot = combine(
    cube([slot_x, slot_y, slot_z]),
    translate([(case_x - slot_x) / 2, (case_y - slot_y) / 2, -tol_z]),
)
solid -= slot

# Create access holes for the Nanopi R5S.
front_x = pocket_x
front_y = case_y + 2 * tol_xy
front_z = r5s_z + 2 * tol_z
front = combine(
    cube([front_x, front_y, front_z]),
    translate([(case_x - front_x) / 2, -(margin_base + tol_xy), margin_base]),
)
solid -= front

# Create rear access holes for the Nanopi R5S.
rear_x = pocket_x - 2 * margin_base
rear_y = case_y + 2 * tol_xy
rear_z = r5s_z - 2 * margin_base + 2 * tol_z
rear = combine(
    cube([rear_x, rear_y, rear_z]),
    translate([(case_x - rear_x) / 2, -tol_xy, margin_base * 2]),
)
solid -= rear

# Create vents for the Nanopi R5S.
vent_x = (pocket_x - (vent_count - 1) * margin_base) / vent_count
vent_y = case_y + 2 * tol_xy
vent_z = case_z - pocket_z - 2 * margin_base + tol_z
vent = cube([vent_x, vent_y, vent_z], center=True)
vent -= combine(
    cube([vent_x + 2 * tol_xy, margin_base + 2 * tol_xy, margin_base + tol_xy], center=True),
    translate([0, (vent_y - margin_base) / 2 + tol_xy, -margin_base - tol_z]),
)
vent -= combine(
    cube([vent_x + 2 * tol_xy, margin_base + 2 * tol_xy, margin_base + tol_xy], center=True),
    translate([0, -(vent_y - margin_base) / 2, -margin_base - tol_z]),
)
vent = combine(
    vent,
    translate([vent_x / 2, vent_y / 2, vent_z / 2 - 2 * tol_z]),
)
for i in range(vent_count):
    solid -= combine(
        vent,
        translate([(case_x - pocket_x) / 2 + margin_base * i + vent_x * i, - tol_xy, case_z - vent_z - margin_base])
    )

# Create latch.
latch_x = margin_base * 3 + tol_xy
latch_y = case_y - 2 * margin_base - tol_xy
latch_z = pocket_z - 2 * margin_base
latch_cutout = combine(
    cube([latch_x, latch_y, pocket_z]),
    translate([(case_x - pocket_x) / 2 - latch_x + tol_xy, -tol_xy, margin_base]),
)
solid -= latch_cutout

latch = combine(
    cube([latch_x, 3 * margin_base, latch_z]),
    translate([0, latch_y - 3 * margin_base, 0]),
)
latch += combine(
    cube([margin_base, latch_y + tol_xy, latch_z]),
    translate([latch_x - margin_base, -tol_xy, 0]),
)
latch += combine(
    cube([margin_base * 3, margin_base * 4, latch_z]),
    translate([latch_x - margin_base * 2, -(tol_xy + margin_base * 3), 0]),
)
latch = combine(
    latch,
    translate([(case_x - pocket_x) / 2 - latch_x + tol_xy, -tol_xy, margin_base * 2]),
)
solid += latch

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
