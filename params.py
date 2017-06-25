import os
from collections import OrderedDict

import numpy as np

# Nvida's camera format
img_h = 64
img_w = 64
img_c = 3

# Fix random seed for reproducibility
np.random.seed(42)

# Path
data_dir = os.path.abspath('./epochs')
out_dir = os.path.abspath('./output')
model_dir = os.path.abspath('./models')
