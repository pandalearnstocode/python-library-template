# All the sub module 1 related tests will be here.
# These will be mostly unit tests. 
import pytest
import lib_template.sub_module_1 as sub_module_1


def test_hello_world():
    assert sub_module_1.hello_world() == "Hello World!"
