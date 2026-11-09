import tkinter as tk


class MenuBar:
    def __init__(self, root, controller):
        self.controller = controller
        self.menubar = tk.Menu(root)

        # Menu Arquivo
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Abrir...", command=controller.open_image)
        file_menu.add_command(label="Salvar como...", command=controller.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Restaurar Original", command=controller.reset_image)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=root.quit)
        self.menubar.add_cascade(label="Arquivo", menu=file_menu)

        # Menu Cores
        color_menu = tk.Menu(self.menubar, tearoff=0)
        color_menu.add_command(label="Tons de Cinza", command=controller.apply_gray)
        color_menu.add_command(label="Espaço HSV", command=controller.apply_hsv)
        color_menu.add_command(label="Espaço LAB", command=controller.apply_lab)
        self.menubar.add_cascade(label="Cores", menu=color_menu)

        # Menu Histograma
        hist_menu = tk.Menu(self.menubar, tearoff=0)
        hist_menu.add_command(label="Visualizar Histograma", command=controller.show_histogram)
        hist_menu.add_command(label="Equalizar Histograma", command=controller.apply_equalization)
        self.menubar.add_cascade(label="Histograma", menu=hist_menu)

        # Menu Limiarização
        thresh_menu = tk.Menu(self.menubar, tearoff=0)
        thresh_menu.add_command(label="Otsu (Automático)", command=controller.apply_otsu)
        thresh_menu.add_command(label="Adaptativa (Média)", command=controller.apply_adaptive_thresh)
        thresh_menu.add_command(label="Multissegmentação (4 níveis)", command=controller.apply_multilevel_thresh)
        self.menubar.add_cascade(label="Limiarização", menu=thresh_menu)
