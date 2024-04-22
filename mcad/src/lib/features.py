"""
Shared features that can be reused across several parts.
"""
from os import getenv
from math import ceil, sin, cos, pi
from euclid3 import Point2
from solid import OpenSCADObject
from solid.objects import polygon, cube, cylinder
from solid.utils import linear_extrude, rotate, translate, up, forward, right
from .utils import combine
from .units import rxxu


def deg2rad(deg: float):
    """
    Converts degress to radians.
    """
    return pi * (deg / 180)


def arc2d(
    center=Point2(),
    radius=1,
    start=0,
    stop=90,
    segments=512,
):
    """
    Draws an arc of specified `radius` aroung the given `center` point
    from `start` to `end`, where both are angles given in degrees. The
    resolution of the arc can be adjusted via the segments parameter,
    which sets the number of points on a 360 degree full circle.
    """
    resolution = getenv("RESOLUTION")
    if resolution is not None:
        segments = int(resolution)

    start = deg2rad(start)
    stop = deg2rad(stop)
    span = stop - start

    steps = ceil(segments * abs(span) / (2 * pi))
    step = span / steps

    return [
        Point2(
            center.x + cos(start + step * i) * radius,
            center.y + sin(start + step * i) * radius,
        )
        for i in range(steps + 1)
    ]


def handle(length=50, width=5) -> OpenSCADObject:
    """
    Create a handle of the specified length and width.
    """
    return combine(
        polygon(
            [
                Point2(0, 0),
                Point2(width, 0),
                *arc2d(Point2(width * 2, -width * 2), width, 180, 270),
                *arc2d(Point2(length - width * 2, -width * 2), width, 270, 360),
                Point2(length - width, 0),
                Point2(length, 0),
                *arc2d(Point2(length - width * 2, -width * 2), width * 2, 360, 270),
                *arc2d(Point2(width * 2, -width * 2), width * 2, 270, 180),
            ],
        ),
        linear_extrude(width),
    )

def corner(height: int = 1):
    """
    Create a corner that allows to connect two parts via M3 screws.
    """
    # Mounting bracket overlap.
    mbo = 10
    # Mounting screw hole radius.
    msr = 2.5 / 2
    # Mounting screw hole depth.
    msd = 10

    # Create corner.
    c_x = mbo * 2
    c_y = mbo * 2
    c_z = rxxu(height)
    solid = combine(
        cube([c_x, c_y, c_z + 2], center=True),
        up(c_z / 2),
    )
    mso = -(c_y / 2 + msd)
    screw = combine(
        cylinder(r=msr, h=c_y + 2 * msd),
        rotate(-90, [1, 0, 0]),
    )
    for i in range(2):
        solid += combine(
            screw,
            translate([5, mso, 5 + i * c_z - i * 10]),
        )
    for i in range(2):
        solid += combine(
            screw,
            translate([-5, mso, 5 + i * c_z - i * 10]),
        )

    return solid


def corners(dim_x: float, dim_y: float, height: int = 1):
    """
    Create four corners along the specified rectangle that allow to connect parts via M3 screws.
    """
    corn = corner(height)

    solid = corn
    solid += combine(
        corn,
        forward(dim_y),
    )
    solid += combine(
        corn,
        forward(dim_y),
        right(dim_x),
    )
    solid += combine(
        corn,
        right(dim_x),
    )

    return solid
