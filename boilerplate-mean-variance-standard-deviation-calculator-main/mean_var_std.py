import numpy as np

def calculate(list):
    # only works if we get exactly 9 numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # reshape into 3x3 grid
    arr = np.array(list).reshape(3, 3)

    # calculates in 3 ways: col-wise, row-wise, whole thing
    calculations = {
        'mean': [
            np.mean(arr, axis=0).tolist(),   # cols
            np.mean(arr, axis=1).tolist(),   # rows
            np.mean(arr).item()              # entire array
        ],
        'variance': [
            np.var(arr, axis=0).tolist(),
            np.var(arr, axis=1).tolist(),
            np.var(arr).item()
        ],
        'standard deviation': [
            np.std(arr, axis=0).tolist(),
            np.std(arr, axis=1).tolist(),
            np.std(arr).item()
        ],
        'max': [
            np.max(arr, axis=0).tolist(),
            np.max(arr, axis=1).tolist(),
            np.max(arr).item()
        ],
        'min': [
            np.min(arr, axis=0).tolist(),
            np.min(arr, axis=1).tolist(),
            np.min(arr).item()
        ],
        'sum': [
            np.sum(arr, axis=0).tolist(),
            np.sum(arr, axis=1).tolist(),
            np.sum(arr).item()
        ]
    }

    return calculations
