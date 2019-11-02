import cv2
import numpy as np
import scipy
from scipy.misc import imread
import pickle
import random
import os
import matplotlib.pyplot as plt
import csv


file = open('region1.csv','r')
csvreader = csv.reader(file)
row = next(csvreader)

def extract_features_BRIEF(image_path, vector_size=32):#first-best 32 keypoints and each disc size is 64
    img = cv2.imread(image_path)
    image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #HSV DONT WORK for BRIEF algorithm
    row = next(csvreader)
    pos = row[1]
    pos = pos[1:-1]
    pos = pos.split(',')
    pos = [int(float(p)) for p in pos]
    x,y,w,h=pos[0],pos[1],pos[2],pos[3]
    crop_img = image[x:x+w,y:y+h]

    try:

        n_kp = 120 # Number of KeyPoints
        # BRIEF can't detect keypoints SO use SIFT for detecting keypoints
        sift = cv2.xfeatures2d.SIFT_create()

        # Initiate BRIEF extractor
        brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
        kps = sift.detect(crop_img,None)
        # compute the descriptors with BRIEF
        kps, dsc = brief.compute(crop_img, kps)
        # Getting first 32 of them.
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        # Flatten all of them in one big vector - our feature vector
        if(dsc is not None):
            dsc = dsc.flatten()
        # Making descriptor of same size
        # Descriptor vector size is 64
        needed_size = (vector_size * 64)
        if(dsc is not None):
            if dsc.size < needed_size:
            # if we have less the 32 descriptors then just adding zeros at the
            # end of our feature vector
                dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
            dsc = dsc[:2048]
    except cv2.error as e:
        print ('Error: ', e)
        return None

    return dsc

def batch_extractor_BRIEF(images_path):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    csvfile = open("brief.csv","a")

    for f in files:
        print ('Extracting BRIEF_features from image %s' % f)
        # Get image name from absolute file path
        name = f.split('/')[-1].lower()
        result = extract_features_BRIEF(f)
        # Converting into a 2d array of shape (N,1) inorder to transpose it later

        result1d = np.ravel(result)[:,np.newaxis]
        nameprint = name[7:]# slicing to get image name only
        np.savetxt(csvfile,result1d.T,fmt='%1.0f',delimiter=',',header=nameprint)# THE NUMBERS SEEMS FAR APART 1-13453 SO 2 DIGIT PRECISION
        print("sucesssful")

# image_path = 'C:/Users/sivas/Desktop/ComputerVision/images'
# batch_extractor_BRIEF(image_path)
