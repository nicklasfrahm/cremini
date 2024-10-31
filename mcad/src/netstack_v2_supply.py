"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, polygon
from solid.objects import color
from solid.utils import linear_extrude
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

# Configurable design parameters.
wall = 8
tolerance_xy = 0.3

# Dimension of the network appliance.
supply_x = 50.5
supply_y = 132.5
supply_z = 30.5
device_r = 2

# Dimensions of the case for the power supply.
supply_case_x = supply_x + 2 * wall + tolerance_xy
supply_case_y = supply_y + 2 * wall + tolerance_xy
supply_case_z = supply_z + wall + tolerance_xy

solid = combine(
    polygon(
        [
            *arc2d(Point2(device_r, device_r), device_r, 180, 270),
            *arc2d(Point2(supply_x - device_r,  device_r), device_r, 270, 360),
            *arc2d(Point2(supply_x - device_r, supply_y - device_r), device_r, 0, 90),
            *arc2d(Point2(device_r, supply_y - device_r), device_r, 90, 180),
        ],
    ),
    linear_extrude(supply_z),
    color("#333", 0.5),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
