"""A python package for analyzing Ising models."""

# Add imports here
from .functions import *

from .spinconfig import SpinConfig
from .hamiltonian import Hamiltonian


# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
