#!/usr/bin/env python

# bring nested functions to top for API access
from .core.assembly import Assembly, merge
from .core.load import load_json
from .core.Parallel import cluster_info
import os as _os
import sys as _sys
import subprocess as _sps

# Dunders
__version__ = "0.9.7"
__author__ = "Deren Eaton & Isaac Overcast"

# CLI __main__ changes to 0
__interactive__ = 1

# get binaries from conda/bin or conda/env/bin
class _Bins:
    pass
bins = _Bins()
bins.muscle = _os.path.join(_sys.prefix, "bin", "muscle")
bins.samtools = _os.path.join(_sys.prefix, "bin", "samtools")
bins.bedtools = _os.path.join(_sys.prefix, "bin", "bedtools")
bins.vsearch = _os.path.join(_sys.prefix, "bin", "vsearch")
bins.bwa = _os.path.join(_sys.prefix, "bin", "bwa")

# check binaries
for binary, path in bins.__dict__.items():

    # check for conda version
    if not _os.path.exists(path):
        setattr(bins, binary, binary)

        # if not then check for binary in PATH (less reliable versioned...)
        if _sps.call(['which', binary]):
            raise ImportError("Missing requirement: {}".format(binary))

# if user installed with pip then the following may be missing:
# _other_deps = ["pysam", "mpi4py", ""]
try:
    import pysam
except ImportError:
    print("""
You must first install 'pysam' with either conda or pip, e.g.,: 

    conda install pysam -c bioconda

    or 

    pip install pysam
""")


