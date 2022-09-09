"""
import cv2

# load images
image1 = cv2.imread("Images/first.jpg")
image2 = cv2.imread("Images/second.jpg")

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
cv2.imwrite('Images/first.jpg', image1)
cv2.imwrite('Images/second.jpg', image1)
cv2.imwrite('diff.jpg', difference)
skimage.metrics.structural_similarity
"""
import numpy as np
from skimage.metrics import structural_similarity
import argparse
import imutils
import cv2

# 2. Construct the argument parse and parse the arguments
""""ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True, help="Images/first.jpg")
ap.add_argument("-s", "--second", required=True, help="Images/second.jpg")
args = vars(ap.parse_args())
"""""

# 3. Load the two input images


# When we use difference against registered image
image1 = cv2.imread("Images/registered.jpg")
image2 = cv2.imread("Images/second.jpg")
# 4. Convert the images to grayscaleWhen we resize(same size) images directly and compare them
# image1 = cv2.imread("Images/first.jpg")
# image2 = cv2.imread("Images/second.jpg")
# 
# scale_percentage=60
# width=int(image1.shape[1]*scale_percentage/100)
# height=int(image1.shape[1]*scale_percentage/100)
# 
# width=int(image2.shape[1]*scale_percentage/100)
# height=int(image2.shape[1]*scale_percentage/100)
# dim=(width,height)
# image1=cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)
# image2=cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)

grayA = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# 5. Compute the Structural Similarity Index (SSIM) between the two
#    images, ensuring that the difference image is returned
(score, diff) = structural_similarity(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print(diff)

# 6. Printing score
print("SSIM: {}".format(score))
result=(1-float(format(score)))*100
print("Change in scene :", result,"%")
