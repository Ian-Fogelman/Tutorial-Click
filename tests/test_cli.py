from my_cli_project.cli import process_text
from my_cli_project.cli import requests
from my_cli_project.cli import return_pokemon

def test_process_text():
    assert process_text("hello") == "HELLO"
    assert process_text("") == ""
    assert process_text("Test") == "TEST"

def test_pokemon():
    assert return_pokemon('Charizard') != ""