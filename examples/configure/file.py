"""Example about to specify a file."""

from openflow.configure import ConfigureTools

cfg = ConfigureTools('file.yml')

for tool in cfg.get_tools():
    print(cfg.get_command(tool))
