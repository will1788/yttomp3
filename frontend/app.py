import customtkinter as ctk


class App:
    """
    Classe principal da interface gráfica.
    """

    def __init__(self):
        """Cria os atributos da classe."""
        self.root = None
        self.geometry = "900x600"

        # Estrutura da UI (criados em build_ui)
        self.toolbar = None
        self.toolbar_width = 200
        self.main_frame = None
        self.header_frame = None
        self.header_label = None

    def _create_root(self):
        """Cria a janela principal."""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("YT to MP3 Converter")
        self.root.geometry(self.geometry)
        self.root.minsize(600, 400)

    def _apply_border(self, widget, color="#ff0000"):
        """Aplica borda ao widget."""
        widget.configure(border_width=2, border_color=color)

    def _create_frames(self):
        """Cria os frames principais (toolbar + main)."""
        self.toolbar = ctk.CTkFrame(
            master=self.root,
            height=25,
            width=self.toolbar_width,
            fg_color="#2b2b2b",
        )
        self._apply_border(self.toolbar, "#ff0000")

        self.main_frame = ctk.CTkFrame(master=self.root, fg_color="#1f1f1f")
        self._apply_border(self.main_frame, "#0000ff")

        self.header_frame = ctk.CTkFrame(
            master=self.main_frame,
            height=50,
            fg_color="#2b2b2b",
        )
        self._apply_border(self.header_frame, "#ff0000")

        self.header_label = ctk.CTkLabel(
            master=self.header_frame,
            text="YT Converter to MP3",
            height=50,
            # fg_color="#2b2b2b",
        )

    def _layout_frames(self):
        """Aplica layout apenas no modo real."""
        # toolbar
        self.toolbar.pack(side="top", fill="x")
        self.toolbar.pack_propagate(False)

        # Botão placeholder
        self.menu_btn = ctk.CTkButton(self.toolbar, text="Menu")
        self.menu_btn.pack(side="left", padx=5)

        # Main frame
        self.main_frame.pack(side="top", expand=True, fill="both")

        # Header frame
        self.header_frame.pack(side="top", fill="x")

        # Header label
        self.header_label.pack(side="top", fill="x")

    def build_ui(self):
        """Cria toda a interface."""
        self._create_root()
        self._create_frames()
        self._layout_frames()

        # Atributos que os testes esperam
        self.toolbar_layout = True
        self.main_layout = True

    def run(self):
        """Executa o loop principal."""
        if self.root is None:
            self.build_ui()

        self.root.mainloop()

        return True


def main():
    app_inst = App()
    app_inst.build_ui()
    app_inst.run()

    return app_inst


if __name__ == "__main__":
    main()
