# mycli.py
import click
import requests 
import json

@click.group()
def cli():
    """My CLI tool"""
    pass

@cli.command(name='greet')
@click.option('--name', default='World', help='Name to greet')
def greet(name):
    """Greet the user"""
    greeting = f"Hello, {name}!"
    click.echo(greeting)
    return greeting

@cli.command(name='return_pokemon')
@click.option('--pokemon', default='charizard', help='Name of pokemon')
def return_pokemon(pokemon):
    r = requests.get('https://pokeapi.co/api/v2/pokemon/{pokemon}'.format(pokemon=pokemon))
    parsed = json.loads(r.text)
    retjson = json.dumps(parsed, indent=4)
    click.echo(retjson)
    return retjson

if __name__ == '__main__':
    cli()
    #cli(standalone_mode=False)) #uncomment to return values.