def test_import_package():
    import goit_pycore_hw_03

    assert isinstance(goit_pycore_hw_03.__version__, str)
