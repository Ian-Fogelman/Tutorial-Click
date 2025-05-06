# mycli.py
import click

@click.group()
def cli():
    """My CLI tool"""
    pass

@cli.command()
@click.option('--name', default='World', help='Name to greet')
def greet(name):
    """Greet the user"""
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    cli()