import cv2, numpy as np, matplotlib.pyplot as plt
import original, translation, rotation, affine, perspective

img = cv2.imread('C:/Users/Mashu/OneDrive/Pictures/hima.png')

while True:
    print("=======================")
    print("1. Gray Image")
    print("2. Translation Image")
    print("3. Rotation Image")
    print("4. Affine Image")
    print("5. Perspective Image")
    print("0. Exit Program")
    print("=======================")
    menu = input("Masukkan pilihan : ")

    if menu == "1":
        hasil = original.original_image(img)
        plt.imshow(hasil, cmap='gray')
        plt.title("Original")
        plt.axis("off")
        plt.show()

    elif menu == "2":
        hasil = translation.translate_image(img)
        plt.imshow(hasil, cmap='gray')
        plt.title("Translation")
        plt.axis("off")
        plt.show()

    elif menu == "3":
        hasil = rotation.rotate_image(img)
        plt.imshow(hasil, cmap='gray')
        plt.title("Rotation")
        plt.axis("off")
        plt.show()

    elif menu == "4":
        hasil = affine.affine_image(img)
        plt.imshow(hasil, cmap='gray')
        plt.title("Affine")
        plt.axis("off")
        plt.show()

    elif menu == "5":
        hasil = perspective.perspective_image(img)
        plt.imshow(hasil, cmap='gray')
        plt.title("Perspective")
        plt.axis("off")
        plt.show()

    elif menu == "0":
        break