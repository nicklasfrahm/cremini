"""
An assembly of the Netstack V2 device and the mounting rails.
"""
from solid import OpenSCADObject
from solid.objects import translate, cube, color
from lib.utils import build, combine
from lib.units import rxxu, rxxr, r19i

from netstack_v2_device import obj as device
from netstack_v2_device import device_x

solid = combine(
    device(),
    translate([r19i(1) - device_x, 0, 0]),
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

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
