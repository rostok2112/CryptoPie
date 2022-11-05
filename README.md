# Cesar-encryptor

Cesar cipher encryptor  with CLI interface

## Requirements

+ Python3
+ Optionally:
        + PipEnv

## Usage

```text
usage: python encrypt.py [-h] [-p [PATHES ...]] [-d DESTINATION] [-r] [-s SHIFT] [-b [BORDERS ...]]
                         [-e {utf-8, ascii, ...}]
                         input [input ...]

Simple CLI Cesar Encryptor/Decryptor

positional arguments:
  input                 An input text for encrypt

options:
  -h, --help            show this help message and exit
  -p [PATHES ...], --pathes [PATHES ...]
                        A path/pathes to a file/files/directory/directories
  -d DESTINATION, --destination DESTINATION, --dest DESTINATION
                        Destination path
  -r, --recursively     Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input
  -v, --verbose         Print results into stdout
  -s SHIFT, --shift SHIFT
                        The value by which the letters will be shifted relative to the alphabet
  -b [BORDERS ...], --borders [BORDERS ...]
                        Alphabet/alphabets borders in format: a-z A-Z а-я А-Я
  -e {utf-8, ascii, ...}, --encoding {utf-8, ascii, ...}
                        Encoding of texts of input and output files
```

Use by:

```bash
cd src/
python encrypt.py [options] <input>
```

Or if pipenv installed:

`pipenv run encrypt [options] <input>`
