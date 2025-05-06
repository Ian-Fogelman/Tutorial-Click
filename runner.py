from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli, ['greet', '--name', 'Alice'])
print(result.output)  # Outputs: Hello, Alice!\nCommand returned: Hello, Alice!\n
print(result.return_value)  # Outputs: Hello, Alice!