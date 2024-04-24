"""
An test file to calibrate 3D-printing shrinkage.
"""
from solid import OpenSCADObject
from solid.objects import translate
from lib.utils import build, combine
from lib.units import rxxu, rxxr, r19o

from netstack_v1_case_nanopir5s import obj as nanopir5s_case

solid = combine(
    nanopir5s_case(),
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
