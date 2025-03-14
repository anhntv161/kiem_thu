from calculate import tong_chi_phi

import pytest


@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (3500, 2000, "invalid input"), 
        (30, 50, 300000),  
        (100, 80, 800000),  
        (1000, 500, 5500000),  
    ]
)

def test_tong_chi_phi(x, y, expected_output):
    result = tong_chi_phi(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()