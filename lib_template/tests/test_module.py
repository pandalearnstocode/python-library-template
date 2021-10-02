# All the main module level tests and all the tests which require interation with the other sub-modules should live here.

import pytest

from lib_template.main import say_hello


def test_say_hello():
    assert say_hello("hello") == "Hello World!"
    assert say_hello("MCU") == "Hello MCU!"
