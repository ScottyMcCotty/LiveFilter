import cv2
import numpy as np

def red_function(x, y, cx, cy, n):
    dx = abs(x - cx)
    dy = abs(y - cy)

    max_d = np.sqrt(pow(cx, 2) + pow(cy, 2))
    d = np.sqrt(pow(dx, 2) + pow(dy, 2))

    f = d / float(max_d)

    red = pow(f, n) * 255

    return red

print("Starting script")

cap = cv2.VideoCapture(0)

print("Started video capture")

ret, frame = cap. read ()

print("Read from video capture")

while True:

    ret, frame = cap. read ()

# mirror the original video frame so that every video frame appears correct
    frame = cv2.flip(frame, 1)

    for ii in range(frame.shape[0]):
        for jj in range(frame.shape[1]):
            # angry red border
            # set the red component based on the distance to the middle
            # frame[ii, jj, 2] = min(255, frame[ii, jj, 2] + red_function(ii, jj, frame.shape[0]/2, frame.shape[1]/2, 6))
            pass
            
    canny = cv2.Canny(frame,100,200)
    
    cv2.imshow('original', frame)
    
    if cv2.waitKey(10) & 0xFF==ord('q'):
            break

print("Exited while loop")

cap. release ()

print("Released video capture")


# maximize the red component of each pixel
for ii in range(frame.shape[0]):
    for jj in range(frame.shape[1]):

        # this is WRONG, colors are stored in BGR format
        # frame[ii, jj, 0] = 255

        # makes overwhelming red
        # frame[ii, jj, 2] = 255

        # triple gradient
        # frame[ii, jj, 0] = ((frame.shape[0] - ii) / float(frame.shape[0])) * (jj / float(frame.shape[1])) * 255
        # frame[ii, jj, 1] = (ii / float(frame.shape[0])) * ((frame.shape[1] - jj) / float(frame.shape[1])) * 255
        # frame[ii, jj, 2] = (ii / float(frame.shape[0])) * (jj / float(frame.shape[1])) * 255

        # angry red border
        # set the red component based on the distance to the middle
        frame[ii, jj, 2] = min(255, frame[ii, jj, 2] + red_function(ii, jj, frame.shape[0]/2, frame.shape[1]/2, 6))

# lets adjust canny too, because I want to see the grayscale version of this
for ii in range(canny.shape[0]):
    for jj in range(canny.shape[1]):
        canny[ii, jj] = red_function(ii, jj, canny.shape[0]/2, canny.shape[1]/2, 3)

cv2.imshow('Edited', frame)
cv2.imshow('Canny?', canny)

# print(frame)
print(canny)
print(type(canny))
print(canny.shape)
print(frame.shape)
# print(canny.__dict__)

# np.savetxt("canny.txt", canny, fmt='%1.0f')

# canny.tofile("canny.txt")

# with open("canny.txt", 'w') as f:
#     f.write(np.array2string(canny))
#     print("Saved canny to file")


while not (cv2.waitKey(1) & 0xFF==ord('f')):
    pass

cv2.destroyAllWindows()

print("Finished script")