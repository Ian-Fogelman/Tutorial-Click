from click.testing import CliRunner
from mycli import greet
from mycli import return_pokemon

# Test the first CLI command
runner = CliRunner()
result = runner.invoke(greet, ['--name', 'Alice'])
print(result.output)
#print(result.return_value) #(Optional) print the `return_vale` context from the results...

# Test the second CLI command
runner = CliRunner()
result = runner.invoke(return_pokemon, ['--pokemon', 'Bulbasaur'])
print(result.output)

# TODO: Add more tests for future commands...