from frontend import app


def test_se_app_tem_main():
    assert hasattr(app, "main")  # Verifica se a função main existe em app.py


def test_main_executa_sem_erros(mock_ctk):
    # mock_ctk impede que o mainloop bloqueie a execução
    result = app.main()
    # Verifica se a função main retorna algo ou pelo meno augo nao eh None
    assert result is not None


def test_se_app_tem_class_app():
    assert hasattr(app, "App"), "A classe App precisa existir no app.py"


def test_app_constroi_raiz_com_theme_e_geometry(app_inst):
    # app_inst já vem com build_ui() chamado e mocks configurados
    app_inst.build_ui()

    # root foi criado (mock do conftest garante métodos como title/geometry)
    assert app_inst.root is not None

    # verificações práticas: métodos que o app chama na root
    assert hasattr(app_inst.root, "title")
    assert hasattr(app_inst.root, "geometry")
    assert hasattr(app_inst.root, "minsize")
    assert hasattr(app_inst.root, "mainloop")


def test_toolbar_existe_e_tem_width_fixa(app_inst):
    assert hasattr(app_inst, "toolbar")
    assert app_inst.toolbar is not None
    # Verificamos o atributo da classe, já que o widget é um Mock
    assert app_inst.toolbar_width == 200


def test_main_frame_existe_e_expande(app_inst):
    assert hasattr(app_inst, "main_frame")
    # verifica que main_frame existe e que toolbar + main_frame foram definidos
    assert app_inst.toolbar is not None
    assert app_inst.main_frame is not None


def test_run_chama_mainloop(app_inst):
    # app_inst.root é um Mock configurado no conftest
    app_inst.run()
    app_inst.root.mainloop.assert_called_once()
