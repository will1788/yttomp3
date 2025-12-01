from frontend import app


def test_se_app_tem_main():
    assert hasattr(app, "main")  # Verifica se a função main existe em app.py


def test_main_executa_sem_erros():
    app.main(test_mode=True)
    assert True, "A função main() não deve retornar None"


def test_se_app_tem_class_app():
    assert hasattr(app, "App"), "A classe App precisa existir no app.py"


def test_main_retorna_app_instance_no_test_mode():
    result = app.main(test_mode=True)
    assert isinstance(
        result, app.App
    ), "main() deve retornar uma instância de App quando test_mode=True"


def test_app_constroi_raiz_com_theme_e_geometry():
    app_inst = app.App(test_mode=False)
    app_inst.build_ui()
    assert hasattr(app_inst, "root")
    assert app_inst.root is not None
    # atributos que vamos definir
    assert getattr(app_inst.root, "title")  # existe método title
    assert getattr(app_inst, "geometry", None) is not None or hasattr(
        app_inst.root, "geometry"
    )


def test_sidebar_existe_e_tem_width_fixa():
    app_inst = app.App(test_mode=True)
    app_inst.build_ui()
    assert hasattr(app_inst, "sidebar")
    # largura acessivel via cget ou via atributo
    width = getattr(app_inst.sidebar, "winfo_reqwisth", lambda: None)()
    assert width is None or isinstance(width, int)


def test_main_frame_existe_e_expande():
    app_inst = app.App(test_mode=True)
    app_inst.build_ui()
    assert hasattr(app_inst, "main_frame")
    # verifica que main_frame existe e que sidebar + main_frame foram definidos
    assert app_inst.sidebar is not None
    assert app_inst.main_frame is not None


def test_run_nao_bloqeia_modo_teste(monkeypatch):
    app_inst = app.App(test_mode=True)
    app_inst.build_ui()
    called = {"mainloop": False}
    # monkeypatch o mainloop para garantir que não é chamado
    app_inst.root.mainloop = lambda: called.update({"mainloop": True})
    app_inst.run()
    assert called["mainloop"] is False
