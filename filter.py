import cv2
import numpy as np

def apply_blur(image, ksize):
    if ksize > 1:
        ksize = ksize if ksize % 2 == 1 else ksize + 1
        return cv2.GaussianBlur(image, (ksize, ksize), 0)
    return image

# def apply_sharpness(image, alpha):
#     if alpha > 0:
#         kernel = np.array([[0, -1, 0],
#                            [-1, 5 + alpha, -1],
#                            [0, -1, 0]])
#         return cv2.filter2D(image, -1, kernel)
#     return image

def apply_sharpness(image, strength):
    if strength <= 0:
        return image

    blurred = cv2.GaussianBlur(image, (0, 0), sigmaX=2)
    return cv2.addWeighted(image, 1 + strength, blurred, -strength, 0)


def apply_brightness(image, beta):
    if beta != 0:
        return cv2.convertScaleAbs(image, alpha=1, beta=beta)
    return image

def apply_contrast(image, alpha):
    if alpha != 1.0:
        return cv2.addWeighted(image, alpha, image, 0, 128 * (1 - alpha))
    return image

def apply_edge_auto_canny(image, enabled):
    if not enabled:
        return image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    v = np.median(gray)
    lower = int(max(0, 0.66 * v))
    upper = int(min(255, 1.33 * v))
    edges = cv2.Canny(gray, lower, upper)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def apply_grayscale(image, enabled):
    if enabled:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    return image