def test_defaults(cookies):
    result = cookies.bake()
    assert result.project.isdir()
    assert result.exit_code == 0
    assert result.exception is None
