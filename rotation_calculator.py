"""
File: rotation_calculator.py
Author: Rawda Hassanin
Date: 11/9/2025
Description: Contains the function to normalize a rotation degree input 
             to a value between 0 and 360 degrees.
"""


from typing import Union  

def normalize_rotation_degrees(degrees: Union[int, float]) -> Union[int, float]:
    """
    Adjusts a numeric input representing the degrees of a rotation to 
    remove unnecessary full rotations (360 degrees).

    The result is a value between 0 (inclusive) and 360 (exclusive).

    Args:
        degrees (int or float): The input rotation in degrees.

    Returns:
        int or float: The normalized rotation in degrees (0 <= result < 360).

    Raises:
        TypeError: If the input is not a number.
    """
    # 1. Input Validation: Check if the input is numeric
    if not isinstance(degrees, (int, float)):
        # Raise a TypeError for non-numeric input
        raise TypeError("Input must be a numeric value (int or float).")

    # 2. Modulo Operation: Remove full 360-degree rotations
    # The modulo operator (%) returns the remainder of a division.
    # For positive numbers: 460 % 360 = 100
    # For negative numbers: -460 % 360 = -100 (in Python)
    normalized = degrees % 360

    # 3. Adjust Negative Results: Convert results like -100 to 260
    # The modulo operator in Python can return a negative result when 
    # the dividend is negative. We want the result in the [0, 360) range.
    if normalized < 0:
        normalized += 360

    return normalized

if __name__ == '__main__':
    # Simple examples for demonstration (optional)
    print(f"100 degrees normalized: {normalize_rotation_degrees(100)}")    # Output: 100
    print(f"460 degrees normalized: {normalize_rotation_degrees(460)}")    # Output: 100
    print(f"-100 degrees normalized: {normalize_rotation_degrees(-100)}")  # Output: 260
    # The expected output 260 for -100 is equivalent to: -100 + 360 = 260
