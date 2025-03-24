from calculate import tong_chi_phi

import pytest


@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (5000, 200, "invalid input"), 
        (2000, 20, 10000000),  
        (30, 30, 300000),  
        (100, 20, 800000),  
        (1000, 2000, "invalid input"), 
        (1000, 200, 5500000),  
    ]
)

def test_tong_chi_phi(x, y, expected_output):
    result = tong_chi_phi(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()