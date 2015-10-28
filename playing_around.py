__author__ = 'esievers'

#starting w. scripts posted on kaggle website to get a feel

import pandas as pd
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from collections2 import Counter

train = pd.read_json('./train.json')