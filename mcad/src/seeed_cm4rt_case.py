"""
A case for the Seeed Compute Module 4 router board, including a 40x40x10mm fan.
"""
from solid import OpenSCADObject, cube, translate
from lib.utils import build, combine
from lib.units import l19x, l19y, l19z

# TODO: Set up tolerances for 3D printing.

# Define body solid.
X = l19x(2)
Y = l19y(1)
Z = l19z(1)
solid = cube([X, Y, Z])

# Create cutout based on PCB dimensions.
PCB_X = 75.8
PCB_Y = 64.95
PCB_MV_X = 3
PCB_MV_Y = 3
PCB_MV_Z = 6
solid -= combine(
    cube([PCB_X, PCB_Y, Z + 2]),
    translate([PCB_MV_X, PCB_MV_Y, -1]),
)

# Create supports for PCB.
PCB_SUP_X = 60
PCB_SUP_Y = 3
solid += combine(
    cube([PCB_SUP_X, PCB_SUP_Y, PCB_MV_Z]),
    translate([PCB_MV_X + PCB_X - PCB_SUP_X, PCB_MV_Y, 0]),
)
solid += combine(
    cube([PCB_SUP_X, PCB_SUP_Y, PCB_MV_Z]),
    translate([PCB_MV_X + PCB_X - PCB_SUP_X, PCB_MV_Y + PCB_Y - PCB_SUP_Y, 0]),
)

# Create opening for USB A ports.
USBA_X = 14.85
USBA_Z = 15.45
USBA_MV_X = 67.5 - USBA_X / 2
USBA_MV_Z = 2.45
solid -= combine(
    cube([USBA_X, PCB_MV_Y + 2, USBA_Z]),
    translate([PCB_MV_X + USBA_MV_X, -1, PCB_MV_Z + USBA_MV_Z]),
)

# Create opening for Ethernet ports.
ETH_X = 32.2
ETH_Z = 13.90
ETH_MV_X = 39.5 - ETH_X / 2
ETH_MV_Z = 2.1
solid -= combine(
    cube([ETH_X, PCB_MV_Y + 2, ETH_Z]),
    translate([PCB_MV_X + ETH_MV_X, -1, PCB_MV_Z + ETH_MV_Z]),
)

# Create opening for USB C port.
USBC_X = 3.25
USBC_Z = 8.95
USBC_MV_X = 18 - USBC_X / 2
USBC_MV_Z = 1.6
solid -= combine(
    cube([USBC_X, PCB_MV_Y + 2, USBC_Z]),
    translate([PCB_MV_X + USBC_MV_X, -1, PCB_MV_Z + USBC_MV_Z]),
)

# Create opening for HDMI port.
HDMI_X = 6.55
HDMI_Z = 2.95
HDMI_MV_X = 7 - HDMI_X / 2
HDMI_MV_Z = 1.6
solid -= combine(
    cube([HDMI_X, PCB_MV_Y + 2, HDMI_Z]),
    translate([PCB_MV_X + HDMI_MV_X, -1, PCB_MV_Z + HDMI_MV_Z]),
)

# Create opening for SD card slot.
SD_X = 14.35
SD_Z = 2.0
SD_MV_X = 8 - SD_X / 2
SD_MV_Z = -SD_Z
solid -= combine(
    cube([SD_X, PCB_MV_Y + 2, SD_Z]),
    translate([PCB_MV_X + SD_MV_X, -1, PCB_MV_Z + SD_MV_Z]),
)

# Create space for UART cable.

# TODO: Create cutout for the UART connector.
# TODO: Create air intake.
# TODO: Create rear exhaust.


def obj() -> OpenSCADObject:
    """
    Retrieve part object when importing it into assemblies or similar.
    """
    return solid


# Boilerplate code to export the part as `.scad` file if invoked as a script.
if __name__ == "__main__":
    build(obj(), __file__)
