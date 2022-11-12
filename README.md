# CryptoPie

Encryptor and decryptor with implemented collection of encryption algorithms and CLI interface

## Requirements

- Python3
- Optionally:
  - PipEnv

## Usage

```text
usage: python crypto_pie.py [-h] [-p [PATHES ...]] [-d DESTINATION] [-r] [-k KEY] [-b [BORDERS ...]]
                         [-e {utf-8, ascii, ...}]
                         {encrypt,decrypt} ... input [input ...]

Encryptor/Decryptor with CLI interface

positional arguments:
  {encrypt,decrypt}     List of purposes handlers
    encrypt             Encrypt options
      options:
        -h, --help          show help message
        -g, --generate_key  Generate random key
    decrypt             Decrypt options
      options:
        -h, --help  show help message
  input                 An input text for encrypt

options:
  -h, --help            show help message
  -p [PATHES ...], --pathes [PATHES ...]
                        A path/pathes to a file/files/directory/directories
  -d DESTINATION, --destination DESTINATION, --dest DESTINATION
                        Destination path
  -r, --recursively     Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input
  -v, --verbose         Print results into stdout
  -k KEY, --key KEY     The value by which an input will be encrypted/decrypted
  -b [BORDERS ...], --borders [BORDERS ...]
                        Alphabet/alphabets borders in format: a-z A-Z а-я А-Я
  -e {utf-8, ascii, ...}, --encoding {utf-8, ascii, ...}
                        Encoding of texts of input and output files
```

Use by:

```bash
cd src/
python crypto_pie.py [options] <input>
```

Or if pipenv installed:

```bash
pipenv run crypto_pie [options] <input>
```
