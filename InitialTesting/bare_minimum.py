import cv2
import numpy as np

print("Starting script")

cap = cv2.VideoCapture(0)

print("Started video capture")

ret, frame = cap. read ()

print("Read from video capture")

ret, frame = cap. read ()

# mirror the original video frame so that every video frame appears correct
frame = cv2.flip(frame, 1)

# gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# inversion = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# sketch = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# sketch = cv2.medianBlur(sketch,3)
canny = cv2.Canny(frame,100,200)
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# sketch_update = cv2.adaptiveThreshold(sketch,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,5,5)
# X_ray_image = cv2.bitwise_not(frame)
# thresh, blackAndWhiteFrame = cv2.threshold(gray_frame, 115, 280,cv2.THRESH_BINARY)
# resized_blacknwhite = cv2.resize(blackAndWhiteFrame, (350,350))
# resized_inv = cv2.resize(inversion, (350,350))
# resized_canny = cv2.resize(canny, (350,350))
# resized_sketch = cv2.resize(sketch_update, (350,350))
# resized_x_ray = cv2.resize(X_ray_image, (350,350))
# resized_gray = cv2.resize(gray, (350,350))
# cv2.imshow('Gray Image',resized_gray)
# cv2.imshow('black_and_white', resized_blacknwhite)
# cv2.imshow('original', frame)
# cv2.imshow('sketch_update art', resized_sketch)
# cv2.imshow('Canny Edge',resized_canny)
cv2.imshow('Canny Edge',canny)
# cv2.imshow('X_Ray', resized_x_ray)
# cv2.imshow('inversion', resized_inv)
# if cv2.waitKey(10) & 0xFF==ord('q'):
#         break

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
        frame[ii, jj, 0] = ((frame.shape[0] - ii) / float(frame.shape[0])) * (jj / float(frame.shape[1])) * 255
        frame[ii, jj, 1] = (ii / float(frame.shape[0])) * ((frame.shape[1] - jj) / float(frame.shape[1])) * 255
        frame[ii, jj, 2] = (ii / float(frame.shape[0])) * (jj / float(frame.shape[1])) * 255

cv2.imshow('Edited', frame)

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