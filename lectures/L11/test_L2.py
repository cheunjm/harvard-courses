import pytest
import L2

class TestL2:

    def test_L2_result(self):
        assert L2.L2([3.0, 4.0], [1.0, 2.0]) == 8.54400374531753
    
    def test_L2_types(self):
        with pytest.raises(ValueError):
            L2.L2([1.0, -1.0], [1.0, 3.0, 5.0])
    
    def test_L2_noweights(self):
        assert L2.L2([3.0, 4.0]) == 5.0
