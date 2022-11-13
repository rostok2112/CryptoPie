import argparse
import pkgutil
import encodings

parser = argparse.ArgumentParser(
    prog = "python crypto_pie.py",
    description="Encryptor/Decryptor with CLI interface",
)

subparsers = parser.add_subparsers(help="List of purposes handlers", dest="purpose",)

encrypt_parser = subparsers.add_parser("encrypt",  help="Encrypt options")
decrypt_parser = subparsers.add_parser("decrypt",  help="Decrypt options")

encrypt_parser.add_argument(
    "-g",
    "--generate_key", 
    action="store_true",
    help="Generate random key",
)

# + Start of getting set of encodings
false_positives = set(["aliases"])
encodings_set = set(name for imp, name, ispkg in pkgutil.iter_modules(encodings.__path__) if not ispkg)
encodings_set.difference_update(false_positives)
# + End of getting set of encodings

general_args = [
    {
        "kwargs" : {
            "choices": [
                "cesar", 
                "replacement",
            ],
            "type" : str,
            "help" : "A cryptographic algorithm for encryption/decryption",
        },
        "args" : [
            "method",
        ]
    },
    {
        "kwargs" : {
            "nargs" : "*",
            "type" : str,
            "action" : "extend",
            "default" : [],
            "help" : "An input text for processing",

        },
        "args" : [
            "input",
        ]
    },
    {
        "kwargs" : {
            "nargs" : "*",
            "type" : str,
            "action" : "extend",
            "default" : [],
            "help" : "A path/pathes to a input file/files/directory/directories",

        },
        "args" : [
            "-p",
            "--pathes",
        ]
    },
    {
        "kwargs" : {
            "type" : str,
            "default" : "outout",
            "help" : "Destination path",
        },
        "args" : [
            "-d",
            "--destination",
            "--dest",
        ]
    },
    {
        "kwargs" : {
            "action" : "store_true",
            "help" : "Recursively encrypt/decrypt everuthing in input path. Doesnt do anything if file on input",

        },
        "args" : [
            "-r",
            "--recursively",
        ]
    },
    {
        "kwargs" : {
            "action" : "store_true",
            "help" : "Print results into stdout",

        },
        "args" : [
            "-v",
            "--verbose",
        ]
    },
    {
        "kwargs" : {
            "nargs" : '*',
            "action" : "extend",
            "default" : ["a-z", "A-Z"],
            "help" : "Alphabet/alphabets borders in format: a-z A-Z а-я А-Я",

        },
        "args" : [
            "-b",
            "--borders",
        ]
    },
    {
        "kwargs" : {
            "choices" : list(encodings_set),
            "default" : "UTF-8",
            "help" : "Encoding of texts of input and output files",

        },
        "args" : [
            "-e",
            "--encoding",
        ]
    },
    {
        "kwargs" : {
            "help" : "The value by which an input will be encrypted/decrypted",
        },
        "args" : [
            "-k",
            "--key",
        ]
    },
]

for arg in general_args:
    encrypt_parser.add_argument(*arg["args"], **arg["kwargs"])
    decrypt_parser.add_argument(*arg["args"], **arg["kwargs"])

args = parser.parse_args()

if not len(args.input) and not len(args.pathes):
   parser.error("At least one of input texts or input pathes (--pathes) required")

if args.purpose == "encrypt" and bool(args.key) == bool(args.generate_key): # if not or specified at the same time 
   parser.error("Specify key by -k (--key) key OR set -g (--generate_key) (not at the same time)")

if not args.key and args.purpose == "decrypt":
    parser.error("Specify key by -k (--key) key for decryption")
