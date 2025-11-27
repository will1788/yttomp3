class App:
    def __init__(self):
        pass  # Implementação da classe App


def main(test_mode=False):
    app_instance = App()

    if test_mode:
        return app_instance

    # Código normal da função main
    return app_instance


if __name__ == "__main__":
    main()
