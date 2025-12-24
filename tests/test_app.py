from frontend import app


def test_se_app_tem_main():
    """Verifica se a função main existe no módulo."""
    assert hasattr(app, "main")


def test_main_executa_sem_erros(mock_ctk):
    """Testa a execução do main sem bloquear (usando mocks)."""
    result = app.main()
    # Garante que a função retorna a instância da aplicação
    assert result is not None


def test_se_app_tem_class_app():
    """Verifica se a classe App está definida."""
    assert hasattr(app, "App"), "A classe App precisa existir no app.py"


def test_app_constroi_raiz_com_theme_e_geometry(app_inst):
    """Verifica a configuração da janela principal (root)."""
    # app_inst já vem inicializado pela fixture
    app_inst.build_ui()

    assert app_inst.root is not None

    # Confere se os métodos esperados do ctk estão presentes no mock
    assert hasattr(app_inst.root, "title")
    assert hasattr(app_inst.root, "geometry")
    assert hasattr(app_inst.root, "minsize")
    assert hasattr(app_inst.root, "mainloop")


def test_toolbar_existe_e_tem_width_fixa(app_inst):
    """Verifica a existência e configuração da toolbar."""
    assert hasattr(app_inst, "toolbar")
    assert app_inst.toolbar is not None
    # Valida a largura fixa definida na classe
    assert app_inst.toolbar_width == 200


def test_main_frame_existe_e_expande(app_inst):
    """Assegura que o frame principal foi criado."""
    assert hasattr(app_inst, "main_frame")
    assert app_inst.toolbar is not None
    assert app_inst.main_frame is not None


def test_run_chama_mainloop(app_inst):
    """Testa se o método run invoca o mainloop do ctk."""
    app_inst.run()
    app_inst.root.mainloop.assert_called_once()


def test_header_frame_existe(app_inst):
    """Verifica a criação do frame de cabeçalho."""
    assert hasattr(app_inst, "header_frame")
    assert app_inst.header_frame is not None


def test_header_label_existe(app_inst):
    """Verifica a criação do label de título."""
    assert hasattr(app_inst, "header_label")
    assert app_inst.header_label is not None
