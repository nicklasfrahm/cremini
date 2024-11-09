"""
An assembly of the Netstack V2 device and the mounting rails.
"""
from solid import OpenSCADObject
from solid.objects import translate, cube, color
from lib.utils import build, combine
from lib.units import rxxu, rxxr, r19i

from netstack_v2_device import obj as device
from netstack_v2_device import hole_margin_x, wall, padding, rail_clearance
from netstack_v2_bottom import obj as bottom
from netstack_v2_bottom import bottom_x, bottom_z
from netstack_v2_supply import obj as supply
from netstack_v2_supply import supply_x, supply_case_x
from netstack_v2_top import obj as top

explosion = 0.1
offset_x = rail_clearance + rxxr(0.5)
offset_y = -wall / 2

solid = combine(
    device(),
    translate([r19i(1) - bottom_x - hole_margin_x + padding - offset_x, offset_y, bottom_z + explosion]),
)

# Create a mock of the mounting rails.
rail = cube([rxxr(1), rxxr(1), rxxu(3)])
rails = combine(
    rail,
    translate([-rxxr(1), 0, -rxxu(1)]),
)

rails += combine(
    rail,
    translate([r19i(1), 0, -rxxu(1)]),
)

rails = combine(
    rails,
    color("#333"),
)

solid += rails

solid += combine(
    bottom(),
    translate([r19i(1) - bottom_x - offset_x, offset_y, 0]),
)

solid += combine(
    supply(),
    translate([r19i(1) - supply_x - wall - offset_x, wall + offset_y, bottom_z + explosion]),
)

solid += combine(
    top(),
    translate([r19i(1) - supply_case_x - offset_x, offset_y, bottom_z]),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
