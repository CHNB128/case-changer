from __future__ import annotations

import functools
import inspect
from typing import Callable, Tuple

import click

import case_changer.changers


def _wrap_command(cmd: Tuple[str, Callable]):
    # wrap around each command as the CLI takes a variable list of strings to
    # change and each case changer only takes a single string as argument
    @functools.wraps(cmd[1])
    def wrapper(*args, **kwargs):
        for s in kwargs.pop('strings', ()):
            click.echo(cmd[1](s))

    # wrap a command around (wrap the main argument around the callback)
    return click.command(cmd[0].replace('_case', ''))(
            click.argument(
                    'strings',
                    nargs=-1,
                    type=click.STRING)(wrapper)
    )


@click.group()
def cli():
    pass


[cli.add_command(_wrap_command(a))
 for a in inspect.getmembers(case_changer.changers)
 if (not a[0].startswith('_') and inspect.isfunction(a[1]))]

if __name__ == "__main__":
    cli.main()
