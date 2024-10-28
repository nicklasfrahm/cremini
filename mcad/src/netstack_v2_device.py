"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, polygon
from solid.objects import color
from solid.utils import linear_extrude
from euclid3 import Point2
from lib.utils import build, combine
from lib.features import arc2d

# Dimension of the network appliance.
device_x = 141
device_y = 131
device_z = 40
device_r = 8

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

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
