import cv2
import csv
import numpy as np
import scipy
from scipy.misc import imread
import pickle
import random
import os
import matplotlib.pyplot as plt

file = open('region1.csv','r')
csvreader = csv.reader(file)
row = next(csvreader)

# Extract feature for each image. This function is called in batch extractor function
def extract_features_SURF(image_path, vector_size=32):#first-best 32 keypoints
    img = cv2.imread(image_path)
    image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # Extracting x,y,w,h from csv file
    row = next(csvreader)
    pos = row[1]
    pos = pos[1:-1]
    pos = pos.split(',')
    pos = [int(float(p)) for p in pos]
    x,y,w,h=pos[0],pos[1],pos[2],pos[3]
    # Crop image using co-ordinates from cvs file
    crop_img = image[x:x+w,y:y+h]

    try:

        alg = cv2.xfeatures2d.SURF_create()
        # Finding image keypoints
        kps = alg.detect(crop_img)
        # Number of keypoints is varies depend on image size and color pallet
        # Sorting them based on keypoint response value(bigger is better)
        kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
        # computing descriptors vector
        kps, dsc = alg.compute(crop_img, kps)
        # Flatten all of them in one big vector - our feature vector
        if(dsc is not None):
            dsc = dsc.flatten()
        # ndarray.flatten(order='C') .Return a copy of the array collapsed into one dimension.
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

def batch_extractor_SURF(images_path):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    csvfile = open("surf.csv","a")

    for f in files:
        print ('Extracting SURF_features from image %s' % f)
        # Get image name from absolute file path
        name = f.split('/')[-1].lower() # split by / and get the one after last split
        result = extract_features_SURF(f)
        print(f)
        nameprint = name[7:]
        result = result[:,np.newaxis]
        result_tra = result.T
        np.savetxt(csvfile, result_tra,fmt='%1.6f',delimiter=',',header=nameprint)
        print("sucesssful")
        # 2048 rows for each image
