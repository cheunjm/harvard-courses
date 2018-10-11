
import pytest
import norm

def test_norm_result():
    assert norm.L2([3,4]) == 5.0
    
def test_norm_types():
    with pytest.raises(TypeError):
        norm.L2(3)
def test_norm_dimension_mismatch():
    with pytest.raises(ValueError):
        norm.L2([3,4], [2])