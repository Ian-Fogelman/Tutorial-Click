A small repo dedicated to desigining a CLI tool with Python via Click and built by the Poetry.
For details, see:

- [Click](https://click.palletsprojects.com/en/stable/)
- [Poetry](https://python-poetry.org/docs/)

### Instructions

1. `pip install poetry` | `pip install click` - install poetry module
2. `poetry install` - install project dependencies
    > [!NOTE]  
    > If you need to add dependencies again for poetry (it is its own virtual env), use :`poetry add requests`.
3. `poetry run mycli "hello world"` - test the cli
4. `poetry build` - build the /dist folder
5. `pip install dist/my_cli_project-0.1.0.tar.gz` - install the cli locally
6. Open a new terminal window and try the cli: `mycli --help`
7. (Optional) `poetry publish` - publish to pypi requires credentials
   ```
    poetry config repositories.my-repo https://my-repo-url/simple/
    poetry config http-basic.my-repo username password
    poetry publish --repository my-repo
   ```
7. Open a new terminal window.
   Run the following command(s):

    | Command                               | Description                             |
    |---------------------------------------|-----------------------------------------|
    | `mycli return_pokemon --pokemon charizard` | Returns data or details about the Pokémon named "charizard". |
    | `mycli greet --name ian`              | Prints a greeting message for the name "ian". |
    | `mycli reverse abc`                   | Reverses the string "abc".              |
    | `mycli cap abc`                       | Capitalizes the string "abc".           |

### Testing

To run the test files in `/tests`, from the root directory execute the following command:
```bash
poetry run pytest
```
- Todo: possible to use runner.py to test cli commands more effectively? 

### Tagging 

To add a tag to a branch, use `git tag v0.0.1`.

To trigger a test build, add a tag matching the `v0.0.0` naming convention:

```
git checkout main
git tag v0.0.1
git push origin refs/tags/v0.0.1
```

Optionally:

```
git tag -f v0.0.1 HEAD
```
