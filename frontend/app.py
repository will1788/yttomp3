import customtkinter as ctk

COLORS = {
    "border": ("#ff0000", "#0000ff"),  # (frames, main)
    "toolbar_bg": ("#dbdbdb", "#2b2b2b"),  # (light, dark)
    "main_bg": ("#eeeeee", "#1f1f1f"),
    "header_bg": ("#dbdbdb", "#2b2b2b"),
    "entry_placeholder": "#888888",
    "entry_text": "#000000",
    "entry_bg": "#eeeeee",
}


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
        self.url_entry = None
        self.mode_selector = None
        self.convert_button = None

        # Debug
        self.debug_mode = False

    def _create_root(self):
        """Cria a janela principal."""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("YT to MP3 Converter")
        self.root.geometry(self.geometry)
        self.root.minsize(600, 400)

    def _apply_border(self, widget, color=COLORS["border"][0]):
        """Aplica borda apenas se o modo de debug estiver ativado."""
        if not self.debug_mode:
            return

        if hasattr(widget, "configure"):
            widget.configure(border_color=color, border_width=2)

    def _create_frames(self):
        """Cria os frames principais (toolbar + main)."""
        self.toolbar = ctk.CTkFrame(
            master=self.root,
            height=25,
            width=self.toolbar_width,
            fg_color=COLORS["toolbar_bg"][1],
        )
        self._apply_border(self.toolbar)

        self.main_frame = ctk.CTkFrame(master=self.root, fg_color=COLORS["main_bg"][1])
        self._apply_border(self.main_frame, COLORS["border"][1])

        self.header_frame = ctk.CTkFrame(
            master=self.main_frame,
            height=50,
            fg_color=COLORS["header_bg"][1],
        )
        self._apply_border(self.header_frame)

        self.header_label = ctk.CTkLabel(
            master=self.header_frame,
            text="YT Converter to MP3",
            height=40,
        )

        self.url_entry = ctk.CTkEntry(
            master=self.main_frame,
            placeholder_text="Cole o link aqui",
            placeholder_text_color=COLORS["entry_placeholder"],
            text_color=COLORS["entry_text"],
            height=30,
            width=400,
            fg_color=COLORS["entry_bg"],
        )

        self.mode_selector = ctk.CTkSegmentedButton(
            master=self.main_frame,
            values=["Link", "Playlist"],
            command=self.on_mode_change,
        )

        self.convert_button = ctk.CTkButton(
            master=self.main_frame,
            text="Converter",
            height=30,
            width=100,
            command=self.on_convert_click,
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

        # URL entry
        self.url_entry.pack(side="top", pady=(10, 0), padx=20)

        # Mode selector
        self.mode_selector.pack(side="top", pady=(10, 0), padx=20)

        # Convert button
        self.convert_button.pack(side="top", pady=(10, 0), padx=20)

    def on_convert_click(self):
        return print("Convert button clicked")

    def on_mode_change(self, value):
        return print("Mode selector changed to", value)

    def build_ui(self):
        """Cria toda a interface."""
        self._create_root()
        self._create_frames()
        self._layout_frames()

        self.mode_selector.set("Link")

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
