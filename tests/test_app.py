from frontend import app


def test_app_has_main():
    assert hasattr(app, "main")  # Verifica se a função main existe em app.py


def test_main_executes_without_errors():
    app.main(test_mode=True)
    assert True, "A função main() não deve retornar None"


def test_app_has_class_app():
    assert hasattr(app, "App"), "A classe App precisa existir no app.py"


def test_main_returns_app_instance_in_test_mode():
    result = app.main(test_mode=True)
    assert isinstance(
        result, app.App
    ), "main() deve retornar uma instância de App quando test_mode=True"
