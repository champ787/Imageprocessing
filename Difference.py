import cv2

# load images
import skimage

image1 = cv2.imread("Images/registered.jpg")
image2 = cv2.imread("Images/second.jpg")

scale_percentage=60
width=int(image1.shape[1]*scale_percentage/100)
height=int(image1.shape[1]*scale_percentage/100)

width=int(image2.shape[1]*scale_percentage/100)
height=int(image2.shape[1]*scale_percentage/100)

dim=(width,height)
image1=cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)
image2=cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

# compute difference
difference = cv2.subtract(image1, image2)

# color the mask red
Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
difference[mask != 255] = [0, 0, 255]

# add the red mask to the images to make the differences obvious
image1[mask != 255] = [0, 0, 255]
image2[mask != 255] = [0, 0, 255]

# store images
""""cv2.imwrite('Images/first.jpg', image1)
cv2.imwrite('Images/second.jpg', image1)"""""

cv2.imwrite('Images/difference.jpg', difference)
skimage.metrics.structural_similarity