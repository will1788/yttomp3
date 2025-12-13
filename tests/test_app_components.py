# tests/test_app_components.py
from frontend import app


def test_components_exist_and_callbacks(app_inst):
    # app_inst já vem configurado via conftest.py com mocks

    # Root criado
    assert app_inst.root is not None

    # Frames principais
    assert hasattr(app_inst, "toolbar")
    assert hasattr(app_inst, "main_frame")

    # Layout flags (criadas no build_ui)
    assert hasattr(app_inst, "toolbar_layout")
    assert hasattr(app_inst, "main_layout")

    # ===== CALLBACKS EXISTENTES =====
    assert hasattr(app_inst, "run")  # método principal de execução
    assert hasattr(app, "main")  # função main do módulo
