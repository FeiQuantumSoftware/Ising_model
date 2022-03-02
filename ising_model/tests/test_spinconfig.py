""" 
Unit and regression test for the measure module. 
"""

# Import package, test suite, and other packages as needed
import ising_model
import numpy as np


def test_spinconfig():
    """Test that spinconfig function calculates what we expect."""

    test_spin = ising_model.SpinConfig(8)

    expected_N = 8
    calculated_N = test_spin.N

    expected_iMax = 256
    calculated_iMax = test_spin.iMax

    expected_input_decimal = [0, 0, 0, 0, 1, 0, 1, 0]
    calculated_input_decimal = test_spin.input_decimal(10)

    expected_magnetization = -4
    calculated_magnetization = test_spin.magnetization()

    # translate '+' '-' intro list
    test_spin2 = ising_model.SpinConfig()
    expected_input_p_m = [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1]
    calculated_input_p_m = test_spin2.input_p_m("++-+---+--+")

    assert expected_N == calculated_N
    assert expected_iMax == calculated_iMax
    assert expected_input_decimal == calculated_input_decimal
    assert expected_input_p_m == calculated_input_p_m
    assert expected_magnetization == calculated_magnetization
