# All the sub module 2 level tests should be here
from lib_template import sub_module_2


def test_hello_mcu():
    assert sub_module_2.hello_mcu() == "Hello MCU!"
