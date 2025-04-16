import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Mashu/OneDrive/Pictures/hima.png')

# BGR ke RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# BGR ke HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# BGR ke Gray Scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# BGR ke LAB
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# BGR ke YUV


while True:
    print("=======================")
    print("1. Original IMG")
    print("2. PNG to RGB")
    print("3. PNG to HSV")
    print("4. PNG to Gray")
    print("5. PNG to LAB")
    print("6. PNG to YUV")
    print("0. Exit Program")
    print("=======================")
    menu = input("Masukkan pilihan : ")
    
    if menu == "1":
        plt.imshow(img[..., ::-1])  # BGR to RGB for display
        plt.title('Original Image')
        plt.axis('off')

    elif menu == "2":
        plt.imshow(img_rgb)
        plt.title('PNG to RGB Image')
        plt.axis('off')

    elif menu == "3":
        plt.imshow(img_hsv)
        plt.title('PNG to HSV Image')
        plt.axis('off')

    elif menu == "4":
        plt.imshow(img_gray, cmap='gray')
        plt.title('PNG to Grayscale Image')
        plt.axis('off')

    elif menu == "5":
        plt.imshow(img_lab)
        plt.title('PNG to LAB Image')
        plt.axis('off')

    elif menu == "6":
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        plt.imshow(img_yuv)
        plt.title('PNG to YUV Image')
        plt.axis('off')

    elif menu == "0":
        break
    
    plt.show()