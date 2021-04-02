# extend

Command line script for adding extensions to file names

## Installation

    $ git clone https://github.com/2yr434hgd7fy384/extend
    $ pip install extend/

## Usage

    extend [OPTIONS] [PATHS]...

`extend` guesses the extension of a file using the `[filetype](https://github.com/h2non/filetype.py)` module, and adds that extension to the file name. A file will be ignored if it has an extension that `extend` recognises. `extend` will do nothing if it cannot guess the extension of a file.

Paths can be files or directories; `extend` will check directories recursively.
