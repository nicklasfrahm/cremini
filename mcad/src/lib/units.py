"""
Functions for common mechanical dimensions of a server rack.
"""


def rxxu(factor: float = 1) -> float:
    """
    The height of a single rack unit in a 10-inch or
    19-inch rack. Often also referred to as RU or U.
    """
    return 44.45 * factor


def rxxp(factor: float = 1) -> float:
    """
    The vertical screw pitch on the mounting rails of
    a 10-inch or 19-inch rack.
    """
    return 15.875 * factor


def rxxr(factor: float = 1) -> float:
    """
    The horizontal width of the mounting rail in a
    10-inch or 19-inch rack.
    """
    return 15.875 * factor


def r10i(factor: float = 1) -> float:
    """
    The inner spacing of the mounting rails in a 10-inch
    half rack and thus the maximum size of the appliance.
    """
    return 222.25 * factor


def r10s(factor: float = 1) -> float:
    """
    The horizontal screw spacing on the mounting rails
    of a 10-inch half rack.
    """
    return 236.525 * factor


def r10o(factor: float = 1) -> float:
    """
    The outer size of the mounting rails of a 10-inch
    half rack giving it its name.
    """
    return 254.0 * factor


def r19i(factor: float = 1) -> float:
    """
    The inner spacing of the mounting rails in a 19-inch
    full rack and thus the maximum size of the appliance.
    """
    return 450.85 * factor


def r19s(factor: float = 1) -> float:
    """
    The horizontal screw spacing on the mounting rails
    of a 19-inch full rack.
    """
    return 465.12 * factor


def r19o(factor: float = 1) -> float:
    """
    The outer size of the mounting rails of a 19-inch
    full rack giving it its name.
    """
    return 482.6 * factor


def inches(factor: float = 1) -> float:
    """
    A function to convert inches into millimeters.
    """
    return 25.4 * factor


def l19x(factor: float = 1) -> float:
    """
    The size of a Libre19 brick along the x-axis.
    """
    return factor * 73


def l19y(factor: float = 1) -> float:
    """
    The size of a Libre19 brick along the y-axis.
    """
    return factor * 215


def l19z(factor: float = 1) -> float:
    """
    The size of a Libre19 brick along the z-axis.
    """
    return factor * 42.5
