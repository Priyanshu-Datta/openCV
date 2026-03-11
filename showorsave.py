import cv2
img = cv2.imread('test.JPG')

if img is None:
    print('Could not load the image.')
else:
    print('Image loaded successfully.')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print('choose \n1. Show the image \n2. Save the image')
    choice = int(input('Enter your choice: '))
    if choice ==1:
        cv2.imshow('Grayscale Image', gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif choice == 2:
        cv2.imwrite('gray_test.jpg', gray)
        print('Image saved as "gray_test.jpg" successfully.')