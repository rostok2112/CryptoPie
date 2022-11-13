import argparse
import pkgutil
import encodings

parser = argparse.ArgumentParser(
    prog = 'python crypto_pie.py',
    description='Encryptor/Decryptor with CLI interface'
)
parser.add_argument(
    "method",
    choices=["cesar", "replacement"],
    type=str,
    help="A cryptographic algorithm for encryption/decryption"
)

subparsers = parser.add_subparsers(help='List of purposes handlers', dest='purpose')

encrypt_parser = subparsers.add_parser('encrypt',  help='Encrypt options')
decrypt_parser = subparsers.add_parser('decrypt',  help='Decrypt options')

parser.add_argument(
    "input",
    nargs='*',
    type=str,
    action="extend",
    default=[],
    help="An input text for encrypt"
)

parser.add_argument(
    "-p",
    "--pathes",
    nargs='*',
    type=str,
    action="extend",
    default=[],
    help="A path/pathes to a input file/files/directory/directories"
)

parser.add_argument(
    "-d",
    "--destination",
    "--dest",
    default="output",
    type=str,
    help='Destination path'
)

parser.add_argument(
    "-r",
    "--recursively", 
    action="store_true",
    help="Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input"
)
parser.add_argument(
    "-v",
    "--verbose", 
    action="store_true",
    help="Print results into stdout"
)
parser.add_argument(
    "-b",
    "--borders", 
    nargs='*',
    type=str,
    action="extend",
    default=["a-z", "A-Z"],
    help="Alphabet/alphabets borders in format: a-z A-Z а-я А-Я"
)

false_positives = set(["aliases"])
encodings_set = set(name for imp, name, ispkg in pkgutil.iter_modules(encodings.__path__) if not ispkg)
encodings_set.difference_update(false_positives)

parser.add_argument(
    "-e",
    "--encoding", 
    choices=list(encodings_set),
    default="UTF-8",
    help="Encoding of texts of input and output files"
)

encrypt_parser.add_argument(
    "-g",
    "--generate_key", 
    action="store_true",
    help="Generate random key"
)

encrypt_parser.add_argument(
    
)

decrypt_parser.add_argument(
    "input",
    nargs='*',
    type=str,
    action="extend",
    default=[],
    help="An input text for encrypt"
)

general_args = [
    {
        'kwargs' : {
            "nargs" : "*",
            "type" : str,
            "action" : "extend",
            "default" : [],
            "help" : "An input text for encrypt",

        },
        'args' : [
            "input",
        ]
    },
    {
        'kwargs' : {
            'help' : "The value by which an input will be encrypted/decrypted",
        },
        'args' : [
            "-k",
            "--key",
        ]
    },
]

for arg in general_args:
    encrypt_parser.add_argument(*arg['args'], **arg['kwargs'])
    decrypt_parser.add_argument(*arg['args'], **arg['kwargs'])

args = parser.parse_args()

if not len(args.input) and not len(args.pathes):
   parser.error("At least one of input texts or input pathes (--pathes) required")

if args.purpose == "encrypt" and bool(args.key) == bool(args.generate_key): # if not or specified at the same time 
   parser.error("Specify key by -k (--key) key OR set -g (--generate_key) (not at the same time)")

if not args.key and args.purpose == "decrypt":
    parser.error("Specify key by -k (--key) key for decryption")
