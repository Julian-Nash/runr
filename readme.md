## Python modular task runner CLI

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

Compile SCSS to CSS:

```sh
python runr.py -c scss
```

Minify CSS:

```sh
python runr.py -m css
```

Minify JavaScript:

```sh
python runr.py -m js
```

Minify all:

```sh
python runr.py -m all
```

Format with Black:

```sh
python runr.py -f .
```

Security lint with Bandit:

```sh
python runr.py -b .
```

#### Requirements

```sh
pip install click rcssmin rjsmin libsass black bandit
```

#### Dependencies

| Package | Description | Reference |
| --- | --- | --- |
| click | Command line tool | <a href="https://github.com/pallets/click">https://github.com/pallets/click</a> |
| rcssmin | CSS minifier | <a href="https://github.com/ndparker/rcssmin">https://github.com/ndparker/rcssmin</a> |
| rjsmin | JavaScript minifier | <a href="https://github.com/ndparker/rjsmin">https://github.com/ndparker/rjsmin</a> |
| libsass | SCSS to CSS compiler | <a href="https://github.com/sass/libsass-python">https://github.com/sass/libsass-python</a> |
| black | Python code formatter | <a href="https://github.com/ambv/black">https://github.com/ambv/black</a> |
| bandit | Python security linter | <a href="https://github.com/PyCQA/bandit">https://github.com/PyCQA/bandit</a> |

#### Extending

- Add a class method to the `Runner class`
- Add a new `click.option` to the `runr` function
- Call the new method from the `runr` function