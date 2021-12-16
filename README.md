
### Requirements:
This is the list of additional things I've had to install in order to get code working.
* NumPy
  * pip install numpy
* OpenCV
  * pip install opencv-python

### Background:
This is a repository where I'll learn to use OpenCV to various video processing things.

First I want to make sure that I can stream video from my small 720p camera into a python script, and display on screen.

Then I want to make small changes to that video and have see the changes in the displayed video.

My goal is to recognize the position of faces in the video, and put bucket hats on each head. From there, I'll try to recognize entire bodies and make larger changes, like clothing, etc.

Another goal is to do basic facial recognition to differentiate between each of my roommates.

It all begins with getting input video and then deciding how to handle it.

### 12/15
OpenCV works on my computer and communicates with my webcam.

I've displaying live video on my monitor, and oriented it how I want.

My initial attemps at changing the video in live time are wayyyy too slow. I need to use built-in OpenCV functions or switch to a different language.