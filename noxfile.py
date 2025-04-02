from nox_poetry import session


@session(python="3.13")
def tests(session):
    """Run tests from ``tests``"""
    session.install("pytest", ".")
    session.run("pytest")


@session(python="3.13")
def formatter(session) -> None:
    """Run ruff code formatter"""
    # args = session.posargs or locations
    session.install("ruff")
    session.run("ruff", "format")
