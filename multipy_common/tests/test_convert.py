from multipy_common import serialize, deserialize
import numpy as np


def test_serialize():
    data = np.array([1, 2, 3])
    string = serialize(data)

    assert string == '[type=int64;1,2,3]'


def test_deserialize():
    string = '[type=float;3,2,1]'
    data = deserialize(string)

    assert data.dtype == np.float64
    assert np.all(data == np.array([3, 2, 1], dtype=float))
