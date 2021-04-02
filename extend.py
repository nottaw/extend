import os
import click
import filetype


EXTENSIONS = set(kind.extension for kind in filetype.TYPES)

checked_dirs = 0
checked_files = 0
renamed = 0


@click.command()
@click.argument("paths", nargs=-1, type=click.Path(exists=True))
def extend(paths):
    for path in paths:
        check(path)
    click.echo(
        f"Checked {checked_dirs} director{'y' if checked_dirs == 1 else 'ies'}\n"
        f"Checked {checked_files} file{'' if checked_files == 1 else 's'}\n"
        f"Renamed {renamed} file{'' if renamed == 1 else 's'}"
    )

def check(path):
        global checked_dirs, checked_files, renamed
        if os.path.isdir(path):
            entries = os.listdir(path)
            for entry in entries:
                check(entry)
            checked_dirs += 1
        elif os.path.isfile(path):
            extension = os.path.splitext(path)[1][1:]
            if extension not in EXTENSIONS:
                kind = filetype.guess(path)
                if kind:
                    os.rename(path, f"{path}.{kind.extension}")
                    renamed += 1
            checked_files += 1


if __name__ == "__main__":
    extend()
