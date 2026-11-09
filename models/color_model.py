import cv2
import numpy as np


class ColorModel:
    """
    Responsável por gerenciar transformações e conversões de espaços de cores
    (RGB, Tons de Cinza, HSV, LAB, RGBA, CMYK).
    """

    @staticmethod
    def to_gray(bgr_image):
        if bgr_image is None:
            return None
        if len(bgr_image.shape) == 2:
            return bgr_image.copy()
        gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def to_hsv(bgr_image):
        if bgr_image is None:
            return None
        return cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    @staticmethod
    def to_lab(bgr_image):
        if bgr_image is None:
            return None
        return cv2.cvtColor(bgr_image, cv2.COLOR_BGR2LAB)

    @staticmethod
    def to_rgba(bgr_image):
        if bgr_image is None:
            return None
        return cv2.cvtColor(bgr_image, cv2.COLOR_BGR2BGRA)

    @staticmethod
    def extract_channel(bgr_image, channel_index):
        """
        Extrai um canal específico (0: B, 1: G, 2: R) e o retorna como imagem monocromática.
        """
        if bgr_image is None or len(bgr_image.shape) < 3:
            return None
        channel = bgr_image[:, :, channel_index]
        return cv2.cvtColor(channel, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def get_pixel_values(bgr_image, x, y):
        """
        Retorna os valores dos canais para as coordenadas (x, y) fornecidas.
        """
        if bgr_image is None:
            return None
        h, w = bgr_image.shape[:2]
        if 0 <= x < w and 0 <= y < h:
            b, g, r = [int(v) for v in bgr_image[y, x][:3]]
            return {
                "RGB": (r, g, b),
                "BGR": (b, g, r),
                "Gray": int(0.299 * r + 0.587 * g + 0.114 * b)
            }
        return None

