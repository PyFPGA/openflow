"""Example about default values."""

from openflow.configure import ConfigureTools

cfg = ConfigureTools()

for tool in cfg.get_tools():
    print(cfg.get_command(tool))
