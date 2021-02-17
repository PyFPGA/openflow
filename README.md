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
