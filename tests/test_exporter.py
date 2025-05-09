# Copyright (c) 2025 Antmicro <www.antmicro.com>
#
# SPDX-License-Identifier: Apache-2.0

import subprocess

from filecmp import cmp
from pathlib import Path
from peakrdl_cocotb.exporter import CocotbExporter
from systemrdl import RDLCompiler

proj_dir = Path(__file__).resolve().parent.parent
input_file = proj_dir / "example" / "axtmega_spi.rdl"
golden_file = proj_dir / "example" / "axtmega_spi.py"
output_file = proj_dir / "example" / "axtmega_spi_generated.py"

def remove_file(file: Path):
    if file.is_file():
        file.unlink()


def test_cli():
    remove_file(output_file)

    cmd = [
        "peakrdl",
        "cocotb",
        input_file,
        "-o",
        output_file
    ]
    peakrdl_cocotb = subprocess.run(cmd)
    assert not peakrdl_cocotb.returncode, "PeakRDL-Cocotb tool did not return 0"

    assert cmp(output_file, golden_file), "Generated file does not match golden output"


def test_exporter():
    remove_file(output_file)

    # Compile
    rdlc = RDLCompiler()
    rdlc.compile_file(input_file)
    root = rdlc.elaborate()

    # Export Cocotb dictionary
    exporter = CocotbExporter()
    exporter.export(root, path=str(output_file))
    assert cmp(output_file, golden_file), "Generated file does not match golden output"


if __name__ == "__main__":
    test_cli()
    test_exporter()
    remove_file(output_file)

    print("All tests finished successfully")
