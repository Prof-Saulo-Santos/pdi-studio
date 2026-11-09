import cv2
import numpy as np


class HistogramModel:
    """
    Responsável pelo cálculo de dados estatísticos, histogramas
    e operações de equalização e ajuste de brilho/contraste.
    """

    @staticmethod
    def calculate_histogram(image):
        """
        Calcula os histogramas para uma imagem.
        Retorna um dicionário com os dados por canal ('gray' ou 'b', 'g', 'r').
        """
        if image is None:
            return None

        hist_data = {}
        if len(image.shape) == 2 or (len(image.shape) == 3 and image.shape[2] == 1):
            hist = cv2.calcHist([image], [0], None, [256], [0, 256])
            hist_data['Gray'] = hist.flatten()
        else:
            # Imagem colorida BGR
            colors = ('b', 'g', 'r')
            names = ('Azul (B)', 'Verde (G)', 'Vermelho (R)')
            for i, (col, name) in enumerate(zip(colors, names)):
                hist = cv2.calcHist([image], [i], None, [256], [0, 256])
                hist_data[name] = (hist.flatten(), col)

        return hist_data

    @staticmethod
    def equalize(image):
        """
        Aplica equalização de histograma.
        Se colorida, converte temporariamente para YCrCb ou escala de cinza.
        """
        if image is None:
            return None

        if len(image.shape) == 2:
            equalized = cv2.equalizeHist(image)
            return cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

        # Equaliza o canal de luminância (Y) no espaço YCrCb para manter as cores
        ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

    @staticmethod
    def adjust_brightness_contrast(image, brightness=0, contrast=0):
        """
        Ajusta brilho (-100 a 100) e contraste (-100 a 100).
        """
        if image is None:
            return None

        # alpha: ganho de contraste (1.0 = normal)
        # beta: deslocamento de brilho
        alpha = float((contrast + 100.0) / 100.0)
        beta = float(brightness)

        return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

