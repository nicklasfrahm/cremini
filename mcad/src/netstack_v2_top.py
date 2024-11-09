"""
A model of the Nanopi R5S with its enclosure.
"""
from solid import OpenSCADObject, polygon, linear_extrude, rotate, translate, cylinder
from solid.objects import color
from euclid3 import Point2
from lib.utils import build, combine
from lib.units import rxxr, rxxp
from lib.features import arc2d

from netstack_v2_device import wall, tolerance_xy, tolerance_z, rail_clearance, bottom_z
from netstack_v2_supply import supply_case_x, supply_case_y, supply_r, supply_case_z, supply_x, supply_y, supply_z, supply_slot_x, supply_slot_z
from m3_bolt import m3_bolt_tapping_hole, thread_z

m6_bolt_clearance_r = 6.5 / 2
overlap = 0.1

solid = combine(
    polygon(
        [
            *arc2d(Point2(supply_r, supply_r), supply_r, 270, 180),
            *arc2d(Point2(supply_r, supply_case_y - supply_r), supply_r, 180, 90),
            *arc2d(Point2(supply_case_x - supply_r, supply_case_y - supply_r), supply_r, 90, 0),
            *arc2d(Point2(supply_case_x + supply_r, wall + supply_r), supply_r, 180, 270),
            *arc2d(Point2(supply_case_x + rail_clearance - supply_r, wall - supply_r), supply_r, 90, 0),
            *arc2d(Point2(supply_case_x + rail_clearance + supply_r, wall / 2 + supply_r), supply_r, 180, 270),
            *arc2d(Point2(supply_case_x + rail_clearance + rxxr(1.5) - supply_r, wall / 2 - supply_r), supply_r, 90, 0),
            *arc2d(Point2(supply_case_x + rail_clearance + rxxr(1.5) - supply_r, supply_r), supply_r, 360, 270),
        ],
    ),
    linear_extrude(supply_case_z),
    color("#ff9800", 0.5),
)

# Create space for the power supply.
solid -= combine(
    polygon(
        [
            *arc2d(Point2(supply_r, supply_r), supply_r, 270, 180),
            *arc2d(Point2(supply_r, supply_y - supply_r + tolerance_xy), supply_r, 180, 90),
            *arc2d(Point2(supply_x - supply_r + tolerance_xy, supply_y - supply_r + tolerance_xy), supply_r, 90, 0),
            *arc2d(Point2(supply_x - supply_r + tolerance_xy, supply_r), supply_r, 360, 270),
        ],
    ),
    linear_extrude(supply_z + tolerance_z + overlap),
    translate([wall, wall, -overlap]),
)

solid -= combine(
    polygon(
        [
            Point2(0, 0),
            *arc2d(Point2(supply_r, supply_slot_z - supply_r + overlap), supply_r, 180, 90),
            *arc2d(Point2(supply_slot_x - supply_r, supply_slot_z - supply_r + overlap), supply_r, 90, 0),
            Point2(supply_slot_x, 0),
        ],
    ),
    linear_extrude(supply_case_y + 2 * overlap),
    rotate([90, 0, 0]),
    translate([wall, supply_case_y + overlap, -overlap]),
    color("#ff9800", 0.5),
)

# Create mounting holes for the power supply.
solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([wall / 2, wall / 2, thread_z]),
)

solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([supply_case_x - wall / 2, wall / 2, thread_z]),
)

solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([wall / 2, supply_case_y - wall / 2, thread_z]),
)

solid -= combine(
    m3_bolt_tapping_hole(),
    rotate([180, 0, 0]),
    translate([supply_case_x - wall / 2, supply_case_y - wall / 2, thread_z]),
)

# Create mounting holes for the rack rails.
solid -= combine(
    cylinder(d=m6_bolt_clearance_r*2, h=wall/2 + 2 * overlap),
    rotate([90, 0, 0]),
    translate([supply_case_x + rail_clearance + rxxr(1), wall / 2 + overlap, (supply_case_z - bottom_z) / 2 + rxxp(1)]),
)
solid -= combine(
    cylinder(d=m6_bolt_clearance_r*2, h=wall/2 + 2 * overlap),
    rotate([90, 0, 0]),
    translate([supply_case_x + rail_clearance + rxxr(1), wall / 2 + overlap, (supply_case_z - bottom_z) / 2]),
)
solid -= combine(
    cylinder(d=m6_bolt_clearance_r*2, h=wall/2 + 2 * overlap),
    rotate([90, 0, 0]),
    translate([supply_case_x + rail_clearance + rxxr(1), wall / 2 + overlap, (supply_case_z - bottom_z) / 2 - rxxp(1)]),
)

def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the file as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
