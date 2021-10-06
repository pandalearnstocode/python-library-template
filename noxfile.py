import nox


@nox.session
def tests(session):
    session.install("pytest")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "--import-order-style", "google")

def hello():
    return "hello"

def add():
    return 1 + 1


def add_2():
    return 2 + 2


def multiplication():
    return 2 * 2

def add_3():
    return 3 + 3



def add_4():
    return 4 + 4