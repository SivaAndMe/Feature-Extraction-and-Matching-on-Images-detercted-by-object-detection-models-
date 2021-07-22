  <h3>FEATURE EXTRACTION using BRIEF,SURF,HISTOGRAM,LOCALLY BINARY PATTERNS</h3>

<h4>ABOUT FILES:</h4>
getcsvMAIN.py =>file calls all feature extraction files<br>
getbrief1.py => BRIEF FEATURES<br>
getsurf1.py => SURF FEATURES<br>
gethist1.py => HISTOGRAM FEATURES<br>
getlbp1.py => LOCALLY BINARY PATTERNS<br>
feature_matcher1.py => MATCH FEATURES AFTER THEY ARE EXTRACTED<br>

And CSV file which has the data of selected regions(bounding boxes) of images should be saved in the same directory as of above files.<br>



<h4>IMPORTANT NOTE:</h4>
->SURF(used in getsurf1.py) AND SIFT(used in getbrief1.py) are removed from OpenCV library in version 4.0 onwards(moved to OpenCV-contrib).<br> ->So version 3.4.2.16 should be used to run getcsvMAIN.py ,getsurf1 and getbrief1 files.<br>-> It's better to install OpenCV version - 3.4.2.16 after uninstalling present version.<br> -> To run using present version , one has to change 1-2 lines of code in getbrief1.py and getsurf1.py files.


<h4>HOW TO RUN ?</h4>
-> Change the image path in getcsvMAIN.py to a local image folder<br>
-> getcsvMAIN.py imports other functions from remaining files. So run it .<br>
-> CSV files with feature vectors will be saved in the same directory as that of getcsvMAIN.py file , after the feature extraction is completed.<br>
<h4>ISSUES :</h4>
-> When getcsvMAIN is run (and assuming there are n images) , All except BRIEF gives n feature vectors and BRIEF gives n-1 features(of first n-1 images) . To get n features for BRIEF too , uncomment the last two lines of code and run getbrief1.py

<h5>Changes in feature_matcher1.py</h5>
You can change num_of_best_matches, csvreader, csvwriter variables according to your need .



![SLIDES](/images/Slide6.JPG)
![SLIDES](/images/Slide7.JPG)
![Problem Statement](/images/Slide8.JPG)
![Problem Statement](/images/Slide9.JPG)
![Problem Statement](/images/Slide10.JPG)
![Problem Statement](/images/Slide11.JPG)
![Problem Statement](/images/Slide12.JPG)
![Problem Statement](/images/Slide13.JPG)
![Problem Statement](/images/Slide14.JPG)
