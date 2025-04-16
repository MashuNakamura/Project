import cv2, numpy as np
def affine_image(img):
    rows, cols = img.shape[:2]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M_affine = cv2.getAffineTransform(pts1, pts2)
    affine = cv2.warpAffine(img, M_affine, (cols, rows))
    affine_gray = cv2.cvtColor(affine, cv2.COLOR_BGR2GRAY)
    return affine_gray