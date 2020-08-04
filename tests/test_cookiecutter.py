def test_defaults(cookies):
    result = cookies.bake()
    assert result.proejct.isdir()
    assert result.exit_code == 0
    assert result.exception is None
