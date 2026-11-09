import cv2
import numpy as np


class ThresholdModel:
    """
    Responsável por operações de limiarização e segmentação de imagens
    (Global, Otsu, Adaptativo e Multissegmentado).
    """

    @staticmethod
    def _to_gray_uint8(image):
        if image is None:
            return None
        if len(image.shape) == 3:
            return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image.copy()

    @staticmethod
    def global_threshold(image, thresh_val=127, max_val=255, invert=False):
        gray = ThresholdModel._to_gray_uint8(image)
        if gray is None:
            return None
        thresh_type = cv2.THRESH_BINARY_INV if invert else cv2.THRESH_BINARY
        _, binary = cv2.threshold(gray, thresh_val, max_val, thresh_type)
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def otsu_threshold(image, invert=False):
        gray = ThresholdModel._to_gray_uint8(image)
        if gray is None:
            return None
        thresh_type = (cv2.THRESH_BINARY_INV if invert else cv2.THRESH_BINARY) | cv2.THRESH_OTSU
        _, binary = cv2.threshold(gray, 0, 255, thresh_type)
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def adaptive_threshold(image, method='mean', block_size=11, c=2):
        gray = ThresholdModel._to_gray_uint8(image)
        if gray is None:
            return None
        # block_size deve ser ímpar e > 1
        block_size = max(3, block_size if block_size % 2 != 0 else block_size + 1)
        adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C if method == 'gaussian' else cv2.ADAPTIVE_THRESH_MEAN_C
        binary = cv2.adaptiveThreshold(gray, 255, adaptive_method, cv2.THRESH_BINARY, block_size, c)
        return cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

    @staticmethod
    def multilevel_threshold(image, levels=4):
        """
        Quantização em múltiplos tons (ex: 2, 4, 8, 16 níveis de cinza).
        """
        gray = ThresholdModel._to_gray_uint8(image)
        if gray is None:
            return None

        levels = max(2, min(levels, 256))
        step = 256.0 / levels
        quantized = (np.floor(gray / step) * (255.0 / (levels - 1))).astype(np.uint8)
        return cv2.cvtColor(quantized, cv2.COLOR_GRAY2BGR)

