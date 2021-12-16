
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

First I'll start by boosting the red component of each pixel. I've used the code `frame[ii, jj, 0] = 255` to set the first component of every pixel to 255.

For some reason, this made blue become the dominant color in the image:

<img src="script-capture-3.png" alt="overwhelming blue when it's supposed to be red" width="600"/>

Maybe the components are in reverse order for some reason? Instead I'll try `frame[ii, jj, 2] = 255` to hopefully adjust the red component.

Okay, that fixed it. Red wins this time:

<img src="script-capture-4.png" alt="overwhelming red, as expected" width="600"/>

## Not sure why, but these colors are definitely being stored and read from `BGR` format

Can I apply a fun little red gradient effect, weakest in the top right and growing towards the bottom left?

Yep, and it looks pretty cool:

<img src="script-capture-5.png" alt="red gradient in bottom right corner" width="600"/>

What about a triple gradient in each of the three corners?

Oh, the whole image is just a gradient because none of the original pixel data is being used in the calculation. I guess I shouldn't be surprised by this:

<img src="script-capture-6.png" alt="triple gradient makes me vanish" width="600"/>

Good for you if you saw that coming. Now I want an angry red filter which grows from the center of the picture towards the edges.

This is what the red component of the image should look like:

<img src="script-capture-7.png" alt="center grayscale gradient" width="600"/>

It's calculated with the following function, which needs the x and y coordinate of the current pixel, the center of the image, and the degree of gradient falloff:

```python
def red_function(x, y, cx, cy, n):
    # calculate distance to center
    dx = abs(x - cx)
    dy = abs(y - cy)

    # calculate max distance to center
    max_d = np.sqrt(pow(cx, 2) + pow(cy, 2))

    # calculate actual distance to center
    d = np.sqrt(pow(dx, 2) + pow(dy, 2))

    # distance / max distance tells us how strong the red component should be
    f = d / float(max_d)

    # raise the fraction to the power of n, which will adjust the falloff
    red = pow(f, n) * 255

    return red
```

When applied to my image, I don't look quite as angry as I was hoping...

<img src="script-capture-8.png" alt="ANGRY RED BORDER" width="600"/>

Maybe I should increase the red value instead of replacing the red value, which will help the middle of the picture look less blue...

<img src="script-capture-9.png" alt="ANGRIER RED BORDER" width="600"/>

Yeah, that's better. Now increase the falloff to 6, and it's perfect:

<img src="script-capture-10.png" alt="ANGRIEST RED BORDER" width="600"/>

One problem... up until now I've only been testing on still images where I have as much processing time as I need.

## My algorithm is brutally slow

## My image links aren't working in github