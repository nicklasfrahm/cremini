"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, cube, translate, rotate
from solid.objects import color
from lib.utils import build, combine
from lib.units import rxxr

from netstack_v2_device import wall, tolerance_xy, tolerance_z, rail_clearance
from netstack_v2_supply import supply_case_x, supply_case_y, supply_case_z, supply_x, supply_y, supply_z, supply_slot_x, supply_slot_z
from m3_bolt import m3_bolt_tapping_hole, thread_z

overlap = 0.1

solid = combine(
    cube([supply_case_x + rail_clearance + rxxr(1.5), supply_case_y, supply_case_z]),
    color("#333", 0.5),
)

# Create space for the mounting rail.
solid -= combine(
    cube([rail_clearance + rxxr(1.5) + overlap, supply_case_y - wall + overlap, supply_case_z + 2 * overlap]),
    translate([supply_case_x, wall, -overlap]),
)

solid -= combine(
    cube([rxxr(1.5), wall / 2 + overlap, supply_case_z + 2 * overlap]),
    translate([supply_case_x + rail_clearance + overlap, wall / 2 + overlap, -overlap]),
)

# Create space for the power supply.
solid -= combine(
    cube([supply_x + tolerance_xy, supply_y + tolerance_xy, supply_z + tolerance_z + overlap]),
    translate([wall, wall, -overlap]),
)

# Create space for the cables of the spine switches.
solid -= combine(
    cube([supply_slot_x, supply_case_y + 2 * overlap, supply_slot_z + overlap]),
    translate([wall, -overlap, -overlap]),
)

solid = combine(
    solid,
    color("#ff9800", 0.5),
)

# Create mounting holes for the power supply.
solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([wall / 2, wall / 2, thread_z]),
)

solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([supply_case_x - wall / 2, wall / 2, thread_z]),
)

solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([wall / 2, supply_case_y - wall / 2, thread_z]),
)

solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([supply_case_x - wall / 2, supply_case_y - wall / 2, thread_z]),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
