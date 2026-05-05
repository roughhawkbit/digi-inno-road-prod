def is_in_google_colab():
    try:
        import google.colab  # type: ignore
        return True
    except ImportError:
        return False