"""
Unit and regression test for the ising_model package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import ising_model


def test1():
    assert(1 == 1)


def test_ising_model_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "ising_model" in sys.modules
