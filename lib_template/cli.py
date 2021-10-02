import typer
from lib_template.sub_module_1 import hello_world
from lib_template.sub_module_2 import hello_mcu
from lib_template.main import say_hello


app = typer.Typer()


@app.command("hello")
def hello():
    hello_world()


@app.command("mcu")
def mcu():
    hello_mcu()


@app.command("say_hello")
def say_hello_app(type_of_greeting: str):
    say_hello(type_of_greeting)


if __name__ == "__main__":
    app()
