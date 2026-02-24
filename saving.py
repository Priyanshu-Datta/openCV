import cv2

image = cv2.imread('test.JPG')

if image is None:
    print('Could not read the image.')
else:
    print('Image read successfully.')
    success = cv2.imwrite('test_copy.JPG', image)
    if success:
        print("Image saved successfully at 'test_copy.JPG'.")
    else:
        print('Failed to save the image.')
    

