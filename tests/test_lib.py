# All the library level tests will live here.
import lib_template as lib

def test_hello_world_lib():
    assert lib.hello_world() == "Hello World!"

def test_hello_mcu_lib():
    assert lib.hello_mcu() == "Hello MCU!"

def test_say_hello_lib():
    assert lib.say_hello("hello") == 'Hello World!'
    assert lib.say_hello("MCU") == 'Hello MCU!'