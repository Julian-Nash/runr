#### Python modular task runner CLI

Usage:

```sh
python runr.py --help
```

```sh
Usage: runr.py [OPTIONS]

Options:
  -c, --compile [scss]       Compile SCSS to CSS
  -m, --minify [css|js|all]  Minify files
  -f, --black TEXT           Run Black Python linter
  -b, --bandit TEXT          Run Bandit security linter
  --help                     Show this message and exit.
```

#### Requirements

```sh
pip install click rcssmin rjsmin libsass black bandit
```

#### Dependencies

| Package | Description |
| --- | --- |
| click | Command line tool |
| rcssmin | CSS minifier |
| rjsmin | JavaScript minifier |
| libsass | SCSS to CSS compiler |
| black | Python code formatter |
| bandit | Python security linter |

#### Extending

- Add a class method to the `Runner class`
- Add a new `click.option` to the `runr` function
- Call the new method from `runr`