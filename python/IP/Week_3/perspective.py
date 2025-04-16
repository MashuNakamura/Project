import cv2, numpy as np

def perspective_image(img):
    rows, cols = img.shape[:2]
    pts1 = np.float32([[0, 0], [cols-1, 0], [0, rows-1], [cols-1, rows-1]])
    pts2 = np.float32([[50, 50], [cols-50, 50], [50, rows-50], [cols-50, rows-50]])
    M_perspective = cv2.getPerspectiveTransform(pts1, pts2)
    perspective = cv2.warpPerspective(img, M_perspective, (cols, rows))
    perspective_gray = cv2.cvtColor(perspective, cv2.COLOR_BGR2GRAY)
    return perspective_gray