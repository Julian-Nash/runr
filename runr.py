#!env/bin/python

import click
import rcssmin
import rjsmin
import sass

import os
import time

"""
pip install click rcssmin rjsmin libsass black bandit
"""


class Runner:

    tasks_failed = 0
    tasks_complete = 0
    src_files_not_found = []
    dest_files_not_found = []

    black_options = "--line-length 120 --exclude env"
    # bandit_options = "" :TODO

    def __init__(self):
        self.start = time.time()

    def compile_scss(self):

        mapping = {"app/static/scss/style.scss": "app/static/css/style.css"}

        click.secho("\nCompiling SCSS to CSS")
        click.secho("--------------------")

        for source, dest in mapping.items():
            if os.path.isfile(source):
                with open(dest, "w") as outfile:
                    try:
                        outfile.write(sass.compile(filename=source))
                        click.secho(f"src: {source}", fg="green")
                        click.secho(f"dst: {dest}", fg="green")
                        self.tasks_complete += 1
                    except Exception as e:
                        click.secho(e)
                        self.tasks_failed += 1
                        continue
            else:
                click.secho(f"src not found: {source}", fg="red")
                self.src_files_not_found.append(source)
                self.tasks_failed += 1

    def minify_css(self):

        mapping = {"app/static/css/style.css": "app/static/css/style.min.css"}

        click.secho("\nMinifying CSS")
        click.secho("--------------------")

        for source, dest in mapping.items():
            if os.path.isfile(source):
                with open(source, "r") as infile:
                    if os.path.isfile(dest):
                        with open(dest, "w") as outfile:
                            outfile.write(rcssmin.cssmin(infile.read()))
                            click.secho(f"src: {source}", fg="green")
                            click.secho(f"dst: {dest}", fg="green")
                            self.tasks_complete += 1
                    else:
                        click.secho(f"dest not found: {dest}", fg="red")
                        self.dest_files_not_found.append(dest)
                        self.tasks_failed += 1
            else:
                click.secho(f"src not found: {source}", fg="red")
                self.src_files_not_found.append(source)
                self.tasks_failed += 1

    def minify_js(self):

        mapping = {"app/static/js/app.js": "app/static/js/app.min.js"}

        click.secho("\nMinifying JavaScript")
        click.secho("--------------------")

        for source, dest in mapping.items():
            if os.path.isfile(source):
                with open(source, "r") as infile:
                    if os.path.isfile(dest):
                        with open(dest, "w") as outfile:
                            outfile.write(rcssmin.cssmin(infile.read()))
                            click.secho(f"src: {source}", fg="green")
                            click.secho(f"dst: {dest}", fg="green")
                            self.tasks_complete += 1
                    else:
                        click.secho(f"dest not found: {dest}", fg="red")
                        self.dest_files_not_found.append(dest)
                        self.tasks_failed += 1
            else:
                click.secho(f"src not found: {source}", fg="red")
                self.src_files_not_found.append(source)
                self.tasks_failed += 1

    def format_code(self, path):
        click.secho("\nFormatting with black")
        click.secho("--------------------")
        os.system(f"black {self.black_options} {path}")

    def bandit(self, path):
        click.secho("\nRunning Bandit")
        click.secho("--------------------")
        # os.system(f"bandit {self.bandit_options} {path}")

    def report(self):
        click.secho("\nRunner report", fg="magenta")
        click.secho("--------------------")
        click.secho(f"Tasks complete: {self.tasks_complete}")
        click.secho(f"Tasks failed: {self.tasks_failed}")
        click.secho(f"Time elapsed: {round(time.time() - self.start, 4)} s")
        if self.src_files_not_found:
            click.secho("src files not found:")
            for f in self.src_files_not_found:
                click.secho(f"> {f}")
        if self.dest_files_not_found:
            click.secho("dest files not found:")
            for f in self.dest_files_not_found:
                click.secho(f"> {f}")
        click.secho()


@click.command()
@click.option("-c", "--compile", help="Compile SCSS to CSS", type=click.Choice(["scss"]))
@click.option("-m", "--minify", help="Minify files", type=click.Choice(["css", "js", "all"]))
@click.option("-f", "--fmt", help="Run Black Python linter")
@click.option("-b", "--bandit", help="Run Bandit security linter")
def runr(compile=None, minify=None, fmt=None, bandit=None):

    click.secho("\nRunner started", fg="magenta")
    click.secho("--------------------")

    runner = Runner()

    if compile:
        if compile == "scss":
            runner.compile_scss()

    if minify:
        if minify == "css":
            runner.minify_css()
        elif minify == "js":
            runner.minify_js()
        elif minify == "all":
            runner.minify_css()
            runner.minify_js()

    if fmt:
        runner.format_code(fmt)

    runner.report()


if __name__ == "__main__":
    runr()
