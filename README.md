# Ant-Detection
Detecting ants using Python's Open-CV library and a self trained Haar feature-based cascade classifier.

I used around 42 vanilla positive images changed into around 9000 with slight angle deviations and around 800 negative images.

A few false positives and some undetected because my positive/negative images set wasn't large enough. Could only train the classifier for 7 stages.
Result: https://i.imgur.com/MlSE4Mh.png 

How to run the script:
  1. Clone the entire repository
  2. You need to have OpenCV to run it. If you don't, "git clone https://github.com/opencv/opencv.git" into the repository.
  2. i. If you're using a Python IDE, then just open the script and run it.                                                     

     ii. If you don't have an IDE, open your terminal and navigate to the directory (~/Ant-Detection) and type out:
     "python script.py". 
     If you get an error similar to "no module cv2", then try "python3 script.py"
  3. To exit, press any key.
  
     
