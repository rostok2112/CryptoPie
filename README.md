# CryptoPie

Encryptor and decryptor with implemented collection of encryption algorithms and CLI interface

## Requirements

- Python3
- Optionally:
  - PipEnv

## Dependencies installation

If you have pipenv you can install or update dependencies by:

```bash
pipenv sync
```

Else:

```bash
pip install -r requirements.txt
```

Install new dependencies  if you have pipenv:

```bash
pipenv install <name_of_package>
pipenv requirements > requirements.txt
```

Else:

```bash
pip install <name_of_package>
pip freeze > requirements.txt
```

## Usage

```text
usage: python crypto_pie.py [-h] {encrypt,decrypt} [-p [PATHES ...]] [-d DESTINATION] [-r] [-k KEY] [-b [BORDERS ...]]
                         [-e {utf-8, ascii, ...}]
                         {cesar,replacement,additive_stream} ... input [input ...]

Encryptor/Decryptor with CLI interface

positional arguments:
  {encrypt,decrypt}     List of purposes handlers
    encrypt             Encrypt options
      options:
        -h, --help            show help message
        -p [PATHES ...], --pathes [PATHES ...]
                              A path/pathes to a file/files/directory/directories
        -d DESTINATION, --destination DESTINATION, --dest DESTINATION
                              Destination path
        -r, --recursively     Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input
        -v, --verbose         Print results into stdout
        -k KEY, --key KEY     The value by which an input will be encrypted/decrypted
        -g, --generate_key  Generate random key
        -b [BORDERS ...], --borders [BORDERS ...]
                              Alphabet/alphabets borders in format: a-z A-Z а-я А-Я
        -e {utf-8, ascii, ...}, --encoding {utf-8, ascii, ...}
                              Encoding of texts of input and output files
    decrypt             Decrypt options
      options:
        -h, --help            show help message
        -p [PATHES ...], --pathes [PATHES ...]
                              A path/pathes to a file/files/directory/directories
        -d DESTINATION, --destination DESTINATION, --dest DESTINATION
                              Destination path
        -r, --recursively     Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input
        -v, --verbose         Print results into stdout
        -k KEY, --key KEY     The value by which an input will be encrypted/decrypted
        -g, --generate_key  Generate random key
        -b [BORDERS ...], --borders [BORDERS ...]
                              Alphabet/alphabets borders in format: a-z A-Z а-я А-Я
        -e {utf-8, ascii, ...}, --encoding {utf-8, ascii, ...}
                              Encoding of texts of input and output files
  {cesar,substitution, additive_stream}   A cryptographic algorithm for encryption/decryption
    cesar 
      key format:
        integer_num,  -inf <= integer_num <= inf
        May be any positive or negative integer
    substitution
      key format:
        value_to_be_replaced1:value_to_replace1,value_to_be_replaced2:value_to_replace1,...
        Sequence of pairs of values to be replace and values to replace and values to be replaced by this value
    additive_stream
      key format:
        interval_to_encrypt1:interval1_key1,interval1_key2,interval1_key3,...;interval_to_encrypt2:interval2_key1,interval2_key2,interval2_key3,...;... interval_to_encrypt1 - in format a-z, A-Z; 0 <=interval_key <= length of interval
        Sequence of pairs of intervals to encrypt and sequence of keys for encryption. The length of keys sequence must be greater than 3 or equal to count + 1 of characters if count is lesser than 3. It is best if the length of the keys sequence is equal to the count of characters of the input text 
options:
        -h, --help            show help message
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
