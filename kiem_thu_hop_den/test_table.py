from calculate import tong_chi_phi

import pytest

# Test cases for decision table testing
@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (0, 2000, "invalid input"), 
        (4000, 50, "invalid input"),  
        (3500, 400, "invalid input"),  
        (30, 1200, "invalid input"),  
        (40, 80, 400000),  
        (50, 200, 550000),  
        (100, 1500, "invalid input"), 
        (150, 50, 1200000),
        (200, 200, 1760000),
        (500, 1200, "invalid input"),
        (1000, 50, 5000000),
        (2000, 200, 11000000),
    ]
)


def test_tong_chi_phi(x, y, expected_output):
    result = tong_chi_phi(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()