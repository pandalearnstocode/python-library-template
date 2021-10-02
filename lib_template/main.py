import lib_template.sub_module_1 as sub_module_1
import lib_template.sub_module_2 as sub_module_2


def say_hello(type_of_greeting):
    if type_of_greeting == "hello":
        return sub_module_1.hello_world()
    else:
        return sub_module_2.hello_mcu()
