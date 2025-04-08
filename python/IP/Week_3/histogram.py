import cv2, matplotlib.pyplot as plt

img = cv2.imread('C:/Users/Mashu/OneDrive/Pictures/hima.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure(figsize=(10,4))

while True:
    print("=======================")
    print("1. Original Image")
    print("2. Histogram Image")
    print("0. Exit Program")
    print("=======================")
    menu = input("Masukkan pilihan : ")

    if menu == "1":
        plt.subplot(1, 2, 1)
        plt.imshow(gray, cmap='gray')
        plt.title('Grayscale Image')
        plt.axis('off')

    elif menu == "2":
        plt.subplot(1, 2, 2)
        plt.plot(hist, color='black')
        plt.title('Grayscale Histogram')
        plt.xlabel('Pixel Intensity')
        plt.ylabel('Frequency')

    elif menu =="0":
        break
    
    plt.show()