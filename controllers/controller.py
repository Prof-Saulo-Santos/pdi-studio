from tkinter import Tk, filedialog, messagebox
from models.model import Model
from views.histogram_canvas import HistogramCanvas
from views.view import View


class Controller:
    def __init__(self):
        self.root = Tk()
        self.root.title("PDI Studio - Sistema Interativo de Processamento de Imagens")
        self.root.geometry("1600x900")

        # Model
        self.model = Model()

        # View
        self.view = View(self.root, controller=self)

    # ========== Métodos principais ==========
    def run(self):
        self.root.mainloop()

    def _ensure_image_loaded(self):
        """
        Valida se há uma imagem carregada no sistema antes de aplicar qualquer operação.
        """
        if self.model.image is None:
            messagebox.showwarning("Aviso", "Nenhuma imagem carregada. Abra uma imagem primeiro.")
            return False
        return True

    def open_image(self):
        path = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Arquivos de imagem", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if path:
            image = self.model.load_image(path)
            if image is not None:
                self.view.display_image(image)
                self.view.log_action(f"Imagem carregada: {path}")
            else:
                messagebox.showerror("Erro", f"Não foi possível abrir a imagem: {path}")

    def save_image(self):
        if not self._ensure_image_loaded():
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")]
        )
        if path:
            self.model.save_image(path)
            self.view.log_action(f"Imagem salva em: {path}")

    def reset_image(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.reset_image()
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Imagem restaurada para o estado original.")

    # ========== Operações de Cores ==========
    def apply_gray(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.convert_to_gray()
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Conversão para tons de cinza aplicada.")

    def apply_hsv(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.convert_to_hsv()
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Conversão para o espaço HSV aplicada.")

    def apply_lab(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.convert_to_lab()
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Conversão para o espaço LAB aplicada.")

    # ========== Histograma ==========
    def show_histogram(self):
        if not self._ensure_image_loaded():
            return
        hist_data = self.model.get_histogram_data()
        if hist_data:
            HistogramCanvas.show_popup(self.root, hist_data, title="Análise de Histograma")
            self.view.log_action("Gráfico de histograma exibido.")

    def apply_equalization(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.equalize_histogram()
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Equalização de histograma aplicada.")

    # ========== Limiarização ==========
    def apply_otsu(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.apply_otsu_threshold()
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Limiarização de Otsu aplicada.")

    def apply_adaptive_thresh(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.apply_adaptive_threshold()
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Limiarização adaptativa aplicada.")

    def apply_multilevel_thresh(self):
        if not self._ensure_image_loaded():
            return
        result = self.model.apply_multilevel_threshold(levels=4)
        if result is not None:
            self.view.display_image(result)
            self.view.log_action("Limiarização multissegmentada (4 níveis) aplicada.")
