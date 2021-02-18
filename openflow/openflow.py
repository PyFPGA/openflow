#
# Copyright (C) 2020-2021 Rodrigo A. Melo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""openflow.openflow

A Python Package which solves HDL-to-bitstream based on FOSS.
"""


class Openflow:
    """Class which solves HDL-to-bitstream based on FOSS."""

    def __init__(self, name='openflow', part='hx8k-ct256'):
        """Class constructor."""
        self.name = name
        self.part = get_part(part)
        self.set_oci()
        self.set_tools()

    def set_oci(self):
        """Set the OCI engine."""
        self.oci = {
            'engine': 'docker',
            'volumes': ['$HOME:$HOME'],
            'work': '$PWD',
            'containers': {
                'ghdl': 'hdlc/ghdl:yosys',
                'yosys': 'hdlc/ghdl:yosys',
                'nextpnr-ice40': 'hdlc/nextpnr:ice40',
                'icetime': 'hdlc/icestorm',
                'icepack': 'hdlc/icestorm',
                'iceprog': 'hdlc/icestorm',
                'nextpnr-ecp5': 'hdlc/nextpnr:ecp5',
                'ecppack': 'hdlc/prjtrellis',
                'openocd': 'hdlc/prog'
            },
            'tools': {
                'ghdl': 'ghdl',
                'yosys': 'yosys',
                'nextpnr-ice40': 'nextpnr-ice40',
                'icetime': 'icetime',
                'icepack': 'icepack',
                'iceprog': 'iceprog',
                'nextpnr-ecp5': 'nextpnr-ecp5',
                'ecppack': 'ecppack',
                'openocd': 'openocd'
            }
        }

    def set_tools(self):
        """Set the underlying tools."""
        # Check if oci['engine'] is available
        engine = self.oci['engine']
        volumes = '-v ' + ('-v ').join(self.oci['volumes'])
        work = '-w ' + self.oci['work']
        command = '{} run --rm {} {}'.format(engine, volumes, work)
        self.tools = {}
        for tool in self.oci['tools']:
            self.tools[tool] = '{} {} {}'.format(
                command, self.oci['containers'][tool], self.oci['tools'][tool]
            )

    # pylint: disable=too-many-arguments
    def synthesis(
            self, top,
            vhdl=None, verilog=None, system_verilog=None,
            arch=None, defines=None, params=None, paths=None):
        """Performs synthesis."""
        print(self.name)
        print(self.part)
        print(top)
        print(vhdl)
        print(verilog)
        print(system_verilog)
        print(arch)
        print(defines)
        print(params)
        print(paths)

    def implementation(self, constraint=None):
        """Performs implementation."""
        print(self.name)
        print(self.part)
        print(constraint)

    def bitstream(self):
        """Performs bitstream generation."""
        print(self.name)
        print(self.part)


def get_part(part):
    """Get info about the FPGA part.

    :param part: the FPGA part as specified by the tool
    :returns: a dictionary with the keys name, family, device and package
    """
    name = part.lower()
    # Looking for the family
    family = None
    families = [
        # From <YOSYS>/techlibs/xilinx/synth_xilinx.cc
        'xcup', 'xcu', 'xc7', 'xc6s', 'xc6v', 'xc5v', 'xc4v', 'xc3sda',
        'xc3sa', 'xc3se', 'xc3s', 'xc2vp', 'xc2v', 'xcve', 'xcv'
    ]
    for item in families:
        if name.startswith(item):
            family = item
    families = [
        # From <nextpnr>/ice40/main.cc
        'lp384', 'lp1k', 'lp4k', 'lp8k', 'hx1k', 'hx4k', 'hx8k',
        'up3k', 'up5k', 'u1k', 'u2k', 'u4k'
    ]
    if name.startswith(tuple(families)):
        family = 'ice40'
    families = [
        # From <nextpnr>/ecp5/main.cc
        '12k', '25k', '45k', '85k', 'um-25k', 'um-45k', 'um-85k',
        'um5g-25k', 'um5g-45k', 'um5g-85k'
    ]
    if name.startswith(tuple(families)):
        family = 'ecp5'
    # Looking for the device and package
    device = None
    package = None
    aux = name.split('-')
    if len(aux) == 2:
        device = aux[0]
        package = aux[1]
    elif len(aux) == 3:
        device = '{}-{}'.format(aux[0], aux[1])
        package = aux[2]
    else:
        raise ValueError('Part must be DEVICE-PACKAGE')
    if family == 'ice40' and device.endswith('4k'):
        # See http://www.clifford.at/icestorm/
        device = device.replace('4', '8')
        package += ":4k"
    # Finish
    return {
        'name': name, 'family': family, 'device': device, 'package': package
    }
