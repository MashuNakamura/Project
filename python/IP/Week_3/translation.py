import cv2, numpy as np

def translate_image(img):
    rows, cols = img.shape[:2]
    M_translate = np.float32([[1, 0, 50], [0, 1, 100]])
    translated = cv2.warpAffine(img, M_translate, (cols, rows))
    translated_gray = cv2.cvtColor(translated, cv2.COLOR_BGR2GRAY)
    return translated_gray