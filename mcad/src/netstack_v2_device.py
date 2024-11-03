"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, polygon, translate
from solid.objects import color
from solid.utils import linear_extrude
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

from m3_bolt import m3_bolt_tapping_hole

# Configurable design parameters.
wall = 8
tolerance_xy = 0.3
padding = 5

# Dimension of the network appliance.
device_x = 136
device_y = 126
device_z = 40
device_r = 8

# Dimensions of the network appliance mounting holes.
hole_xy = 70
hole_margin_x = 33
hole_margin_y = 28

screw_margin = 70

solid = combine(
    polygon(
        [
            *arc2d(Point2(device_r, device_r), device_r, 180, 270),
            *arc2d(Point2(device_x - device_r,  device_r), device_r, 270, 360),
            *arc2d(Point2(device_x - device_r, device_y - device_r), device_r, 0, 90),
            *arc2d(Point2(device_r, device_y - device_r), device_r, 90, 180),
        ],
    ),
    linear_extrude(device_z),
    color("#333", 0.5),
)

solid -= combine(
    m3_bolt_tapping_hole(),
    translate([hole_margin_x, hole_margin_y + screw_margin / 2, 0]),
)
solid -= combine(
    m3_bolt_tapping_hole(),
    translate([hole_margin_x + screw_margin, hole_margin_y + screw_margin / 2, 0]),
)
solid -= combine(
    m3_bolt_tapping_hole(),
    translate([hole_margin_x + screw_margin / 2, hole_margin_y, 0]),
)
solid -= combine(
    m3_bolt_tapping_hole(),
    translate([hole_margin_x + screw_margin / 2, hole_margin_y + screw_margin, 0]),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
