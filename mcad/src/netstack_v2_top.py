"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, cube, translate
from solid.objects import color
from lib.utils import build, combine
from lib.units import rxxr

from netstack_v2_device import wall, tolerance_xy, tolerance_z
from netstack_v2_supply import supply_case_x, supply_case_y, supply_case_z, supply_x, supply_y, supply_z, supply_slot_x, supply_slot_z

overlap = 0.1

solid = combine(
    cube([supply_case_x + wall + rxxr(1), supply_case_y, supply_case_z]),
    color("#333", 0.5),
)

# Create space for the mounting rail.
solid -= combine(
    cube([wall + rxxr(1) + overlap, supply_case_y - wall + overlap, supply_case_z + 2 * overlap]),
    translate([supply_case_x, wall, -overlap]),
)

# Create space for the power supply.
solid -= combine(
    cube([supply_x + tolerance_xy, supply_y + tolerance_xy, supply_z + tolerance_z + overlap]),
    translate([wall, wall, -overlap]),
)

# Create space the the cables.
solid -= combine(
    cube([supply_slot_z, supply_case_y + 2 * overlap, supply_slot_z + overlap]),
    translate([wall, -overlap, -overlap]),
)

solid = combine(
    solid,
    color("#ff9800", 0.5),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
