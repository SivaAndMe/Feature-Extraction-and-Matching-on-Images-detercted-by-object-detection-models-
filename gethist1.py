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
def extract_features_HIST(image_path):
    image = imread(image_path, mode="HSV")

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
        hist = cv2.calcHist([image],[0,1],None,[45,64],[0,180,0,256])# 45=180/4 and 64 = 256/4 TOTAL=2346 FINE!!
    except cv2.error as e:
        print ('Error: ', e)
        return None
    return hist


def batch_extractor_HIST(images_path):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    csvfile = open("hist.csv","a")

    for f in files:
        print ('Extracting HIST_features from image %s' % f)
        # Get image name from absolute file path

        name = f.split('/')[-1].lower()
        result = extract_features_HIST(f)
        # Converting into a 2d array of shape (N,1) inorder to transpose it later
        result1d = np.ravel(result)[:,np.newaxis]
        #getting image name only
        nameprint = name[7:]
        # writing to csvfile
        np.savetxt(csvfile, result1d.T,fmt='%1.2f',header=nameprint)# THE NUMBERS SEEMS FAR APART 1-13453 SO 2 DIGIT PRECISION
        csvfile.write("\n")
        print("sucesssful")
