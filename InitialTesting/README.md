
## Documentation of my journey :)

The `many_filters.py` script worked! I saw myself in the original camera and then 6 copies of myself with various built-in filters:

<img src="script-capture-1.png" alt="original image with six filtered copies" width="600"/>

However, it seems like the original video and each of the six filtered copies are mirrored from how I want them.

The video feed is from the point of view of the camera, but I'd rather it look more like a mirror image of myself. I bet OpenCV has a built-in mirroring function...

One google search later and I've added a `mirroring_video.py` script that works perfectly, and displays the following video feed:

<img src="script-capture-2.png" alt="original image next to mirrored image" width="600"/>

I combined the two scripts and now `many_filters.py` produces 7 video feeds which all match the movement I wanted.

In order to make certain changes to these video feeds, I'd like to see how the image is stored under the covers. I could probably look this up, but what's the fun in that?

I've made `bare_minimum.py` to display just a single frame from the video camera, and then spill out a bunch of information about that frame.

The image data is saved into ndarrays which have the same dimensions as the image. Their third dimension is the number of colors in the image. RGB has depth 3, B/W is just a 2D array.