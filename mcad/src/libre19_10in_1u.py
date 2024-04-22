"""
A 1U Libre19 chassis that is compatible with 10-inch network shelves.
"""
from solid import OpenSCADObject, cube, translate, cylinder, rotate
from lib.utils import build, combine
from lib.units import inches, r10i, r10o, r10s, rxxu

# Sheet metal thickness.
T = 0.8

# Define interior dimensions.
IX = 72 * 3
IY = 150
IZ = 40

# Define bounding box.
X = IX + 2 * T
Z = IZ + T * 2

# Create front mounting tabs.
solid = combine(
    cube([r10o(1), T, Z]),
    translate([(X - r10o(1)) / 2, 0, 0]),
)

# Create shell.
solid += cube([IX + T * 2, IY, Z])
solid -= combine(
    cube([IX, IY + 2, IZ]),
    translate([T, -1, T]),
)

# TODO: Create alignment tabs.

# Align chassis to screw holes.
solid = combine(
    solid,
    translate([(r10o(1) - X) / 2, 0, (rxxu(1) - Z) / 2]),
)

# Create mounting screw holes.
SD = inches(0.125)
screw = combine(
    cylinder(SD, 3),
    rotate([-90, 0, 0]),
    translate([(r10o(1) - r10s(1)) / 2, -1, inches(0.25)]),
)
screws = screw
screws += combine(
    screw,
    translate([0, 0, inches(0.625)]),
)
screws += combine(
    screw,
    translate([0, 0, inches(1.25)]),
)
screws += combine(
    screws,
    translate([r10s(1), 0, 0]),
)
solid -= screws


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
