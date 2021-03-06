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

def add_5():
    return 5 + 5

def add_6():
    return 6 + 6


def add_7():
    return 7 + 7


def add_8():
    return 8 + 8