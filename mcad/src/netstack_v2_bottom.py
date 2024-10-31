"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, polygon, translate
from solid.objects import color
from solid.utils import linear_extrude
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

from m3_bolt import m3_bolt_clearance_hole

# Configurable design parameters.
tolerance_xy = 0.3
padding = 5
wall = 8
device_r = 8
supply_r = 1 # Change to 0.5
cable_slot = 15

# Dimensions of the network appliance mounting holes.
hole_xy = 70
hole_margin_x = 33

# Dimensions of the mounting plate for the network appliance.
device_plate_x = padding + hole_xy + hole_margin_x + cable_slot
device_plate_y = hole_xy + 2 * padding
device_plate_z = 4

# Dimensions of the case for the power supply.
supply_x = 50.5 + 2 * wall + tolerance_xy
supply_y = 132.5 + 2 * wall + tolerance_xy
supply_z = 30.5 + wall + tolerance_xy

margin_y = supply_y - device_plate_y

solid = combine(
    polygon(
        [
            *arc2d(Point2(device_r, device_r), device_r, 270, 180),
            *arc2d(Point2(device_r, device_plate_y - device_r), device_r, 180, 90),
            *arc2d(Point2(device_plate_x - device_r, device_plate_y + device_r), device_r, 270, 360),
            *arc2d(Point2(device_plate_x + supply_r, device_plate_y + margin_y - supply_r), supply_r, 180, 90),
            *arc2d(Point2(device_plate_x + supply_x - supply_r, device_plate_y + margin_y - supply_r), supply_r, 90, 0),
            *arc2d(Point2(device_plate_x + supply_x - supply_r, - margin_y + supply_r), supply_r, 360, 270),
            *arc2d(Point2(device_plate_x + supply_r, - margin_y + supply_r), supply_r, 270, 180),
            *arc2d(Point2(device_plate_x - device_r, - device_r), device_r, 0, 90),
        ],
    ),
    linear_extrude(device_plate_z),
    color("#333", 0.5),
)

# Create holes for mounting the network appliance.
solid -= combine(
    m3_bolt_clearance_hole(),
    translate([padding, padding + hole_xy / 2, 0]),
)
solid -= combine(
    m3_bolt_clearance_hole(),
    translate([padding + hole_xy / 2, padding + hole_xy, 0]),
)
solid -= combine(
    m3_bolt_clearance_hole(),
    translate([padding + hole_xy, padding + hole_xy / 2, 0]),
)
solid -= combine(
    m3_bolt_clearance_hole(),
    translate([padding + hole_xy / 2, padding, 0]),
)

# Create holes for mounting the power supply.
solid -= combine(
    m3_bolt_clearance_hole(),
    translate([device_plate_x + wall / 2, device_plate_y + margin_y - wall / 2, 0]),
)
solid -= combine(
    m3_bolt_clearance_hole(),
    translate([device_plate_x + supply_x - wall / 2, device_plate_y + margin_y - wall / 2, 0]),
)
solid -= combine(
    m3_bolt_clearance_hole(),
    translate([device_plate_x + supply_x - wall / 2, - margin_y + wall / 2, 0]),
)
solid -= combine(
    m3_bolt_clearance_hole(),
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
