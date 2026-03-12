import cv2
img = cv2.imread('test.jpg')

if img is None:
    print('Could not open or find the image.')
else:
    print("image is loaded successfully")
    print('Original Dimensions : ', img.shape)
    resized = cv2.resize(img, (300, 300)) 
    print('Resized Dimensions : ', resized.shape)
    cv2.imwrite('resized_image.jpg', resized)
    
    choice = input("do you want to see the image? (y/n): ")
    if choice.lower() == 'y':
        cv2.imshow('original image', img)
        cv2.imshow('Resized Image', resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()