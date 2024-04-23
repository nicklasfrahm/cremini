"""
An test file to calibrate 3D-printing shrinkage.
"""
from solid import OpenSCADObject
from solid.objects import translate
from lib.utils import build, combine
from lib.units import rxxu, rxxr, r19o

import netstack_v1_nanopir5s

solid = combine(
    netstack_v1_nanopir5s.obj(),
    translate([0, 0, 0]),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
