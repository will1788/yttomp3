import os


def test_project_structure():
    expected_folders = [
        "frontend",
        "backend",
        "assets",
        "config",
        "bin",
        "core",
        "temp",
    ]

    for folder in expected_folders:
        assert os.path.isdir(folder), f"Pasta '{folder}' está faltando!"
