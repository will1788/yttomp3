import pytest


@pytest.fixture
def mock_ctk(mocker):
    """
    Fixture que mocka os componentes do customtkinter em frontend.app.
    Permite testar a aplicação como se fosse real (test_mode=False),
    mas sem abrir janelas gráficas.
    """
    # Mock da janela principal (root)
    fake_root = mocker.Mock()
    fake_root.title = mocker.Mock()  # Mock do método title
    fake_root.geometry = mocker.Mock()  # Mock do método geometry
    fake_root.minsize = mocker.Mock()  # Mock do método minsize
    fake_root.mainloop = mocker.Mock()  # Mock do método mainloop

    # Patches nos componentes do ctk importados no app.py
    mocks = {
        "root": fake_root,  # Mock da janela principal
        "CTk": mocker.patch(
            "frontend.app.ctk.CTk", return_value=fake_root
        ),  # Mock do CTk
        "CTkFrame": mocker.patch(
            "frontend.app.ctk.CTkFrame", return_value=mocker.Mock()
        ),  # Mock do frame
        "CTkButton": mocker.patch(
            "frontend.app.ctk.CTkButton", return_value=mocker.Mock()
        ),  # Mock do botão
        "CTkEntry": mocker.patch(
            "frontend.app.ctk.CTkEntry", return_value=mocker.Mock()
        ),  # Mock do campo de entrada
        "CTkLabel": mocker.patch(
            "frontend.app.ctk.CTkLabel", return_value=mocker.Mock()
        ),  # Mock do label
        "CTkSegmentedButton": mocker.patch(
            "frontend.app.ctk.CTkSegmentedButton", return_value=mocker.Mock()
        ),  # Mock do botão de seleção
        "set_appearance_mode": mocker.patch(
            "frontend.app.ctk.set_appearance_mode"
        ),  # Mock do modo de aparencia
        "set_default_color_theme": mocker.patch(
            "frontend.app.ctk.set_default_color_theme"
        ),  # Mock do tema de cor
    }
    return mocks


@pytest.fixture
def app_inst(mock_ctk):
    """
    Retorna uma instância da App inicializada com a UI construída (via mocks).
    """
    from frontend.app import App

    # Usamos test_mode=False para exercitar o código real de construção da UI,
    # mas os mocks do mock_ctk impedem a criação real da janela.
    app = App()
    app.build_ui()
    return app
