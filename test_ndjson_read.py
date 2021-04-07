import numpy as np
from PIL import Image


data = np.load("full_numpy_bitmap_The Eiffel Tower.npy")

A = np.reshape(data[0], (28,28))
im = Image.fromarray(A)
im.show()

# for A in data:
#     A = np.reshape(A, (25,25))
#     im = Image.fromarray(A)
#     im.save("your_file.jpeg")


import ndjson