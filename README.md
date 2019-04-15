# Ant-Detection
Detecting ants using Python's Open-CV library and a self trained Haar feature-based cascade classifier.

I used 42 vanilla positive images which I then transformed into 9000+ with slight angle deviations and around 800 negative images.

Trained for 7 stages. Quite a few false positives because my positive/negative image set wasn't large enough.

Result:

![https://i.imgur.com/MlSE4Mh.png](https://i.imgur.com/MlSE4Mh.png)

### Instructions
  1. Clone the entire repository
  2. You need to have OpenCV to run it. If you don't, "git clone https://github.com/opencv/opencv.git" into the repository.
  2. i. If you're using a Python IDE, then just open the script and run it.                                                     

     ii. If you don't have an IDE, open your terminal and navigate to the directory (~/Ant-Detection) and type out:
     `python script.py`. 
     If you get an error similar to `no module cv2`, then try `python3 script.py`

  3. To exit, press any key.
  
If you'd like to use your own image:         
   
   Download and place your image in the root directory of the repo (~/Ant-Detection/) with a name say, img.jpg
    
   Open script.py with any text editor and replace sample.jpeg in img = cv2.imread('sample.jpeg') with what you've named your      image, in this case, 'img.jpg'. Be sure to include the quotes!
     
