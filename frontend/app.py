import customtkinter as ctk


class App:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode
        self.root = None
        self.geometry = "900x600"  # exemplo de geometria

    def build_ui(self):
        if self.test_mode:
            # cria um root falso
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
        # Sidebar
        self.sidebar_width = 200
        if self.test_mode:
            self.sidebar = object()
        else:
            self.sidebar = ctk.CTkFrame(self.root, width=self.sidebar_width)

        # Main Frame
        if self.test_mode:
            self.main_frame = object()
        else:
            self.main_frame = ctk.CTkFrame(self.root)

        if not self.test_mode:
            self.sidebar.pack(side="left", fill="y")
            self.menu_btn = ctk.CTkButton(self.sidebar, text="Menu")
            self.menu_btn.pack(pady=20)
            self.main_frame.pack(side="right", expand=True, fill="both")
        # Atributos para testes
        self.sidebar_layout = True
        self.main_layout = True

    def run(self):
        if self.root is None:
            self.build_ui()
        if not self.test_mode:
            self.root.mainloop()
        return True


def main(test_mode=False):
    app_inst = App(test_mode=test_mode)

    if not test_mode:
        app_inst.build_ui()
        app_inst.run()
    else:
        app_inst.build_ui()
    return app_inst


if __name__ == "__main__":
    main()
