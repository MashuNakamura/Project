import cv2, matplotlib.pyplot as plt

def rotate_image(img):
    rows, cols = img.shape[:2]
    center = (cols // 2, rows // 2)
    M_rotate = cv2.getRotationMatrix2D(center, 45, 1)
    rotated = cv2.warpAffine(img, M_rotate, (cols, rows))
    rotated_gray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
    return rotated_gray