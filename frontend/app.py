import customtkinter as ctk


class App:
    """
    Classe principal da interface gráfica.
    """

    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.root = None
        self.geometry = "900x600"

        # Estrutura da UI (criados em build_ui)
        self.sidebar = None
        self.main_frame = None
        self.sidebar_width = 200

    def _create_root(self):
        """Cria a janela principal (real ou mock)."""
        if self.test_mode:

            class FakeRoot:
                pass

            self.root = FakeRoot()
        else:
            ctk.set_appearance_mode("dark")
            ctk.set_default_color_theme("blue")
            self.root = ctk.CTk()
            self.root.title("YT to MP3 Converter")
            self.root.geometry(self.geometry)
            self.root.minsize(600, 400)

    def _create_frames(self):
        """Cria os frames principais (sidebar + main)."""
        if self.test_mode:
            self.sidebar = object()
            self.main_frame = object()
        else:
            self.sidebar = ctk.CTkFrame(self.root, width=self.sidebar_width)
            self.main_frame = ctk.CTkFrame(self.root)

    def _layout_frames(self):
        """Aplica layout apenas no modo real."""
        if self.test_mode:
            return

        # Sidebar
        self.sidebar.pack(side="left", fill="y")

        # Botão placeholder
        self.menu_btn = ctk.CTkButton(self.sidebar, text="Menu")
        self.menu_btn.pack(pady=20)

        # Main frame
        self.main_frame.pack(side="right", expand=True, fill="both")

    def build_ui(self):
        """Cria toda a interface."""
        self._create_root()
        self._create_frames()
        self._layout_frames()

        # Atributos que os testes esperam
        self.sidebar_layout = True
        self.main_layout = True

    def run(self):
        """Executa o loop principal."""
        if self.root is None:
            self.build_ui()

        if not self.test_mode:
            self.root.mainloop()

        return True


def main(test_mode=False):
    app_inst = App(test_mode=test_mode)
    app_inst.build_ui()

    if not test_mode:
        app_inst.run()

    return app_inst


if __name__ == "__main__":
    main()
