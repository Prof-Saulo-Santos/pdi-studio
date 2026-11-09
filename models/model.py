import cv2
from models.color_model import ColorModel
from models.histogram_model import HistogramModel
from models.threshold_model import ThresholdModel
from models.utils import to_tk_image


class Model:
    def __init__(self):
        self.image = None
        self.original = None

    def load_image(self, path):
        self.image = cv2.imread(path)
        if self.image is not None:
            self.original = self.image.copy()
            return self.to_tk_image(self.image)
        return None

    def save_image(self, path):
        if self.image is not None:
            cv2.imwrite(path, self.image)

    def reset_image(self):
        if self.original is not None:
            self.image = self.original.copy()
            return self.to_tk_image(self.image)
        return None

    # ========== Operações de PDI ==========
    def convert_to_gray(self):
        if self.image is None:
            return None
        self.image = ColorModel.to_gray(self.image)
        return self.to_tk_image(self.image)

    def convert_to_hsv(self):
        if self.image is None:
            return None
        self.image = ColorModel.to_hsv(self.image)
        return self.to_tk_image(self.image)

    def convert_to_lab(self):
        if self.image is None:
            return None
        self.image = ColorModel.to_lab(self.image)
        return self.to_tk_image(self.image)

    def equalize_histogram(self):
        if self.image is None:
            return None
        self.image = HistogramModel.equalize(self.image)
        return self.to_tk_image(self.image)

    def get_histogram_data(self):
        if self.image is None:
            return None
        return HistogramModel.calculate_histogram(self.image)

    def apply_otsu_threshold(self):
        if self.image is None:
            return None
        self.image = ThresholdModel.otsu_threshold(self.image)
        return self.to_tk_image(self.image)

    def apply_adaptive_threshold(self):
        if self.image is None:
            return None
        self.image = ThresholdModel.adaptive_threshold(self.image)
        return self.to_tk_image(self.image)

    def apply_multilevel_threshold(self, levels=4):
        if self.image is None:
            return None
        self.image = ThresholdModel.multilevel_threshold(self.image, levels=levels)
        return self.to_tk_image(self.image)

    # ========== Conversão ==========
    def to_tk_image(self, cv_image):
        return to_tk_image(cv_image)
