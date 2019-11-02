import cv2
import numpy as np
import scipy
from scipy.misc import imread
import pickle
import random
import os
import matplotlib.pyplot as plt
# import io,features

from getsurf1 import batch_extractor_SURF
from getbrief1 import batch_extractor_BRIEF
from getlbp1 import batch_extractor_LBP
from gethist1 import batch_extractor_HIST

image_path = 'C:/Users/sivas/Desktop/ComputerVision/images'

batch_extractor_HIST(image_path)
batch_extractor_LBP(image_path)
batch_extractor_SURF(image_path)
batch_extractor_BRIEF(image_path)
