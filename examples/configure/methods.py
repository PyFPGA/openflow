"""Example about to use the different methods."""

from openflow.configure import ConfigureTools

cfg = ConfigureTools()

print('* Defaults for GHDL:')
print(cfg.get_command('ghdl'))

print('* Setting a different engine:')
cfg.set_engine('podman')
print(cfg.get_command('ghdl'))

print('* Setting different volumes:')
cfg.set_volumes(['v1:v1', 'v2:v2'])
print(cfg.get_command('ghdl'))

print('* Setting a different work:')
cfg.set_work('/tmp')
print(cfg.get_command('ghdl'))

print('* Setting a global options:')
cfg.set_global_options('--global option')
print(cfg.get_command('ghdl'))

print('* Setting a new container:')
cfg.set_container('ghdl', 'alt-ghdl-container')
print(cfg.get_command('ghdl'))

print('* Setting a new tool name:')
cfg.set_name('ghdl', 'alt-ghdl-name')
print(cfg.get_command('ghdl'))

print('* Setting a local options:')
cfg.set_local_options('ghdl', '--local option')
print(cfg.get_command('ghdl'))
