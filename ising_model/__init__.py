"""A python package for analyzing Ising models."""

# Add imports here
from .functions import *
from .hamiltonian import Hamiltonian
from .spinconfig import SpinConfig

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
