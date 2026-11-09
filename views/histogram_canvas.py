import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class HistogramCanvas:
    """
    Componente para exibição de gráficos de histograma utilizando Matplotlib embutido no Tkinter.
    Pode ser utilizado em uma janela flutuante (Toplevel) ou embutido em um Frame.
    """

    def __init__(self, parent):
        self.parent = parent
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.figure.patch.set_facecolor('#222222')
        self.ax = self.figure.add_subplot(111)
        self._format_axes()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.parent)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def _format_axes(self):
        self.ax.set_facecolor('#1e1e1e')
        self.ax.tick_params(colors='white', labelsize=8)
        self.ax.spines['bottom'].set_color('#555555')
        self.ax.spines['top'].set_color('#555555')
        self.ax.spines['left'].set_color('#555555')
        self.ax.spines['right'].set_color('#555555')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.title.set_color('white')
        self.ax.grid(True, linestyle='--', alpha=0.3, color='#888888')

    def plot_histogram(self, hist_data, title="Histograma da Imagem"):
        """
        Plota os dados do histograma fornecidos pelo HistogramModel.
        """
        self.ax.clear()
        self._format_axes()
        self.ax.set_title(title, fontsize=10, pad=10)
        self.ax.set_xlabel("Intensidade (0 - 255)", fontsize=8)
        self.ax.set_ylabel("Frequência de Pixels", fontsize=8)
        self.ax.set_xlim([0, 256])

        if not hist_data:
            self.canvas.draw()
            return

        if 'Gray' in hist_data:
            self.ax.plot(hist_data['Gray'], color='#aaaaaa', linewidth=1.5, label='Escala de Cinza')
        else:
            for name, (data, col) in hist_data.items():
                hex_color = '#4da6ff' if col == 'b' else '#66ff66' if col == 'g' else '#ff6666'
                self.ax.plot(data, color=hex_color, linewidth=1.2, label=name)

        self.ax.legend(facecolor='#333333', edgecolor='#555555', labelcolor='white', fontsize=8)
        self.figure.tight_layout()
        self.canvas.draw()

    @staticmethod
    def show_popup(parent, hist_data, title="Análise de Histograma"):
        """
        Abre uma nova janela (Toplevel) para exibição do histograma.
        """
        window = tk.Toplevel(parent)
        window.title(title)
        window.geometry("640x480")
        window.configure(bg="#222222")

        hist_comp = HistogramCanvas(window)
        hist_comp.plot_histogram(hist_data, title=title)
        return window

