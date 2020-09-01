import pytest


@pytest.fixture
def context():
    return {
        "project_domain": "ashe.kr",
        "project_name": "My Test Project",
        "project_slug": "my_test_project",
        "author": "tech@ashe.kr",
        "database": "sqlite3",
        "cloud_provider": "none",
        "use_drf": "y",
    }


def test_defaults(cookies, context):
    """Test that project is generated and fully rendered."""
    result = cookies.bake(extra_context={**context})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context["project_slug"]
    assert result.project.isdir()
