# Network stack 📡

# Version 1

This new iteration focuses on simplicity in terms of components and assembly. The goal is to provide a basic network stack that can be easily assembled and maintained. The following components are planned:

- 3x [NanoPi R5S][nanopi-r5s] as network routers and firewalls

![Network stack v1](./netstack_v1_assembly.png)

# Version 0

One part of the project is a network stack, which provides a top of rack L3 router, network switches and power. Below, you may find a list of all final components and a picture of the current state.

- [x] Rack mount chassis
  - [x] Appliance layout and size constraints
  - [x] Compatibility concept with 10-inch half-rack
  - [ ] Splitting into 3D-printable components
- [x] Power supply
  - [x] Compatibile with [YOUMILE AC-DC 12V6A][amazon-psu-youmile] or [ANGEEK AC-DC 12V6A][amazon-psu-angeek]
  - [ ] Case for **DIY AC-DC 12V5A** power supply
  - [ ] Case for **X115-Y65-Z40** power supplies
- [ ] Network switches
  - [ ] Compatibility with TP-LINK SG108E and NETGEAR GS308E
  - [ ] Case for any 8-port switch
- [ ] Chassis management
  - [ ] Schematic for WT32-ETH01
  - [ ] [Veroboard][wikipedia-veroboard] layout
  - [ ] Firmware for WT32-ETH01
  - [ ] Case for chassis management unit
- [x] Router and firewall
  - [x] Traffic management via [nftables][wiki-nftables]
  - [ ] Case for [Seeed compute module router][seeed-cm4router]

![Network stack CAD preview][img-netstack]

[img-netstack]: ./netstack_v0_assembly.png
[amazon-psu-youmile]: https://www.amazon.de/dp/B07TZY73H6
[amazon-psu-angeek]: https://www.amazon.de/dp/B07KPK525R
[wikipedia-veroboard]: https://en.wikipedia.org/wiki/Veroboard
[wiki-nftables]: https://wiki.nftables.org/wiki-nftables/index.php/What_is_nftables%3F
[seeed-cm4router]: https://www.seeedstudio.com/Rapberry-Pi-CM4-Dual-GbE-Carrier-Board-p-4874.html
[nanopi-r5s]: https://www.friendlyelec.com/index.php?route=product/product&product_id=287
