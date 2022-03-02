""" 
Unit and regression test for the measure module. 
"""

# Import package, test suite, and other packages as needed
import ising_model
import numpy as np


def test_hamiltonian():
    """Test that spinconfig function calculates what we expect."""

    ham = ising_model.Hamiltonian(-2, 1.1)

    expected_J = -2
    calculated_J = ham.J

    expected_u = 1.1
    calculated_u = ham.u

    expected_energy = -4.9
    calculated_energy = ham. energy([0, 1, 0, 1, 1])

    expected_average = (-1.894905381126034, -0.29386784002835087, 0.17850826588133842, 0.26682385808137565)
    calculated_average = ham.average(10, 4)

    assert expected_J == calculated_J
    assert expected_u == calculated_u
    assert expected_energy == calculated_energy
    assert expected_average == calculated_average
