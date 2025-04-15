import cv2
import numpy as np
import matplotlib.pyplot as plt

def transformation_3d(img):
    img = cv2.imread("C:/Users/Mashu/OneDrive/Pictures/hima.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w = img.shape[:2]

    src_pts = np.float32([
        [0, 0], # Kiri atas
        [w - 1, 0], # Kanan atas
        [0, h - 1], # Kiri bawah
        [w - 1, h - 1] # Kanna bawah
    ])

    depth_factor = 1
    dst_pts = np.float32([
        [w * 0.1, h * 0.2 - depth_factor * 50],
        [w * 0.9, h * 0.1 - depth_factor * 50],
        [w * 0.2, h * 0.9 + depth_factor * 50],
        [w * 0.8, h * 0.8 + depth_factor * 50]
    ])
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)

    transformed = cv2.warpPerspective(img, M, (w, h))
    
    return transformed