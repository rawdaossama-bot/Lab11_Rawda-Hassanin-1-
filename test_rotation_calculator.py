"""
File: rotation_calculator.py
Author: Rawda Hassanin
Date: 11/9/2025
Description: Contains the function to normalize a rotation degree input 
             to a value between 0 and 360 degrees.
"""


import pytest
# Import the function from the main code file
from rotation_calculator import normalize_rotation_degrees

# --- Test Cases for Correct Numeric Output ---

# Use pytest.mark.parametrize for clean testing of multiple inputs/outputs
@pytest.mark.parametrize("input_degrees, expected_output", [
    # a. Input: 100 expectation return 100
    (100, 100),
    # b. Input: 460 expectation return 100
    (460, 100),
    # c. Input: 820 expectation return 100 
    # (820 = 2 * 360 + 100)
    (820, 100),
    # d. Input: -100 return 260
    # (-100 + 360 = 260)
    (-100, 260),
    # e. Input: -460 return 260
    # (-460 = -2 * 360 + 260)
    (-460, 260),
    # f. Input: -820 return 260
    # (-820 = -3 * 360 + 260)
    (-820, 260),
    # Additional checks for edge cases
    (0, 0),
    (360, 0),
    (359, 359),
])
def test_numeric_rotations(input_degrees, expected_output):
    """
    Tests various numeric inputs (positive, negative, and zero) 
    to ensure full rotations are correctly removed and normalized to [0, 360).
    """
    result = normalize_rotation_degrees(input_degrees)
    # Using '==' for assertion
    assert result == expected_output, (
        f"Input: {input_degrees}, Expected: {expected_output}, Got: {result}"
    )

# --- Test Case for Exception Handling ---

def test_non_numeric_input():
    """
    g. Input: non-numeric input Properly catch exception (TypeError)
    Tests that a TypeError is raised for non-numeric inputs.
    """
    # Use pytest.raises(ExceptionType) as a context manager
    with pytest.raises(TypeError) as excinfo:
        normalize_rotation_degrees("hello")  # Testing with a string
    
    # Optional: Verify the message of the exception
    assert "Input must be a numeric value" in str(excinfo.value)

    # Test with another non-numeric type
    with pytest.raises(TypeError):
        normalize_rotation_degrees([1, 2, 3]) # Testing with a list
