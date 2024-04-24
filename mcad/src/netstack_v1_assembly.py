"""
An test file to calibrate 3D-printing shrinkage.
"""
from solid import OpenSCADObject
from solid.objects import translate, cube, color
from lib.utils import build, combine
from lib.units import rxxu, rxxr, r19i

from netstack_v1_case_nanopir5s import obj as nanopir5s_case
from netstack_v1_case_nanopir5s import margin_base, case_x

solid = combine(
    nanopir5s_case(),
    translate([margin_base, 0, 0]),
)

solid += combine(
    nanopir5s_case(),
    translate([margin_base * 2 + case_x, 0, 0]),
)

solid += combine(
    nanopir5s_case(),
    translate([margin_base * 3 + case_x * 2, 0, 0]),
)

# Create a mock of the mounting rails.
rail = cube([rxxr(1), rxxr(1), rxxu(3)])
rails = combine(
    rail,
    translate([-rxxr(1), 10, -rxxu(1)]),
)

rails += combine(
    rail,
    translate([r19i(1), 10, -rxxu(1)]),
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
