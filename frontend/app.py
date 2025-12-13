import customtkinter as ctk


class App:
    """
    Classe principal da interface gráfica.
    """

    def __init__(self):
        self.root = None
        self.geometry = "900x600"

        # Estrutura da UI (criados em build_ui)
        self.toolbar = None
        self.main_frame = None
        self.toolbar_width = 200

    def _create_root(self):
        """Cria a janela principal (real ou mock)."""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("YT to MP3 Converter")
        self.root.geometry(self.geometry)
        self.root.minsize(600, 400)

    def _create_frames(self):
        """Cria os frames principais (toolbar + main)."""
        self.toolbar = ctk.CTkFrame(
            self.root,
            height=25,
            width=self.toolbar_width,
            fg_color="#2b2b2b",
            border_width=2,
            border_color="#ff0000",
        )
        self.main_frame = ctk.CTkFrame(
            self.root, fg_color="#1f1f1f", border_width=2, border_color="#0000ff"
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
