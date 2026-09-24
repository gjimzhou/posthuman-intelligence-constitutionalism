#!/usr/bin/env python3
"""Compatibility entry point; canonical implementation is build_all.py."""
import subprocess
import sys
from pathlib import Path
subprocess.run([sys.executable, str(Path(__file__).with_name('build_all.py')), '--tex-only'], check=True)
