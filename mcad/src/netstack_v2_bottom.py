"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, polygon, translate, rotate
from solid.objects import color
from solid.utils import linear_extrude
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

from m3_bolt import m3_bolt_clearance_hole, bolt_thread_z, bolt_head_z
from netstack_v2_supply import supply_case_x, supply_case_y

# Configurable design parameters.
tolerance_xy = 0.3
padding = 5
wall = 8
device_r = 8
supply_r = 1
cable_slot = 15
bottom_z = 4

# Dimensions of the network appliance mounting holes.
hole_xy = 70
hole_margin_x = 33

# Dimensions of the mounting plate for the network appliance.
device_plate_x = padding + hole_xy + hole_margin_x + cable_slot
device_plate_y = hole_xy + 2 * padding
device_plate_z = bottom_z

margin_y = (supply_case_y - device_plate_y) / 2

bottom_x = device_plate_x + supply_case_x
bottom_y = supply_case_y

solid = combine(
    polygon(
        [
            *arc2d(Point2(device_r, device_r), device_r, 270, 180),
            *arc2d(Point2(device_r, device_plate_y - device_r), device_r, 180, 90),
            *arc2d(Point2(device_plate_x - device_r, device_plate_y + device_r), device_r, 270, 360),
            *arc2d(Point2(device_plate_x + supply_r, device_plate_y + margin_y - supply_r), supply_r, 180, 90),
            *arc2d(Point2(device_plate_x + supply_case_x - supply_r, device_plate_y + margin_y - supply_r), supply_r, 90, 0),
            *arc2d(Point2(device_plate_x + supply_case_x - supply_r, - margin_y + supply_r), supply_r, 360, 270),
            *arc2d(Point2(device_plate_x + supply_r, - margin_y + supply_r), supply_r, 270, 180),
            *arc2d(Point2(device_plate_x - device_r, - device_r), device_r, 0, 90),
        ],
    ),
    linear_extrude(device_plate_z),
    color("#ff9800", 0.5),
)

bolt = combine(
    m3_bolt_clearance_hole(),
    rotate([0, 180, 0]),
    translate([0, 0, bolt_thread_z + bolt_head_z]),
)

# Create holes for mounting the network appliance.
solid -= combine(
    bolt,
    translate([padding, padding + hole_xy / 2, 0]),
)
solid -= combine(
    bolt,
    translate([padding + hole_xy / 2, padding + hole_xy, 0]),
)
solid -= combine(
    bolt,
    translate([padding + hole_xy, padding + hole_xy / 2, 0]),
)
solid -= combine(
    bolt,
    translate([padding + hole_xy / 2, padding, 0]),
)

# Create holes for mounting the power supply.
solid -= combine(
    bolt,
    translate([device_plate_x + wall / 2, device_plate_y + margin_y - wall / 2, 0]),
)
solid -= combine(
    bolt,
    translate([device_plate_x + supply_case_x - wall / 2, device_plate_y + margin_y - wall / 2, 0]),
)
solid -= combine(
    bolt,
    translate([device_plate_x + supply_case_x - wall / 2, - margin_y + wall / 2, 0]),
)
solid -= combine(
    bolt,
    translate([device_plate_x + wall / 2, - margin_y + wall / 2, 0]),
)

solid = combine(
    solid,
    translate([0, margin_y, 0]),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
