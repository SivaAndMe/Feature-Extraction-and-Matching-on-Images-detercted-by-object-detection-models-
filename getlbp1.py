from skimage import io,feature
import cv2
import numpy as np
import scipy
from scipy.misc import imread
import csv
import random
import os
import matplotlib.pyplot as plt

file = open('region1.csv','r')
csvreader = csv.reader(file)
row = next(csvreader)

# Extract feature for each image. This function is called in batch extractor function
def extract_features_LBP(image_path):
    image = io.imread(image_path, as_gray=True)
    #LBP_features can't be extracted in HSV color format . So using grey images

    # Crop image using co-ordinates from cvs file
    row = next(csvreader)
    pos = row[1]
    pos = pos[1:-1]
    pos = pos.split(',')
    # string->float->int as OpenCV accepts only integers
    pos = [int(float(p)) for p in pos]
    x,y,w,h=pos[0],pos[1],pos[2],pos[3]
    crop_img = image[x:x+w,y:y+h]

    try:
        numPoints=24
        radius=8
        # numpoints and radius can be changed
        lbp = feature.local_binary_pattern(crop_img,numPoints,radius,method="uniform")
        # other methods can be used such as var
    except cv2.error as e:
        print ('Error: ', e)
        return None
    return lbp

def batch_extractor_LBP(images_path):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    csvfile = open("lbp.csv","a")

    for f in files:
        print ('Extracting LBP_features from image %s' % f)
        # Get image name from absolute file path
        name = f.split('/')[-1].lower()

        result = extract_features_LBP(f)# A N*K matrix
        # Converting into a 2d array of shape (N,1) inorder to transpose it later
        result1d = np.ravel(result)[:,np.newaxis]
        #getting image name only
        nameprint = name[7:]

        # writing to csvfile
        np.savetxt(csvfile, result1d.T,fmt='%1.0f',header=nameprint)
        print("sucesssful")
