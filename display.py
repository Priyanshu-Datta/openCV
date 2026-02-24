import cv2

image = cv2.imread('test.JPG')

if image is None:
    print('Could not read the image.')
else:
    print('Image read successfully.')
    cv2.imshow('Image showing', image)
    cv2.waitKey(0)
cv2.destroyAllWindows()