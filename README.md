# Ant-Detection
Detecting ants using Python's Open-CV library and a self trained Haar feature-based cascade classifier.

I used around 42 vanilla positive images changed into around 9000 using opencv_createsamples with slight angle deviations and around 800 negative images. Trained the classifier for 7 stages.

Result: https://i.imgur.com/MlSE4Mh.png
A few false positives and some weren't detected because my positive/negative images set wasn't large enough. 
