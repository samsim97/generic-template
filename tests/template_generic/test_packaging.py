import template_generic


def test_version() -> None:
    """Check to see that we can get the package version"""
    assert template_generic.__version__ is not None
