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

"""openflow.configure

A Class to configure the OCI engine, the containers and the name of the
underlying FOSS tools.
"""


import os
from yaml import safe_load, dump


class ConfigureTools:
    """Configure Tools."""

    def __init__(self, filename='.openflow.yml'):
        """Class constructor."""
        userfile = os.getenv('OPENFLOW_FILE')
        homefile = os.path.join(os.path.expanduser('~'), filename)
        projfile = os.path.join(os.path.dirname(__file__), 'configure.yml')
        if userfile is not None and os.path.exists(userfile):
            filepath = userfile
        elif os.path.exists(filename):
            filepath = filename
        elif os.path.exists(homefile):
            filepath = homefile
        else:
            filepath = projfile
        self.configs = {}
        with open(filepath, 'r') as file:
            self.configs = safe_load(file)

    def get_command(self, tool):
        """Get the command-line needed to run a tool."""
        engine = self.configs['engine']['name']
        name = self.configs['tools'][tool]['name']
        if engine is not None and os.getenv('OPENFLOW_OFF') is None:
            oci = [
              engine,
              'run --rm',
              '-v ' + (' -v ').join(self.configs['engine']['volumes']),
              '-w ' + self.configs['engine']['work'],
              self.configs['engine'].get('options', None),
              self.configs['tools'][tool].get('options', None),
              self.configs['tools'][tool]['container'],
              name
            ]
            return ' '.join(list(filter(None, oci)))
        return name

    def get_tools(self):
        """Returns the list of configured tools."""
        return sorted(list(self.configs['tools'].keys()))

    def dump(self):
        """Dumps the configuration in YAML format (debug purpouses)."""
        return dump(self.configs)

    def set_engine(self, engine):
        """Set the OCI engine."""
        self.configs['engine']['name'] = engine

    def unset_engine(self):
        """Unset the OCI engine. """
        self.configs['engine']['name'] = None

    def set_volumes(self, volumes):
        """Set the volumes of the OCI engine."""
        self.configs['engine']['volumes'] = volumes

    def set_work(self, work):
        """Set the working directory inside the container."""
        self.configs['engine']['work'] = work

    def set_global_options(self, options):
        """Set options shared by all the containers."""
        self.configs['engine']['options'] = options

    def set_container(self, tool, container):
        """Set the container of the specified tool."""
        self.configs['tools'][tool]['container'] = container

    def set_name(self, tool, name):
        """Set the name of the specified tool."""
        self.configs['tools'][tool]['name'] = name

    def set_local_options(self, tool, options):
        """Set options for a particular container."""
        self.configs['tools'][tool]['options'] = options
