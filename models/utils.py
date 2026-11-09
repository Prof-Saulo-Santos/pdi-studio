import cv2
import numpy as np
from PIL import Image, ImageTk


def to_tk_image(cv_image, max_size=(1100, 750)):
    """
    Converte uma imagem do formato OpenCV (BGR ou Grayscale) para ImageTk.PhotoImage.
    Redimensiona para exibição na interface sem alterar a matriz original do modelo.
    """
    if cv_image is None:
        return None

    # Se for imagem em escala de cinza (2D), converte para RGB
    if len(cv_image.shape) == 2:
        rgb = cv2.cvtColor(cv_image, cv2.COLOR_GRAY2RGB)
    elif cv_image.shape[2] == 4:
        rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGRA2RGBA)
    else:
        rgb = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

    img = Image.fromarray(rgb)

    if max_size is not None:
        img.thumbnail(max_size, Image.Resampling.LANCZOS)

    try:
        return ImageTk.PhotoImage(img)
    except RuntimeError:
        # Permite execução em ambientes sem display/X11 (ex: scripts e testes)
        return img


def bgr_to_cmyk(bgr_image):
    """
    Converte uma imagem BGR (OpenCV) para o espaço CMYK.
    Retorna uma tupla (C, M, Y, K) de matrizes normalizadas (0 a 255).
    """
    if bgr_image is None:
        return None

    # Converte BGR para RGB e normaliza para [0, 1]
    rgb = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB).astype(float) / 255.0
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]

    # K = 1 - max(R, G, B)
    k = 1.0 - np.maximum(np.maximum(r, g), b)
    denom = 1.0 - k
    denom[denom == 0] = 1.0

    c = (1.0 - r - k) / denom
    m = (1.0 - g - k) / denom
    y = (1.0 - b - k) / denom

    c[k == 1.0] = 0.0
    m[k == 1.0] = 0.0
    y[k == 1.0] = 0.0

    c_uint = (c * 255).astype(np.uint8)
    m_uint = (m * 255).astype(np.uint8)
    y_uint = (y * 255).astype(np.uint8)
    k_uint = (k * 255).astype(np.uint8)

    return c_uint, m_uint, y_uint, k_uint
