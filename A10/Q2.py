import numpy as np
array3D = np.arange(24).reshape(2, 3, 4)
moved_axes = np.moveaxis(array3D, 0, -1)
print("\n 3D Array with Moved Axes:\n", moved_axes)
