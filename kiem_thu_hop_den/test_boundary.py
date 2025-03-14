
from calculate import tong_chi_phi
import pytest

# Test cases for boundary value testing
@pytest.mark.parametrize(
    "x, y, expected_output",
    [
        (1, 500, 11000),   
        (3260, 500, 17930000), 
        (2, 500, 22000),   
        (3259, 500, 17924500),  
        (0, 500, "invalid input"),  
        (3261, 500, "invalid input"),  
        (1630, 1, 8150000),   
        (1630, 1000, 8965000),  
        (1630, 2, 8150000),  
        (1630, 999, 8965000),  
        (1630, 0, "invalid input"),  
        (1630, 1001, "invalid input"),  
        (1630, 500, 8965000),  
    ]
)

def test_tong_chi_phi(x, y, expected_output):
    result = tong_chi_phi(x, y)
    print(f"Test case with x={x}, y={y}: expected {expected_output}, got {result}")
    assert result == expected_output

if __name__ == "__main__":
    pytest.main()