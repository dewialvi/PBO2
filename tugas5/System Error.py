import numpy as np

# Create a large numpy array
arr = np.zeros((1000000, 1000000))

# Try to access an out-of-bounds index
print(arr[1000000, 1000000])
