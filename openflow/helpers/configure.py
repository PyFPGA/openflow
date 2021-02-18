#!/usr/bin/env python3
#
# Copyright (C) 2021 Rodrigo A. Melo
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

"""
A CLI to get the full OCI command for the specified tool.
"""

import argparse

from openflow import __version__ as version
from openflow.configure import ConfigureTools


def main():
    """Solves the main functionality of this helper."""

    cfg = ConfigureTools()

    # Parsing the command-line.

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='v{}'.format(version)
    )

    parser.add_argument(
        'tool',
        metavar='TOOL',
        choices=cfg.get_tools(),
        help=', '.join(cfg.get_tools())
    )

    args = parser.parse_args()

    # Solving the functionality

    print(cfg.get_command(args.tool))


if __name__ == "__main__":
    main()
