# FPGA Openflow [![License](https://img.shields.io/badge/License-GPL--3.0-darkgreen?style=flat-square)](LICENSE)

A **Python** library, and CLI utilities, which solves **HDL-to-bitstream**
based on [FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software).

The library is basically a wrapper which employs
[hdl/containers](https://github.com/hdl/containers) to perform **synthesis**
(VHDL and/or Verilog), **implementation** and **bitstream** generation.
Some command-line utilities are provided, to be used as standalone tools.

Currently, it is based on `GHDL`, `Yosys`, `ghdl-yosys-plugin`, `nextpnr`,
`icestorm` and `prjtrellis`.

> **NOTE:** it started as part of [PyFPGA](https://github.com/PyFPGA/pyfpga)
> and will be used to solves the `openflow` **tool**.

## Installation

Openflow requires Python `>=3.6`. For now, it's only available as a git repository
hosted on GitHub. It can be installed with pip:

```
pip install 'git+https://github.com/PyFPGA/pyfpga#egg=pyfpga'
```

> On GNU/Linux, installing pip packages on the system requires `sudo`.
> Alternatively, use `--local` for installing PyFPGA in your HOME.

You can get a copy of the repository either through git clone or downloading a
tarball/zipfile:

```
git clone https://github.com/PyFPGA/openflow.git
cd openflow
```

Then, use pip from the root of the repo:

```
pip install -e .
```

> With `-e` (`--editable`) your application is installed into site-packages via
> a kind of symlink. That allows pulling changes through git or changing the
> branch, without the need to reinstall the package.
