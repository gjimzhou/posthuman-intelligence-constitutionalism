#!/usr/bin/env python3
"""Compatibility entry point for paired HTML and DOCX exports."""
import subprocess
import sys
from pathlib import Path
subprocess.run([sys.executable, str(Path(__file__).with_name('build_all.py')), '--formats-only'], check=True)
