"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, polygon
from solid.objects import color
from solid.utils import linear_extrude
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

from netstack_v2_device import wall, tolerance_xy, tolerance_z, bottom_z

# Dimension of the power supply.
supply_x = 50.5
supply_y = 132.5
supply_z = 30.5
supply_r = 1

# Dimensions of the case for the power supply.
supply_case_x = supply_x + 2 * wall + tolerance_xy
supply_case_y = supply_y + 2 * wall + tolerance_xy
supply_case_z = 44 - bottom_z

# Dimensions of cable slot.
supply_slot_x = 28
supply_slot_z = 26

solid = combine(
    polygon(
        [
            *arc2d(Point2(supply_r, supply_r), supply_r, 180, 270),
            *arc2d(Point2(supply_x - supply_r,  supply_r), supply_r, 270, 360),
            *arc2d(Point2(supply_x - supply_r, supply_y - supply_r), supply_r, 0, 90),
            *arc2d(Point2(supply_r, supply_y - supply_r), supply_r, 90, 180),
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
