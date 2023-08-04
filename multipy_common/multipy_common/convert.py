import numpy as np

DTYPES = {
    'int': int,
    'float': float,
    'int32': np.int32,
    'int64': np.int64,
    'float32': np.float32,
    'float64': np.float64,
}


def serialize(data: np.ndarray) -> str:
    if len(data.shape) != 1:
        raise ValueError("Data must be 1D array, i.e. have shape (n, )")

    string = f"[type={data.dtype};"
    for i in range(len(data)):
        string += str(data[i]) + ","

    string = string[:-1] + ']'

    return string


def deserialize(string: str) -> np.ndarray:
    if string[0] != "[" or string[-1] != "]":
        raise ValueError("Data must be enclosed in square brackets")

    if string[1:6] != "type=":
        raise ValueError("Data must have type specified")

    # dtype until first semicolon
    dtype, string = string[6:-1].split(";", 2)
    if dtype not in DTYPES.keys():
        raise ValueError("Data type must be one of " +
                         ', '.join(DTYPES.keys()))

    dtype = DTYPES[dtype]

    data = string.split(",")
    data = [dtype(i) for i in data]

    return np.array(data)
