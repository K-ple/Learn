import pandas as pd 
import numpy as np
import random
import tensorflow as tf 
print(tf.__version__)

SEED = 12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)
print('시드고정:',SEED)

from sklearn import datasets 
housing = datasets.load_boston()
X_data = housing.data
Y_data = housing.target
print(X_data.shape, Y_data.shape)
