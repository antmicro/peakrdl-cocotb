# PeakRDL-Cocotb

Copyright (c) 2025 [Antmicro](https://www.antmicro.com)

This package implements Python class-like object exporter for the PeakRDL toolchain.
The exporter provides a way to convert compiled SystemRDL input into class-like accessible Python object with defined registers hierarchy.

## Usage

PeakRDL project provides a standard CLI interface. It can be installed directly via pip:

```bash
pip install git+https://github.com/antmicro/PeakRDL-Cocotb.git
```

Then this package can be used with the following command:

```bash
peakrdl cocotb input_file.rdl -o reg_map.py
```
