from multipy_common import get_data
import numpy as np


def test_get_data():
    assert np.all(get_data() == np.array([1, 2, 3, 4, 5]))
